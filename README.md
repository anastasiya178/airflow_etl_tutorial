# Airflow Tutorial

## Purpose

## Description

### Airflow installation
Airflow installation:
https://airflow.apache.org/docs/apache-airflow/stable/start.html


Recommendations:
- create a venv before proceeding with airflow installation
- if airflow was already installed earlier, it might make sense to reinstall
it using: 
```
pip uninstall apache-airflow
```
- create dags under Airflow home (not in a separate python project)

### Sample DAG

I used a very first DAG sample from here:
https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html

I renamed it to "jay_tutorial".


Notes: 
- I had hard time finding my DAG on the web UI. 
The DAG name is specified here as "tutorial": 
``` 
with DAG(
    #### this is DAG name which is positional argument called dag_id
    "tutorial",
    default_args={...
  
) as dag:

   ....
```
- If you are able to see your DAG on the web, then once you make any changes, they
will be automatically displayed in the UI

### Operators
BashOperator
BasOperator output can be see in the logs. 
In that case it's Tuesday

![img.png](img.png)

HTTPOperator

The code examples use the http_default connection which means the requests are sent against httpbin site to perform basic HTTP operations.
To edit default connection, go to Airflow UI/Admin/Connections and search for http_default.

Options: 
https://medium.com/towards-data-engineering/airflow-3-ways-to-call-a-rest-api-78181fca6fe8

### Other notes
- remove examples: make sure load_examples = False is set in airflow.cfg.
- HTTP workaround for MAC: 
```
# fix for mac machines
import os
from _scproxy import _get_proxy_settings

_get_proxy_settings()
os.environ['NO_PROXY'] = '*'
```

## TODO
- try different operators (4 examples): Bash, Http, Python...

###NOTES: 
- restart web server (eg when changing configs: 
``` airflow webserver -p 8080 -D ```

#### Change config
``` 
# if you wish not to load example dags on the UI 
load_examples = False

# if you wish to access config throgh UI here: http://localhost:8080/configuration
expose_config = True
#

```
- having 2 airflow configs - confusion


### Understanding Airflow commands

``` 
airflow standalone
# initializes the database, creates a user, and starts all components (all-in-one)
# saves password to standalone_admin_password.txt in your airflow home

# alternative to standalone if you want to run the individual parts of Airflow manually
airflow db migrate

airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org

airflow webserver --port 8080
airflow scheduler


```

### XCOM
Inspired by: 
https://marclamberti.com/blog/airflow-xcom/

Notice the parameter ti (task instance). 
Once we access the task instance object, we can call xcom_push.



### Other things: 
- debug functions