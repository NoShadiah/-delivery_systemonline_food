from backend.db import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Order(db.Model):
    __tablename__ = "orders"

    food_item_id:str
    quantity:int
    grand_total:int
    address_id:str
    status:str

    id = db.Column(db.Integer, primary_key = True)
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_items.id'))
    quantity = db.Column(db.Integer)
    grand_total = db.Column(db.Integer, nullable=False)
    made_at = db.Column(db.DateTime, default=datetime.now())
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    status = db.Column(db.String(20), default="Pending")
    # updated_by = db.Column(db.Integer, onupdate=db.ForeignKey('users.id'))
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   


    def __init__(self, quantity,grand_total, address_id,food_item_id, status):
     self.quantity = quantity
     self.grand_total = grand_total
     self.address_id = address_id
     self.food_item_id = food_item_id
     self.status = status
    

    def __repr__(self):
        return f"<Order {self.address_id} >"
