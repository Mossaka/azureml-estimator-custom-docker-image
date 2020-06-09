# Azureml Estimator Custom Docker Image

## Build

1. setup azure workspace from this [tutorial](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace)
2. download `config.json` and place it in the project's directory
3. setup SQLDW from this [tutorial](https://docs.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/create-data-warehouse-portal)
4. get the connection string for SQLDW and modify `test.py`. Notice we are use **ODBC Driver 17** 
5. create a Dockerfile (tutorial below)

## Dockerfile

you should download the base docker image from this [repo](https://msdata.visualstudio.com/Vienna/_git/AzureMlCli). Navigate to `base_images/docker/public/base-gpu/*` to use any one of the *Dockerfile*. Remember you need the mysobdcsql installed in order for it to work. I am workingo this task right now. Once I finished, it should contain it by default.

