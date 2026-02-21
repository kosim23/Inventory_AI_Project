from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Скриптлар папкасини йўлга қўшиш
sys.path.append('/opt/airflow')

from scripts.model_inference import run_inference

default_args = {
    'owner': 'inventory_manager',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
}

dag = DAG(
    'daily_inventory_automation',
    default_args=default_args,
    description='Ҳар кунлик башорат ва заҳира ҳисоби',
    schedule_interval='@daily',
    catchup=False
)

run_model_task = PythonOperator(
    task_id='run_demand_forecast',
    python_callable=run_inference,
    dag=dag,
)