from backend.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class FoodItem(db.Model):
  __tablename__ = 'food_items'

  name:str
  price:int
  price_unit:str
  image:str
  
  category_id:int

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100),unique=True)
  description = db.Column(db.String)
  price = db.Column(db.String(255))  
  price_unit = db.Column(db.String(10),default='UGX')
  image = db.Column(db.String(255))
  category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
  created_by  = db.Column(db.Integer,db.ForeignKey('users.id'))
  created_at = db.Column(db.String(255),nullable=True, default=datetime.now())
  updated_at = db.Column(db.String(255),nullable=True, onupdate=datetime.now())

  orders = db.relationship("Order", backref="fooditem")
  


  def __init__(self, name,image,price,category_id,created_by, description):
   self.name = name
   self.image = image
   self.price = price
   self.created_by = created_by
   self.description = description


  

  def __repr__(self):
        return f"<FoodItem {self.name} >"
  

        
