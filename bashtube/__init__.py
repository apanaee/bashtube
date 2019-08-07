from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from bashtube.config import LocalConfig, ProductionConfig

# db = SQLAlchemy()
cache = Cache()


def create_app(Config_class=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(Config_class)
    # db.init_app(app)
    cache.init_app(app)
    app.register_blueprint(playlist, url_prefix="/playlist")
    app.register_blueprint(singlevideos, url_prefix="/")
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(preview, url_prefix="/preview")
    return app


from bashtube.singlevideos.views import singlevideos
from bashtube.playlist.views import playlist
from bashtube.api.routes import api
from bashtube.preview.views import preview