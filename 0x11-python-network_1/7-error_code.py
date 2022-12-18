#!/usr/bin/python3
""" this module take URL and send request URL"""
import requests
from sys import argv

if __name__ == "__main__":
    resp = requests.get(argv[1])
    code = resp.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(resp.text)