from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
    'owner': 'ayaz',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}


with DAG(
    dag_id='ayaz_first_dag_1',
    default_args=default_args,
    start_date=datetime(2022, 5, 15)
) as dag:
    task1 = PostgresOperator(
        task_id='select_postgres_table',
        postgres_conn_id='postgresql-target-db',
        sql="""
            select * from target_student limit 1
        """
    )
    task1