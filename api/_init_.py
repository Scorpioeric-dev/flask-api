from Flask import Flask
from flask_sqlalchemy import flask_sqlalchemy


def create_app()
app = Flask(_name_)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://database.db'

from .views import main
app.register_blueprint(main)

return app