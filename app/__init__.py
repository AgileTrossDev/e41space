from flask import Flask

app = Flask(__name__)

# Import here to avoid circular dependancies
from app import routes
