import re
import pandas as pd
from base_processor import BaseProcessor

class ContratoParser(BaseProcessor):
    def process_contrato_5733(self, pdf_filename):
        """Extrai itens e valores do contrato de gêneros alimentícios de 2017."""
        # Define o caminho completo do arquivo
        pdf_path = self.base_path / "data" / "docs" / pdf_filename
        
        if not pdf_path.exists():
            print(f"⚠️ Arquivo não encontrado: {pdf_path}")
            return None

        print(f"📑 Analisando Contrato: {pdf_filename}")
        
        with self.open_pdf(pdf_path) as pdf:
            # 1. EXTRAÇÃO DE METADADOS (PÁGINA 1)
            first_page = pdf.pages[0].extract_text()
            
            # Regex para pegar o número do contrato (ex: 5733/2017)
            match_contrato = re.search(r"Contrato:\s*(\d+/\d+)", first_page)
            num_contrato = match_contrato.group(1) if match_contrato else "N/A"
            
            # Regex para pegar o fornecedor (Comercial Angos LTDA)
            match_fornecedor = re.search(r"empresa\s*\n?(.*?LTDA.*?EPP)", first_page, re.DOTALL)
            fornecedor = match_fornecedor.group(1).replace("\n", " ").strip() if match_fornecedor else "Desconhecido"

            # 2. EXTRAÇÃO DA TABELA DE ITENS (PÁGINAS 1 E 2)
            all_rows = []
            for i in range(2): # Checa as duas primeiras páginas
                table = pdf.pages[i].extract_table()
                if table:
                    # Filtra linhas que possuem conteúdo real de itens
                    all_rows.extend([row for row in table if row[0] and row[0].isdigit()])

            # 3. TRATAMENTO DOS DADOS COM PANDAS
            # Colunas baseadas no layout do PDF de Perdões
            df = pd.DataFrame(all_rows, columns=["item_nro", "codigo", "descricao", "unidade", "qtd_valor"])
            
            # Limpeza: Remove quebras de linha indesejadas
            df = df.replace(r'\n', ' ', regex=True)
            
            # Adiciona os metadados em cada linha para a Silver Layer
            df["contrato_origem"] = num_contrato
            df["fornecedor_nome"] = fornecedor
            df["ano_exercicio"] = 2017
            df["municipio"] = "Perdões"

            return df

if __name__ == "__main__":
    parser = ContratoParser()
    # Nome do arquivo que você já tem na sua pasta data/docs
    arquivo = "bronze_portal_transparencia_2017_contrato_5733_2017.pdf"
    
    df_final = parser.process_contrato_5733(arquivo)
    
    if df_final is not None:
        print("\n--- AMOSTRA DOS DADOS EXTRAÍDOS ---")
        print(df_final[['item_nro', 'descricao', 'qtd_valor']].head(10))
        
        # Descomente a linha abaixo quando quiser subir pro BigQuery
        # parser.save_to_bigquery(df_final, "stg_portal_contratos")