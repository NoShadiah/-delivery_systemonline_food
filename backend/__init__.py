from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config# we’ll discuss the config file next
from backend.db import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger, swag_from
from config.swagger import template, swagger_config



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.JWT_SECRET_KEY="super secret key"
    app.config.from_pyfile("../config.py")
    app.config.SWAGGER = {
        "tittle ":"Online food delivery API",
        "ui_version":3
    }


    db.init_app(app)
    # configurations with the app
    JWTManager(app)
    CORS(app)
    Swagger(app, config=swagger_config, template=template)

    from backend.users.controller import users
    # from backend.categories.controller import categories
    from backend.regions.controller import regions
    from backend.districts.controller import districts
    from backend.addresses.controller import addresses
    from backend.categories.controller import categories
    from backend.food_items.controller import food_items
    from backend.orders.controller import orders

    #registering blueprints    
    app.register_blueprint(users)
    app.register_blueprint(regions)
    app.register_blueprint(districts)
    app.register_blueprint(addresses)
    app.register_blueprint(categories)
    app.register_blueprint(food_items)
    app.register_blueprint(orders)

   
    return app