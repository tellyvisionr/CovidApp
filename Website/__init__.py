from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret key'
    from .views import views
    from .API import API

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(API, url_prefix='/')
    return app

