""" Get poverty data from the URL resource"""
import csv
import logging
import requests
from requests.auth import HTTPBasicAuth
from src.api_params import CSV_HEADER, CSV_FILENAME, URL, URL_PARAMS, AUTH

# fix of HTTP calls issue for mac machines
import os
from _scproxy import _get_proxy_settings

_get_proxy_settings()
os.environ['NO_PROXY'] = '*'


logging.basicConfig(level=logging.INFO)


def get_data(url: str, params: dict, auth: requests.auth.HTTPBasicAuth) -> list:
    """
    Request data using GET method, get response.
    Returns the json-encoded content of a response.
    """
    logging.info("Initate GET request")
    response = requests.request("GET", url, params=params, auth=auth, timeout=5)
    response.raise_for_status()
    json_data = response.json()
    logging.info("JSON data received")
    # remove extra data when returning json
    logging.info(json_data)
    return json_data[1][0:3]


def save_to_csv(header: list, csv_filename: str, json_data: list) -> str:
    """Save data to CSV file"""
    logging.info("Save to CSV")
    with open(csv_filename, "w", encoding="UTF8", newline="") as file:
        writer = csv.writer(file)
        # write CSV header
        writer.writerow(header)
        # write a row
        writer.writerow(json_data)
        # define file path
        file_path = os.getcwd()+"/"+csv_filename
        logging.info(f"Data written to {file_path}")
        return file_path


if __name__ == "__main__":
    # get poverty data
    data = get_data(URL, URL_PARAMS, AUTH)

    # save data to CSV
    save_to_csv(CSV_HEADER, CSV_FILENAME, data)