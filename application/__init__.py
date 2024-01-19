from flask import Flask
from application.database import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate = Migrate(app, db)
    
    from application.models.stock_price import StockPrice

    return app