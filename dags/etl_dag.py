import pendulum
from airflow.decorators import dag, task

from src.api_params import URL, URL_PARAMS, AUTH, CSV_HEADER, CSV_FILENAME
from src.extract_data import get_data, save_to_csv
from src.transform_data import transform_csv


@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def tutorial_taskflow_api():
    @task(task_id="extract")
    def extract():
        """ Get data through API request, save it to CSV"""
        data = get_data(URL, URL_PARAMS, AUTH)
        file_path = save_to_csv(CSV_HEADER, CSV_FILENAME, data)

        return file_path

    @task(task_id="transform")
    def transform(fp):
        """
        Read file from CSV and apply transformations.
        """
        transform_csv(fp)
        return "Transformed"

    @task(task_id="load")
    def load():
        """
        Load data to DB.
        """
        return "Loaded to DB"

    # define task dependencies
    data = extract()
    transformed_data = transform(data)
    transformed_data >> load()

    # TODO: manage dependencies https://www.astronomer.io/docs/learn/managing-dependencies


tutorial_taskflow_api()
