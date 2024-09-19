from datetime import datetime, timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow.models.dag import DAG
from airflow.decorators import task

from src.api_params import URL, URL_PARAMS, AUTH, CSV_HEADER, CSV_FILENAME
from src.extract_data import get_data, save_to_csv

# Operators; we need this to operate!
with DAG(
    dag_id="etl_dag",
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function, # or list of functions
        # 'on_success_callback': some_other_function, # or list of functions
        # 'on_retry_callback': another_function, # or list of functions
        # 'sla_miss_callback': yet_another_function, # or list of functions
        # 'on_skipped_callback': another_function, #or list of functions
        # 'trigger_rule': 'all_success'
    },
    description="A simple tutorial DAG",
    schedule=timedelta(days=1),
    start_date=datetime(2024, 9, 1),
    catchup=False,
    tags=["example"],
) as dag:
    @task(task_id="extract")
    def extract():
        """ Get data through API request, save it to CSV"""
        data = get_data(URL, URL_PARAMS, AUTH)
        file_path = save_to_csv(CSV_HEADER, CSV_FILENAME, data)

        return file_path

    @task(task_id="transform")
    def transform():

        return "Transformed"

    @task(task_id="load")
    def transform():
        return "Loaded to DB"

