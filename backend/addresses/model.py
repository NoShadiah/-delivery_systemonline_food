from backend.db import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Address(db.Model):

    __tablename__ = "addresses"
     
    name:str


    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),nullable=False)
    district_id = db.Column(db.Integer,db.ForeignKey('districts.id'))
    added_by  = db.Column(db.Integer,db.ForeignKey('users.id'))
    created_at = db.Column(db.String(255),nullable=True, default=datetime.now())
    updated_at = db.Column(db.String(255),nullable=True, onupdate=datetime.now())
    orders = db.relationship("Order",  backref="address")
   

    def __init__(self, district_id, name,added_by):
     self.district_id = district_id
     self.name = name
     self.added_by = added_by
     
    

    def __repr__(self):
        return f"<Address {self.name} >"
