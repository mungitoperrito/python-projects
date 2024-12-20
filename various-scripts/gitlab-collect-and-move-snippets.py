# Utility to collect snippet files before deleting a user
#

import requests
import json
import os
import sys

# Setup: Assumes configuration along the lines of:
#   https://python-gitlab.readthedocs.io/en/stable/cli.html
#   for the GLAT access token environment variable
PRIVATE_TOKEN = os.environ['GLAT']
GIT_SERVER = 'https://git.grammatech.com/'
API_BASE = 'api/v4/'
GIT_API = GIT_SERVER + API_BASE
GIT_SNIPPETS = GIT_API + 'snippets/'
GIT_PROJECTS = GIT_API + 'projects/'


def print_request_info(req):
    print(f"url: {req.request}")
    print(f"status code: {req.status_code}")


def get_data(url, parameters=""):
    GET_HEADERS = {'PRIVATE-TOKEN': PRIVATE_TOKEN}

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


def post_data(url, parameters='', data=''):
    POST_HEADERS = {'Content-Type': 'application/json',
                    'PRIVATE-TOKEN': PRIVATE_TOKEN}
    # TODO


def get_snippets():
    url = GIT_SNIPPETS
    #url = "FAIL"

    page_num = 1
    PARAMS = {'per_page': '5', 'page': page_num}
    response = get_data(url, PARAMS)
    snippets_json = []
    current_page_data = json.loads(response.text)
    current_page_headers = response.headers
    snippets_json.extend(current_page_data)

    # gitlab pages requests, get all snippets
    while current_page_headers['X-Next-Page']:
        page_num += 1
        PARAMS = {'per_page': '5', 'page': page_num}
        response = get_data(url, PARAMS)
        current_page_data = json.loads(response.text)
        current_page_headers = response.headers
        snippets_json.extend(current_page_data)

    return snippets_json

def get_a_snippet(sid):
    snippet_return = []

    # Get snippet metadata  --   returns a string of json
    url = GIT_SNIPPETS + str(sid)
    response = get_data(url)
    response_json = json.loads(response.text)
    if response_json['project_id'] != 'null':
        current_project_id = response_json['project_id']
    snippet_return.append(response_json)

    # Get snippet body  --   returns a string
    url = GIT_SNIPPETS + str(sid) + '/raw'
    response = get_data(url)
    snippet_return.append(response.text)

    # Get snippet discussions  --   returns a list of json
    if current_project_id:
        url = GIT_PROJECTS \
              + str(current_project_id)  \
              + '/snippets/' \
              + str(sid) + '/discussions/'
        response = get_data(url)
        snippet_return.append(json.loads(response.text))

    return snippet_return


def post_personal_snippet(snip):
    # Project URL https://git.grammatech.com/retired-users/saved-snippets/
    pass


class snippet():
    def __init__(self):
        self.title = ""
        self.file_name = ""
        self.id = ""
        self.visibility = ""
        self.content = ""


def print_to_file(snpt):
    output = ""
    with open('collected-snippets.txt', 'a') as snippets_file:
        for i in snpt:
            print(type(i))
        #snippets_file.write(snpt)


def get_username(uid):
    pass


##########
## MAIN ##
##########
snippets = get_snippets()

count = 0
for snippet in snippets:
    count += 1
    snpt = get_a_snippet(snippet['id'])
    print_to_file(snpt)
    print(f"SNIP: {snpt}\n\n")
    sys.exit(3)

print(f"COUNT: {count}")
# print("EOF")