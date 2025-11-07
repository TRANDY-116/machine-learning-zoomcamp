#!/usr/bin/env python
# coding: utf-8

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get host from .env file with fallback
host = os.getenv('host', 'http://localhost:9696')
url = f'{host}/predict'


customer_ID = "Test User"
customer = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": 29.85
}

response = requests.post(url, json=customer).json()

print(response)


if response['churn'] == True:
    print('sending promo email to %s' % (customer_ID))
else:
    print('no email sent')

