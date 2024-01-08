from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def my_logging_task():
    # Your custom logging logic here
    print("Testing remote logging...")

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 8),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'remote_logging_test',
    default_args=default_args,
    description='A DAG to test remote logging in Airflow deployed on Kubernetes via Helm',
    schedule_interval=timedelta(days=1),
)

# Define the tasks
start_task = DummyOperator(
    task_id='start_task',
    dag=dag,
)

logging_task = PythonOperator(
    task_id='logging_task',
    python_callable=my_logging_task,
    dag=dag,
)

end_task = DummyOperator(
    task_id='end_task',
    dag=dag,
)

# Define the task dependencies
start_task >> logging_task >> end_task