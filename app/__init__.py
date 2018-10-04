from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Import here to avoid circular dependancies
from app import routes
