from flask import Flask
from app.routes.routes import main_routes


def criar_app():
    app = Flask(__name__)

    app.register_blueprint(main_routes) #Aqui registro as rotas

    return app
