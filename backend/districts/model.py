from backend.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class District(db.Model):
    __tablename__ = "districts"
    name:str
    region_id:int

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    region_id = db.Column(db.Integer,db.ForeignKey('regions.id'))
    created_by  = db.Column(db.Integer,db.ForeignKey('users.id'))
    created_at = db.Column(db.String(255),nullable=True, default=datetime.now())
    updated_at = db.Column(db.String(255),nullable=True, onupdate=datetime.now())
    addresses = db.relationship("Address",backref="district")
   

    def __init__(self, region_id, name,created_by):
     self.region_id = region_id
     self.name = name
     self.created_by = created_by
     
    

    def __repr__(self):
        return f"<District {self.name} >"
