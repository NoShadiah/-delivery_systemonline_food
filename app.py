from backend import create_app, db
from flask_migrate import Migrate
from backend.users.model import User
from backend.regions.model import Region
from backend.districts.model import District
from backend.addresses.model import Address
from backend.categories.model import Category
from backend.food_items.model import FoodItem
from backend.orders.model import Order
from flask_jwt_extended import JWTManager

app = create_app('development')
migrate = Migrate(app, db)
jwt = JWTManager(app)


@app.shell_context_processor
def make_shell_context():
   return dict(db=db, 
               User=User, 
               Region=Region, 
               District=District, 
               Address=Address, 
               Category=Category, 
               FoodItem=FoodItem,
               Order=Order)