from flask import Flask
from app.routes import home, api
from app.db import init_db
from dotenv import load_dotenv
from os import getenv
from app.utils import filters

load_dotenv()

def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/', static_folder='static')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='SECRETSARENOFUNUNLESSYOUSHARETHEMWITHEVERYONE'
  )

  app.jinja_env.filters['format_date'] = filters.format_date
  app.jinja_env.filters['capitalize_string'] = filters.capitalize_string

  app.register_blueprint(home)
  app.register_blueprint(api)

  # connects to the database
  init_db()

  return app