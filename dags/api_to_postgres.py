from airflow.decorators import task, dag
from include.controller import gerar_numero_aleatorio, fetch_pokemon_data, add_pokemon_to_db
from datetime import datetime

@dag(
    dag_id="api_postgres_pipeline",
    description="Pipeline para manipulação de dados via API e PostgreSQL",
    schedule_interval="*/5 * * * *",  # Executa a cada 5 minutos
    start_date=datetime(2025, 1, 17),  # Substitua pela data de hoje
    catchup=False
)
def api_postgres():
    # Tarefa 1: Gera um número aleatório
    @task(task_id='gerar_numero_aleatorio')
    def task_gerar_numero_aleatorio():
        return gerar_numero_aleatorio()

    # Tarefa 2: Busca dados do Pokémon
    @task(task_id='fetch_pokemon_data')
    def task_fetch_pokemon_data(numero_aleatorio):
        return fetch_pokemon_data(numero_aleatorio)

    # Tarefa 3: Adiciona os dados ao banco
    @task(task_id='add_pokemon_to_db')
    def task_add_pokemon_to_db(pokemon_data):
        return add_pokemon_to_db(pokemon_data)

    # Orquestração das tarefas
    t1 = task_gerar_numero_aleatorio()
    t2 = task_fetch_pokemon_data(t1)
    t3 = task_add_pokemon_to_db(t2)

    # Define a sequência
    t1 >> t2 >> t3


# Instancia a DAG
api_postgres()
