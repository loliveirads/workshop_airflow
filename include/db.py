from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


load_dotenv(dotenv_path="env")

# Carregar arquivo .env
if not load_dotenv(dotenv_path=".env"):
    raise FileNotFoundError("Arquivo .env.prod não encontrado ou não pôde ser carregado")

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

if not db_port or not db_port.isdigit():
    raise ValueError(f"DB_PORT não foi carregado corretamente: {db_port}")
print(f"DB_PORT carregado com sucesso: {db_port}")

db_port = int(db_port)  # Converte para inteiro

# Conexão dinâmica com o banco de dados
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()