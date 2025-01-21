from airflow.decorators import dag
from pendulum import datetime
from include.custom_operators.postgres_to_duckdb_operator import PostgresToDuckDBOperator

# Definir conexões
CONNECTION_DUCKDB = "duckdb_workshop_airflow	"  # ID da conexão do DuckDB
CONNECTION_POSTGRESDB = "workshop_airflow"  # ID da conexão do PostgreSQL

@dag(
    start_date=datetime(2024, 3, 23),  # Data de início da DAG
    schedule=None,  # Sem agendamento recorrente
    catchup=False  # Não executar retroativamente
)
def pipeline_de_migracao_postgres_to_duckdb():
    PostgresToDuckDBOperator(
        task_id="postgres_to_duckdb",
        postgres_schema="public",  # Esquema do PostgreSQL
        postgres_table_name="pokemons",  # Nome da tabela no PostgreSQL
        duckdb_conn_id=CONNECTION_DUCKDB,  # ID da conexão DuckDB
        postgres_conn_id=CONNECTION_POSTGRESDB  # ID da conexão PostgreSQL
    )

# Instanciar a DAG
pipeline_de_migracao_postgres_to_duckdb()
