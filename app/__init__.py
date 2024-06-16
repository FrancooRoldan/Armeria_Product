from flask import Flask
from flask_cors import CORS
from app.config.database import *
from app.models import *
from flask_caching import Cache
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from app.controllers import product

ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()

def create_app():
  config_name = os.getenv('FLASK_ENV')
  app = Flask(__name__)

  # app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
  # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  f = config.factory(config_name if config_name else 'development')
  app.config.from_object(f)
  
  db.init_app(app)
  ma.init_app(app)
  migrate.init_app(app, db)

  app.register_blueprint(product, url_prefix='/api/v1')
  @app.shell_context_processor
  def ctx():
    return {"app": app, "db": db}
  
  return app