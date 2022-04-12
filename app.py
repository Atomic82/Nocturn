# main components of our app 

from flask import Flask
from myapp import app #importing from  __init__.py

# app = Flask(__name__, static_folder="/static/css/main.css")

if __name__ == '__main__':
    print('app is running')
    app.run(debug=True)