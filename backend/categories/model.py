from backend.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Category(db.Model):
    __tablename__ = "categories"
    name:str
    description:str
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    description = db.Column(db.String(255),nullable=False)
    image = db.Column(db.String(255), nullable=False)
    created_by  = db.Column(db.Integer,db.ForeignKey('users.id'))
    created_at = db.Column(db.String(255),nullable=True, default=datetime.now())
    updated_at = db.Column(db.String(255),nullable=True, onupdate=datetime.now())
    
    fooditems = db.relationship("FoodItem", backref="category")

    def __init__(self, description, name,created_by, image):
     self.description = description
     self.image = image
     self.name = name
     self.created_by = created_by
    

    def __repr__(self):
        return f"<Category {self.name} >"
