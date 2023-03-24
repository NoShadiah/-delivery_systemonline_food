from flask import  jsonify, request, Blueprint
from backend.districts.model import District
from backend.db import db
import datetime
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

districts = Blueprint('districts', __name__, url_prefix='api/v1/districts')

#get all districts
@districts.route("/all")
def all_districts():
    districts= District.query.all()
    return jsonify({
            "success":True,
            "data":districts,
            "total":len(districts)
        }),200



#creating districts
# @jwt_required()
@districts.route('/create', methods= ['POST'])
def create_new_district():

    data = request.get_json()
    name = data['name']
    region_id = data['region_id']
    # created_by =  get_jwt_identity()
    created_by = data['created_by']
      
  
    #validations
    if not name:
         return jsonify({'error':"District name is required"})
   
    if not region_id:
         return jsonify({'error':"region_id is required"})
    

    if District.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "District name exists"}), 409 

    new_district = District(name=name,created_by=created_by, region_id=region_id) 
      
    #inserting values
    db.session.add( new_district)
    db.session.commit()
    return jsonify({'message':'New district created sucessfully','data': new_district}),201
          
   
  
    

#get,edit and delete district by id
@districts.route('/district/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_district(id):
    district = District.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            "id":district.id,
            "name": district.name,
            "region": district.region.name,
            "created_by":district.created_by,
            "created_at": district.created_at
          
        }
        return {"success": True, "district": response,"message":"district details retrieved"}

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['name']:
            return jsonify({"message":"district name is required"})
        
        if not data['region_id']:
            return jsonify({"message":"district region name is required"})
        
        
        district.name = data['name']
        district.region_id = data['region_id']
        
        db.session.add(district)
        db.session.commit()
        return {"message": f"{district.name}  district updated successfully"}

    elif request.method == 'DELETE':
        db.session.delete(district)
        db.session.commit()
        return {"message": f"{district.name} district successfully deleted."}   
  
        
  
   



