#!/usr/bin/python3
""" this module fetch alx-intranet status """

from urllib import request

if __name__ == "__main__":
    """ this code will get the status of link """
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') \
            as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))