#!/usr/bin/env python

import subprocess
import logging
import argparse
import requests
from urllib.parse import urlparse

"""Logger initializer"""
logger = logging.getLogger('url_scrapper_application')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

def arguments():
    """This method is used to Parse the arguments to the application"""
    logger.info("Parsing Arguments")
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, required=True)
    parser.add_argument('--http_server', action='store_true')
    arguments = parser.parse_args()
    return arguments

def content(url):
    """This method is used for getting the response of the request and storing it into a file index.html"""
    parsed = urlparse(url)
    if(bool(parsed.netloc) and bool(parsed.scheme)):
        logger.info("Request to URL")
        r = requests.get(url)
        if r.status_code == 200:
            logger.info("Writing to file")
            with open('index.html','w') as file:
                file.write(r.text)

if __name__ == '__main__':
    """This is the main function for the application"""
    arguments = arguments()
    content(arguments.url)
    if arguments.http_server:
        logger.info("Starting HTTP server")
        process = subprocess.Popen(['python', '-m', 'http.server', '8000', '-d','./'],shell=False)

        """Terminate the server if any input is recieved"""
        val = input() 
        if val:
            logger.info("Terminating Server")
            process.terminate();

