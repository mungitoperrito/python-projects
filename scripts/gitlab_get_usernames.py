# Get usernames from gitlab, add them to a dictionary for later use

# TODO
#  -- fix paging

import requests
import json
import os
import sys
from collections import defaultdict

# Setup: Assumes configuration along the lines of:
#   https://python-gitlab.readthedocs.io/en/stable/cli.html
#   for the GLAT access token environment variable
PRIVATE_TOKEN = os.environ['GLAT']
GIT_SERVER = 'https://git.grammatech.com/'
API_BASE = 'api/v4/'
GIT_API = GIT_SERVER + API_BASE


def print_request_info(req):
    print(f"url: {req.request}")
    print(f"status code: {req.status_code}")


def get_usernames():
    GET_HEADERS = {'PRIVATE-TOKEN': PRIVATE_TOKEN}
    url = GIT_API + 'users'
    parameters = ''
    try:
        response = requests.get(url, headers=GET_HEADERS, params=parameters)
        if response.status_code != 200:
            print_request_info(response)
            sys.exit(1)
    except Exception as e:
        print(e)
        print_request_info(response)
        sys.exit(2)

    return response


def create_dictionary(raw_list):
    user_info = defaultdict(list)
    json_list = json.loads(raw_list.text)
    for entry in json_list:
        # These are only a few of the available user info fields
        user_info[entry['id']] = [
              entry['name'],
              entry['username'],
              entry['email'],
              entry['created_at'],
              entry['last_sign_in_at'],
              entry['last_activity_on'],
              entry['current_sign_in_at'],
              entry['is_admin']
         ]

    return user_info


############
##  MAIN  ##
############
raw_name_list = get_usernames()
user_name_list = create_dictionary(raw_name_list)
for n in user_name_list: print(n)