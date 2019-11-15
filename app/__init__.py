# creates application object as instance of class Flask imported from the flask package
from flask import Flask
from config import Config


# __name__ is python predefined variable which is set to the name of the module where its used
app = Flask(__name__)
app.config.from_object(Config)

# imports the routes module
from app import routes