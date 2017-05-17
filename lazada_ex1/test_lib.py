###################################################################################
# Test library
# The file provides the user libraries which are used for implementing Test cases
# __author__ = 'Hoa Tran'
###################################################################################

import requests
import random
import logging
import datetime

#####################################################################
# Name:     issue_random
#
# Purpose:  randoms an integer value base on the providing range
# Params:
#           +min : minimum of range
#           +max : maximum of range
# Return:   a random integer value
######################################################################
def issue_random(min, max):
    return random.randint(min,max)


#####################################################################
# Name:     get_data
#
# Purpose:  to issue '.get' method of 'requests' module
# Params:
#           +url : url to retrieve the REST api
# Return:   an request object
######################################################################
def get_data(url):
    return requests.get(url)


#####################################################################
# Name:     post_data
#
# Purpose:  to issue '.post' method of 'requests' module
# Params:
#           +url : url to retrieve the REST api
# Return:   an request object
######################################################################
def post_data(url, payload):
    return requests.post(url, data=payload)


#####################################################################
# Name:     issue_log_file
#
# Purpose:  to create the log file( located in the package director)
# Params:    N/A
#
# Return:   N/A
######################################################################
def issue_log_file():
    LOG_FILENAME = 'lazada_ex1.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
    logging.info('===========Date: '+str(datetime.datetime.now()))


#####################################################################
# Name:     verify_element
#
# Purpose:  to verify if the data contains all JSON elements
# Params:
#           +data:  JSON data
#           +list_element:  list of element to be verified
#
# Return:
#           +TRue: data contains all JSON elements
#           +False: data does not contain all JSON element
######################################################################
def verify_element(data, list_element):
    for i in list_element:
        if not data[i]:
            return False
    return True