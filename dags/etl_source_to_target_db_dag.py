from airflow.hooks.base import BaseHook
from airflow.hooks.mysql_hook import MySqlHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from datetime import datetime, timedelta
from airflow import DAG
# from custom import MySqlToPostgreOperator

class PostgresToPostgreOperator(BaseOperator):
    
    @apply_defaults
    def __init__(self,
                 sql=None,
                 target_student=None,
                 identifier=None,
                 source_conn_id='source_db', 
                 postgres_conn_id='postgresql-target-db',
                 *args,
                 **kwargs):
        
        super().__init__(*args, **kwargs)
        self.sql = sql
        self.target_student = target_student
        self.identifier = identifier
        self.source_conn_id = source_conn_id
        self.postgres_conn_id = postgres_conn_id

    def execute(self, context):
        
        
        source = PostgresHook(self.source_conn_id)
        target = PostgresHook(self.postgres_conn_id)
        
        conn = source.get_conn()
        cursor = conn.cursor()
        
        cursor.execute(self.sql)
        
        target_fields = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        
        target.insert_rows(self.target_student,
                           rows,
                           target_fields=target_fields,
                           replace_index=self.identifier,
                           replace=True)
        
        cursor.close()
        conn.close()



dag = DAG(
    dag_id="etl_source_to_target_db_dag",
    start_date=datetime.today() - timedelta(days=1),
    schedule_interval="0 */4 * * *",
    concurrency=100
)

start = PostgresToPostgreOperator(
    task_id=f"start",
    sql="select * from student " ,
    target_student='public.target_student',
    identifier='id',
    dag=dag,
)