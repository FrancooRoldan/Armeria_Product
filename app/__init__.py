from flask import Flask
from app.config.database import *
from flask_caching import Cache
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from app.controllers import product
from app.config import database
# from app.models import Product
# from flask_cors import CORS

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

  cache.init_app(app, config={'CACHE_TYPE': 'RedisCache'
                              ,'CACHE_DEFAULT_TIMEOUT':300, 'CACHE_REDIS_HOST':'localhost' #nombre del contenedor
                              ,'CACHE_REDIS_PORT':'6379','CACHE_REDIS_DB':'0',
                              'CACHE_REDIS_PASSWORD':'admin',
                              'CACHE_KEY_PREFIX':'armeria-product_'})

  app.register_blueprint(product, url_prefix='/api/v1')

  @app.shell_context_processor # PREGUNTAR QUE HACE ESTO
  def ctx(): # CTX = ??
    return {"app": app, "db": db}
  
  return app