from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

current_dir = os.path.dirname(__file__)
project_path = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_path)

from scripts.etl import main as etl_main

with DAG(
    dag_id="orders_etl_pipeline",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    run_etl = PythonOperator(
        task_id="run_etl",
        python_callable=etl_main
    )
