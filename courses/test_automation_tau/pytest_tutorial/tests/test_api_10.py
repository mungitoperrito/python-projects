# ch10
# https://testautomationu.applitools.com/pytest-tutorial/chapter10.html

# For path inclusion, use: c> python -m pytest

# # DEBUG
# import sys
# for p in sys.path:
#   print(p)

import pytest
import requests

@pytest.mark.duckduckgo
@pytest.mark.api
def test_duck_duck_go_inst_ans_api():
    # Setup
    url = 'https://api.duckduckgo.com/?q=python+programming&format=json'

    # Call
    response = requests.get(url)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert 'Python' in body['AbstractText']