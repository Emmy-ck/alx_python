#!/usr/bin/python3
"""
Python script sending request to given URL and display value of X-Request-Id
"""
import requests
import sys

if __name__ == "__main__":
    from urllib import request
    from sys import argv
    if argv[1]:
        with request.urlopen(argv[1]) as response:
            print(response.getheader('X-Request-Id'))