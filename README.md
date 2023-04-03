# ML Ops project 2

## Section 1 - Project Overview

The purpose of this project is to demonstrate the capabilities of Azure ML Ops thorugh the following exercises:

* Creating and deploying a model utilzing AutoML
* Consuming REST API endpoints
* Pipeline automation for re/training the bank marketing model

Through these capabilities we learn how to apply DevOps principles to Machine Learning projects. Many of the same principles including automation, troubleshooting, and code management are similar in MLOps as traditional DevOps.

This project specifically works with the Bank Marketing dataset for purposes of training a model, selecting the best one, deploying it as a REST API endpoint, consuming the API, and automating the flow through pipeline automation.

## Section 2 - Architectural Diagram

The following diagram is adapted from the Azure Reference Architecture, [ML Ops for Python](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/ai/mlops-python). It has been simplified for purposes of illustrating the following key points (labeled on the diagram):

1. MLOps Engineer creating the pipeline build
2. REST Endpoint consumer
3. MLOps Pipeline trigger for retraining

![pipeline-arch](images/pipeline-arch.png)

## Section 3 - Future work to improve project

Areas to investigate / improve upon in future work:

* Model performance
  * Apply data science techniques to the data set for additional feature engineering
  * Investigate whether there are additional datasets which could be combined with this marketing data to provide additional parameters to the models
  * Try utilizing different metric scores for model performance
* Pipeline capabilities
  * Automate more of the process including the create of the dataset, monitoring of any data drift, health checks on the endpoint and other monitoring abilities
  * Assuming this endpoing is part of a larger project/platform, integrate the MLOps steps into the build pipeline for the encompassing project (integrate the DevOps and MLOps)

## Section 4 - Screenshots of main steps in project

The following sections contain the required screenshots as requested by the project syllabus.

### Setup security

`az extension add -n azure-cli-ml`
`az ad sp create-for-rbac --sdk-auth --name ml-auth`

Since I am using an account my company manages, I am also not allowed to create a service principal. See following screenshot.

![as](./images/sp-insufficent-priv.png)

### Show the dataset as available

![data](./images/data-set-avail.png)

### Show the expirement completed

![exp](./images/complete-experiment.png)

### Show the best model

Model rank among the others tried.

![best-1](./images/best-model.png)

Model specific metrics.

![best-2](./images/best-model-2.png)

### Show application insights enabled

![app-insights](./images/app-insights-enabled.png)

### Show the logs output

![logs-output](./images/logs-output.png)

### Show the Swagger docs

![swagger](./images/swagger-app.png)

### Results of invoking endpoint

![endpoint](./images/endpoint-results.png)

### Optional -- benchmark results

![benchmark](./images/ab-results.png)

### Pipeline created

![pipeline](./images/pipeline-created.png)

### Pipeline endpoint

![endpoint](./images/pipeline-endpoint.png)

### Bank data AutoML

![bank](./images/bank-data-automl.png)

### Published Pipeline overview - Active endpoint

![endpoint](./images/published-pipeline-rest.png)

### Run Details Widget

![rundetails](./images/run-details.png)

### ML Studio scheduled run

![scheduled](./images/scheduled-run.png)

## Section 5 - Screencast of working ML application

*insert link here*
