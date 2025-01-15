from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloWorld():
    print("Hello World")

with DAG(
    dag_id="hello_world_dag",
    start_date=datetime(2025, 1, 15),
    schedule_interval="* * * * *",
    catchup=False
) as dag:

    task = PythonOperator(
        task_id="print_hello_world",
        python_callable=helloWorld
    )
