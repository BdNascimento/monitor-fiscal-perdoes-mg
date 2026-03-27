import os
from pathlib import Path
import pdfplumber
import pandas as pd
from google.cloud import bigquery
from google.cloud import storage

class BaseProcessor:
    def __init__(self):
        # 1. CAMINHO ABSOLUTO TOTAL (Baseado no seu Log de erro)
        # Vamos usar o caminho que o Windows entende, sem o símbolo ~
        cred_path = Path(r"D:\Projetos\Projeto de Dados Perdões\monitor-fiscal-perdoes-mg\scripts\utils\gcp-credentials.json")
        
        print(f"🔍 [DEBUG] Tentando acessar caminho fixo: {cred_path}")

        if not cred_path.exists():
            # Tenta uma alternativa caso você tenha renomeado a pasta
            current_dir = Path(__file__).resolve().parent
            cred_path = current_dir.parent / "utils" / "gcp-credentials.json"
            print(f"🔍 [DEBUG] Tentativa 2 (relativa): {cred_path}")

        if not cred_path.exists():
            raise FileNotFoundError(f"❌ Não encontrei o JSON! Verifique se o arquivo está na pasta scripts/utils/")

        # 2. CONFIGURA AS CREDENCIAIS
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(cred_path)
        
        try:
            self.bq_client = bigquery.Client()
            self.storage_client = storage.Client()
            self.bucket_name = "perdoes-transparencia-raw"
            print("🚀 [GCP] Conexão estabelecida com sucesso!")
        except Exception as e:
            print(f"💥 [GCP] Falha na conexão: {e}")

    def open_pdf(self, pdf_path):
        return pdfplumber.open(pdf_path)

    def save_to_bigquery(self, df, table_id):
        # (seu código de save permanece igual)
        pass