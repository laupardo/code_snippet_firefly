#!/usr/bin/env python
from datetime import datetime
import requests
from csv import DictReader


def csv_to_dict(file_path):
    with open(file_path, 'r') as f:
        dict_reader = DictReader(f)
        list_of_dict = list(dict_reader)
    return list_of_dict


def convert_date_format(initial_date):
    # Convert original timestamp to a datetime object
    dt_object = datetime.strptime(initial_date, "some format")
    # Format the datetime object to new format
    formatted_date = dt_object.strftime("new format")
    return formatted_date


def create_transaction(date, type, amount, description, base_url):
    # this token should be managed as an env variables
    headers = {'Authorization': 'Bearer ACCESS_TOKEN', 'Content-Type': 'application/json'}
    url = base_url + '/v1/transactions'
    payload = {
        'description': description,
        'amount': amount,
        'date': convert_date_format(date),
        'type': type
    }
    response = requests.post(url=url, json=payload, headers=headers)
    if response.status_code != 200:
        #could also send to log when error
        print(f'Error importing entry: {payload}')


if __name__ == "__main__":
    # initial data
    base_url = "https://demo.firefly-iii.org/api"
    file_path = 'data.csv'
    finances_list = csv_to_dict(file_path)
    for element in finances_list:
        create_transaction(element['transaction_date'], element['transaction_type'], element['transaction_amout'],
                           element['trabsaction_description'], base_url)
