from flask import Flask, Blueprint
from flask_restx import Api
# from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
# app.wsgi_app = ProxyFix(app.wsgi_app)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)


api = Api(app, title='Api Flask Experiments', version='1.0', description='Api de experimentos com python flask',prefix='/api')