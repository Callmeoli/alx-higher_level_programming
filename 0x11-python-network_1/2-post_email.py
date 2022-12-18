#!/usr/bin/python3
""" take url and display  of X-Reques-Id """
import sys
from urllib import request, parse

url = sys.argv[1]
values = {'email': sys.argv[2]}
data = parse.urlencode(values)
data = data.encode('ascii')
req = request.Request(url, data)
if __name__ == "__main__":
    """ take url and display X-Reques-Id """
    with request.urlopen(req) \
            as response:
        page = response.read()
    print(page)
