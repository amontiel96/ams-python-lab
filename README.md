# ams-lambda-python
***
## Description:
An AWS lambda function developed in Python. It shows how to create, configure and deploy the function in the AWS cloud as an API endpoint in ApiGateway.
***
## Run Locally
To run the commands you must be on the root of the repository


### Local execution
🚨 NOTE: You must be having installed python3.7 or higher in your local machine
### LINUX:
``python -m venv venv``

``./venv/bin/activate``

``pip install --no-cache-dir -r requirements.txt``


### WINDOWS:
``python -m venv venv``

``.\venv\Scripts\activate``

``pip install --no-cache-dir -r requirements.txt``


## For unittest
To run the unittest and coverage run the next commands:

``coverage run -m unittest discover``

`` coverage html -d coverage_html``

after run the last command you can find a folder with the name "coverage html" open the index.html file inside and filter by "app/" for show only the app coverage

