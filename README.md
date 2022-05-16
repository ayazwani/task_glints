# task_glints
The following repo is a simple airflow DAG that does move data from on postgres data base to another. All the services are defined in the docker compose.yaml
-----------------------------------------------------------

Steps to use this repo:<br />
  1: clone this repo on your machine<br />
  2: cd into the airflow-docker<br />
  3: open the terminal in the same working directory and use this command to create environment variable for airflow <br />
  ```echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env```<br />
  4: use this command to init airflow setup <br /> 
   ```docker-compose up airflow-init``` <br />
  5: the use ```docker-compose up -d ``` to up all of your services.<br />
  6: you can check if services are running or not using ```docker ps``` <br />
  7: Go to your browser and type ```localhost:5884``` , you will see a login screen to airflow type <br />
  ``` username = airflow and password = airflow ``` to login in. <br />
  8: Once logged on go to the admin ----> connections ----> and add a new connection there for source DB <br />
      ```connection_id = source_db 
         host = db1 
         schema = source
         login = source
         password = source 
         port = 5432 
       ```
  9: Like wise same for target db <br />
     ```connection_id = postgresql-target-db 
         host = db2 
         schema = target 
         login = target 
         password = target 
         port = 5432 
       ```
   10: After establishing the connection go to Dags and search for  <br /> ```etl_source_to_target_db_dag``` <br />
       dag and trigger it manually. <br />
   11 : it should then be able to move data from source db to target db.
   12 : which you could then verify using ``` docker exec -it docker_container_hash/name /bin/bash``` <br /> ```psql -U target -w target``` <br />  ```select * from target_student``` <br /> and see the requred data from source db
   
   
