# Small vibe-coding `hello world` experiment

This experiment uses [Claude AI](https://claude.ai/new) to create a small app. The process 
unfolds over several steps. 

## ENVIRONMENT SETUP

```bash
cd temp                                        # Go to an empty workspace
pyenv install 3.13.7                           # Install recent python
pyenv versions                                 # Check version list
pyenv virtualenv 3.13.7 hello_flask_app        # create virtual environment
$(pyenv which python3) --version               # Check current running version
                                               # System version: Python 3.10.12
pyenv local hello_flask_app                    # Activate virtual environment
$(pyenv which python3) --version               # Check current running version
                                               # virtual env version: Python 3.13.7
mkdir hello_flask                              # Create project directory
cd !$                                          # Switch directories  
```

## DEPENDENCIES

**CAUTION** Check `pip` version first. If pyenv isn't first in `PATH`, the wrong `pip` will run.

```bash
pip install flask
```

## PROMPTS

1. Create the app skeleton.

```
I want to learn about vibe coding. How can I code a hello world web app in python? 

Use python
Use flask
```

1. Write some unit tests

```
Add a unit test for the '/hello/<name>' endpoint 
```

NOTE: Claude added several unit tests to the source file

1. Refactor the source file

```
break the tests out into their own file
```

1. Use `cURL` to check the API endpoints

```
what is the curl command to test the name endpoint?

show the http response code
```

## `cURL` commands and outputs

* Response and status: `cURL -w`

```bash
curl -w "\nHTTP Status: %{http_code}\n" http://localhost:5000/hello/Alice
<h1>Hello, Alice!</h1><p>Nice to meet you!</p>
HTTP Status: 200
```

* Full header: `cURL -i`

```bash
curl -i http://localhost:5000/hello/Alice
HTTP/1.1 200 OK
Server: Werkzeug/3.1.3 Python/3.13.7
Date: Mon, 15 Sep 2025 03:00:05 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 46
Connection: close

<h1>Hello, Alice!</h1><p>Nice to meet you!</p>nonch ~ >
```

* Status only: `cURL -s`
```bash
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:5000/hello/Alice
200
```

NOTE: This format string needed a new-line character.
