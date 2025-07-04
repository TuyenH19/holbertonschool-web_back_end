# User authentication service
## Resources
* Flask documentation (https://flask.palletsprojects.com/en/stable/quickstart/)
* Requests module (https://requests.kennethreitz.org/en/latest/user/quickstart/)
* HTTP status codes (https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

## Learning Objectives
* How to declare API routes in a Flask app
* How to get and set cookies
* How to retrieve request form data
* How to return various HTTP status codes

## Requirements
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.5)
You should use SQLAlchemy
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
All your functions should be type annotated
The flask app should only interact with Auth and never with DB directly.
Only public methods of Auth and DB should be used outside these classes

## Setup
You will need to install bcrypt
pip3 install bcrypt
