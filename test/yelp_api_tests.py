#!/usr/bin/env python3

import sys
import requests
import json
import urllib

# Put the API Key in the request header as "Authorization: Bearer <YOUR API KEY>"

api_host = 'https://api.yelp.com'
search_path = '/v3/business/search'
api_key = 'cXHwuii2RlVnEI1DUfLX1IWjaib5tKyQojHInSZa4Ub6EyETmsSp8q5y5h8z1QMu9046F88vTe71XWbMpiG1sb14auCq_fjHlXRUkMaUpmHqThn3TPmiIwiCTpDWWnYx'

default_location = 'San Francisco, CA'

header = {
    'Authorization': 'Bearer {}'.format(api_key)
}



response = requests.request('GET', url, headers=header, param=url_params)
