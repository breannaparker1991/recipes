from flask import Flask
from flask_app.gitingore.env import KEY

app = Flask(__name__)
app.secret_key = KEY