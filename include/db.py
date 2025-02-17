from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path="/usr/local/airflow/.env")

# Carregar arquivo .env
if not load_dotenv(dotenv_path=".env"):
    raise FileNotFoundError("DEURUIM .env não encontrado ou não pôde ser carregado")

# Variáveis de conexão
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

if not db_port or not db_port.isdigit():
    raise ValueError(f"DB_PORT não foi carregado corretamente: {db_port}")
db_port = int(db_port)  # Converte para inteiro

# Conexão dinâmica com o banco de dados
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL)

# Sessão e Base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Testando a conexão com o banco
try:
    with engine.connect() as connection:
        print("Conexão com o banco de dados foi bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
