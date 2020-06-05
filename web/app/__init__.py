from web.config import Config
from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)

from web.app import routes
