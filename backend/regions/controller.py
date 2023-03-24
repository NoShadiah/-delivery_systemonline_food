from flask import  jsonify, request, Blueprint
from backend.regions.model import Region
from backend.db import db
from datetime import datetime

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

regions = Blueprint('regions', __name__, url_prefix='api/v1/regions')

#get all regions
@regions.route("/all")
def all_regions():
    regions= Region.query.all()
    return jsonify({
            "success":True,
            "data":regions,
            "total":len(regions)
        }),200



#creating regions
@jwt_required()
@regions.route('/create', methods= ['POST'])
def create_new_region():

    data = request.get_json()
    name = data['name']
    created_by =  get_jwt_identity()
    # created_by = data['created_by']
      
  
    #validations
    if not name:
         return jsonify({'error':"Region name is required"})
    

    if Region.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "Region name exists"}), 409 

    new_region = Region(name=name,created_by=created_by) 
      
    #inserting values
    db.session.add( new_region)
    db.session.commit()
    return jsonify({'message':'New region created sucessfully','data': new_region}),200
          
   
  
    

#get,edit and delete region by id

@regions.route('/region/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def handle_region(id):
    region = Region.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            "id":region.id,
            "name": region.name,
            "created_by":region.created_by,
            "created_at": region.created_at
          
        }
        return {"success": True, "region": response,"message":"Region details retrieved"}

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['name']:
            return jsonify({"message":"Region name is required"})
    
        
        region.name = data['name']
        
        db.session.add(region)
        db.session.commit()
        return {"message": f"{region.name}  region updated successfully"}

    elif request.method == 'DELETE':
        db.session.delete(region)
        db.session.commit()
        return {"message": f"{region.name} region successfully deleted."}   
  
        
  
   



