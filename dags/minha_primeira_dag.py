from airflow.decorators import dag, task
from datetime import datetime
from time import sleep

@dag(
    dag_id='minha_primeira_dag',    # Nome da DAG
    description='Pipeline de exemplo',
    schedule_interval="* * * * *",  # Intervalo de execução (a cada minuto)
    start_date=datetime(2023, 1, 1),
    catchup=False,
)
def pipeline():

    # Funções de atividade
    @task()
    def primeira_atividade():
        print("Minha primeira atividade! - Hello World")
        sleep(2)

    @task()
    def segunda_atividade():
        print("Minha segunda atividade! - Hello World")
        sleep(2)

    @task()
    def terceira_atividade():
        print("Minha terceira atividade! - Hello World")
        sleep(2)

    @task()
    def quarta_atividade():
        print("Pipeline finalizada com sucesso! - Hello World")

    # Chamando as tarefas e definindo a sequência
    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    t1 >> t2 >> t3 >> t4


# Instancia a DAG no Airflow
pipeline()
