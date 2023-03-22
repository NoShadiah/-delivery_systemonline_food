from flask import  jsonify, request, Blueprint
from backend.food_items.model import FoodItem
from backend.db import db
import datetime
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


food_items = Blueprint('food_items', __name__, url_prefix='/food_items')

#get all food_items
@food_items.route("/all")
def all_food_items():
    food_items= FoodItem.query.all()
    return jsonify({
            "success":True,
            "data":food_items,
            "total":len(food_items)
        }),200



#creating food_items
# @jwt_required()
@food_items.route('/create', methods= ['POST'])
def new_food_item():

    data = request.get_json()
    name = data['name']
    description = data['description']
    #created_by =  get_jwt_identity()
    image = data['image']
    created_by = data['created_by']
    category = data['category_id']
    price = data['price']
    
      
  
    #validations
    if not name :
         return jsonify({'error':"FoodItem name is required"})
    
    if not description :
         return jsonify({'error':"FoodItem description is required"})
    

    if FoodItem.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "FoodItem name exists"}), 409 

    new_food_FoodItem = FoodItem(name=name,
                                 created_by=created_by, 
                                 image=image, 
                                 description=description,
                                 price=price, 
                                 category_id=category) 
      
    #inserting values
    db.session.add(new_food_FoodItem)
    db.session.commit()
    return jsonify({'message':'New food FoodItem created sucessfully','data': new_food_FoodItem}),201
          
   
  
    

#get,edit and delete food FoodItem by id
@food_items.route('/food_item/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_food_FoodItem(id):
    food_item = FoodItem.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            "id":food_item.id,
            "name": food_item.name,
            "created_by":food_item.created_by,
            "created_at": food_item.created_at
          
        }
        return {"success": True, "FoodItem": response,"message":"Food FoodItem details retrieved"}

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['name']:
            return jsonify({"message":"Food FoodItem name is required"})
    
        
        food_item.name = data['name']
        food_item.image = data['image']
        food_item.description = data['description']
        food_item.category_id = data['category_id']
        food_item.price = data['price']
        

        db.session.add(food_item)
        db.session.commit()
        return {"message": f"{food_item.name}  Food FoodItem updated successfully"}

    elif request.method == 'DELETE':
        db.session.delete(food_item)
        db.session.commit()
        return {"message": f"{food_item.name} Food FoodItem successfully deleted."}   
  
        
  
   





        
  


