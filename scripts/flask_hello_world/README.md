### ENVIRONMENT SETUP

cd temp                                        # Go to an empty workspace
pyenv install 3.13.7                           # Install recent python
pyenv versions                                 # Check version list
pyenv virtualenv 3.13.7 hello_flask_app        # create virtual environment
$(pyenv which python3) --version               # Check current running version
  Python 3.10.12
pyenv local hello_flask_app                    # Activate virtual environment
$(pyenv which python3) --version               # Check current running version
  Python 3.13.7

mkdir hello_flask                              # Create project directory
cd !$                                          # Switch directories  
  
### DEPENDENCIES

pip install flask


### PROMPTS
I want to learn about vibe coding. How can I code a hello world web app in python? 

Use python
Use flask

# 

Add a unit test for the '/hello/<name>' endpoint 

(NOTE: Added several unit tests)

# 

break the tests out into their own file


###############################
### Check outputs with cURL ###
###############################

# Prompt
what is the curl command to test the name endpoint?

show the http response code

---

curl -w "\nHTTP Status: %{http_code}\n" http://localhost:5000/hello/Alice
<h1>Hello, Alice!</h1><p>Nice to meet you!</p>
HTTP Status: 200


curl -i http://localhost:5000/hello/Alice
HTTP/1.1 200 OK
Server: Werkzeug/3.1.3 Python/3.13.7
Date: Mon, 15 Sep 2025 03:00:05 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 46
Connection: close

<h1>Hello, Alice!</h1><p>Nice to meet you!</p>nonch ~ >


curl -s -o /dev/null -w "%{http_code}\n" http://localhost:5000/hello/Alice
200
