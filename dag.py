from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def print_hello():
      print('hello'*100)


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG
dag = DAG(
    dag_id = "airflow",
    default_args=default_args,
    description='A simple DAG with PythonOperator',
    schedule_interval=timedelta(days=1), 
)

start_task = DummyOperator(task_id='start_task', dag=dag)

print_hello = PythonOperator(task_id='print_hello', 
                             python_callable= print_hello,
                             dag=dag)

start_task >> print_hello
