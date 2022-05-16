# task_glints
The following repo is a simple airflow DAG that does move data from on postgres data base to another. All the services are defined in the docker compose.yaml
-----------------------------------------------------------

Steps to use this repo:<br />
  1: clone this repo on your machine<br />
  2: cd into the airflow-docker<br />
  3: Use this command to create environment variable for airflow <br />
  ```echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env```<br />
