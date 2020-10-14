from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Import all your API endpoint methods here
import is452.routes.square
