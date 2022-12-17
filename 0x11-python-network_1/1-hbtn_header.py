#!/usr/bin/python3

from sys import argv
from urllib import request

if __name__ == "__main__":
    """ take url and display X-Reques-Id """
    url = argv[1]
    with request.urlopen(url) \
            as response:
        Id = response.info()('X-Request-Id')
    print(Id)