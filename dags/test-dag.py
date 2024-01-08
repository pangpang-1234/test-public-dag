from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago


def print_hello():
    print('hello'*100)

default_args={
    'owner':'Pang',
    'retries':5,
    'retry_delay':timedelta(minutes=10)
}

with DAG(   
    dag_id = 'test-airflow',
    default_args=default_args,
    description = 'airflow on kube',
    start_date=days_ago(1), # Daily run
    schedule_interval='@once'
    ) as dag:

    start_task = DummyOperator(task_id='start_task', dag=dag)

    print_hello = PythonOperator(task_id='print_hello', 
                             python_callable= print_hello,
                             provide_context=True,
                             dag=dag)

start_task >> print_hello
