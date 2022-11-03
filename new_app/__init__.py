from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from new_app.config import Configuration

myapp = Flask(__name__)
myapp.config.from_object(Configuration)
api = Api(myapp)




db = SQLAlchemy(myapp)

# with app.app_context():
#     db.create_all()
