import asyncio
import os
import re
import httpx
from playwright.async_api import async_playwright
from google.cloud import storage

# ==============================================================================
# BLOCO 1: CONFIGURAÇÕES E CONEXÃO COM O GOOGLE CLOUD (GCP)
# Alterar aqui: Nome do Bucket ou caminho da chave JSON
# ==============================================================================
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "scripts/gcp-credentials.json"
BUCKET_NAME = "perdoes-transparencia-raw"

async def upload_to_gcs(file_content, destination_blob_name):
    """Envia o conteúdo binário direto para o Google Cloud Storage"""
    try:
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        # Caminho final: bronze/portal_transparencia/ANO/arquivo_limpo.pdf
        blob = bucket.blob(f"bronze/portal_transparencia/{destination_blob_name}")
        blob.upload_from_string(file_content)
        print(f"   ✅ [GCS] Upload concluído: {destination_blob_name}")
    except Exception as e:
        print(f"   ❌ [GCS] Erro no upload: {e}")
# ==============================================================================


# ==============================================================================
# BLOCO 2: FERRAMENTAS DE APOIO (Limpeza de Nomes e Download)
# Não apagar: Funções auxiliares para o script funcionar
# ==============================================================================
def slugify(text):
    """Transforma 'RREO 5º Bimestre' em 'rreo_5_bimestre' para nome de arquivo"""
    text = text.lower()
    # Remove acentos e caracteres especiais, mantendo apenas letras e números
    text = re.sub(r'[^a-z0-9]+', '_', text).strip('_')
    return text

async def download_file(url):
    """Faz o download do arquivo via HTTP (mais rápido que pelo browser)"""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}
    try:
        async with httpx.AsyncClient(follow_redirects=True, headers=headers) as client:
            response = await client.get(url, timeout=30.0)
            return response.content if response.status_code == 200 else None
    except Exception as e:
        print(f"   ❌ [HTTP] Erro no download: {e}")
        return None
# ==============================================================================


# ==============================================================================
# BLOCO 3: LÓGICA DO ROBÔ (FILTRO GLOBAL DE LINKS)
# ==============================================================================
async def run_scraper(ano_alvo):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})
        page = await context.new_page()
        
        current_page = 1
        total_files = 0

        while True:
            url_listagem = f"https://perdoes.mg.gov.br/transparencia/publicacoes/tipo/{ano_alvo}/pagina-{current_page}"
            print(f"\n🔎 [Navegador] Lista: {url_listagem}")
            
            try:
                await page.goto(url_listagem, wait_until="domcontentloaded", timeout=60000)
                await page.wait_for_timeout(5000) # 5 segundos para o site carregar tudo
            except: break

            # ESTRATÉGIA GLOBAL: Pegamos TODOS os links '<a>' da página inteira
            todos_os_links = await page.locator("a").all()
            
            links_na_pagina = []
            for link_el in todos_os_links:
                href = await link_el.get_attribute("href")
                
                # Filtramos links que contenham o padrão de visualização de publicação
                if href and ("/publicacao/" in href or "/view/" in href):
                    # Removemos o domínio se ele já estiver lá para não duplicar depois
                    clean_href = href.replace("https://perdoes.mg.gov.br", "")
                    links_na_pagina.append(clean_href)

            # Remove duplicatas (um card pode ter o link na foto e no botão)
            links_na_pagina = list(set(links_na_pagina))

            if not links_na_pagina:
                print(f"⚠️  Nenhum link de publicação encontrado na página {current_page}.")
                break

            print(f"🔗 Extraídos {len(links_na_pagina)} links únicos. Iniciando abas...")

            for href in links_na_pagina:
                new_page = await context.new_page()
                try:
                    full_pub_url = f"https://perdoes.mg.gov.br{href if href.startswith('/') else '/' + href}"
                    print(f"   -> Abrindo aba: {full_pub_url}")
                    
                    await new_page.goto(full_pub_url, wait_until="domcontentloaded", timeout=45000)
                    await new_page.wait_for_timeout(3000)
                    
                    # Busca os botões de download
                    downloads = await new_page.locator("a[href*='getDownload']").all()
                    
                    for dl_btn in downloads:
                        title_attr = await dl_btn.get_attribute("title")
                        nome_doc = title_attr.replace("Fazer download do arquivo ", "") if title_attr else "documento"
                        
                        dl_url = await dl_btn.get_attribute("href")
                        if not dl_url.startswith("http"):
                            dl_url = f"https://perdoes.mg.gov.br{dl_url if dl_url.startswith('/') else '/' + dl_url}"
                        
                        print(f"      ⬇️  Baixando: {nome_doc[:40]}...")
                        
                        data = await download_file(dl_url)
                        if data:
                            ext = ".zip" if "zip" in dl_url.lower() else ".pdf"
                            final_name = f"{slugify(nome_doc)}{ext}"
                            await upload_to_gcs(data, f"{ano_alvo}/{final_name}")
                            total_files += 1
                except Exception as e:
                    print(f"   ❌ Erro na aba: {e}")
                finally:
                    await new_page.close()

            current_page += 1
            if current_page > 40: break

        print(f"\n🏆 Finalizado Ano {ano_alvo}! {total_files} arquivos enviados.")
        await browser.close()

# ==============================================================================
# BLOCO 4: EXECUÇÃO DO SCRIPT (MODO EM MASSA)
# Alterar aqui: O intervalo de anos que você deseja processar
# ==============================================================================
if __name__ == "__main__":
    # Definimos a lista de anos (2017 até 2026)
    # O range(2017, 2027) vai de 2017 até 2026 inclusive
    anos_para_coletar = range(2018, 2027)
    
    for ano in anos_para_coletar:
        print(f"\n" + "="*50)
        print(f"📅 INICIANDO COLETA GLOBAL: ANO {ano}")
        print("="*50)
        
        try:
            # Chama a função de extração para o ano atual do loop
            asyncio.run(run_scraper(ano))
        except Exception as e:
            print(f"💥 Erro crítico no ano {ano}: {e}")
            continue # Pula para o próximo ano se um falhar
            
    print("\n✅ [PIPELINE FINALIZADO] Todos os anos foram processados!")
# ==============================================================================