from flask import  jsonify, request, Blueprint
from backend.orders.model import Order
from backend.db import db
import datetime
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


orders = Blueprint('orders', __name__, url_prefix='api/v1/orders')

#get all orders
@orders.route("/all")
def all_orders():
    orders= Order.query.all()
    return jsonify({
            "success":True,
            "data":orders,
            "total":len(orders)
        }),200



#creating orders
# @jwt_required()
@orders.route('/create', methods= ['POST'])
def new_food_item():

    data = request.get_json()
    food_item_id = data['food_item_id']
    quantity = data['quantity']
    #created_by =  get_jwt_identity()
    grand_total = data['grand_total']
    status = data['status']
    address = data['address_id']
    status = data['status']

    
      
  
    #validations
    if not food_item_id :
         return jsonify({'error':"Order food_item_id is required"})
    
    if not quantity :
         return jsonify({'error':"Order quantity is required"})
    
    if not status :
        default="pending"

    # if Order.query.filter_by(food_item_id=food_item_id).first() is not None:
        # return jsonify({'error': "Order food_item_id exists"}), 409 

    new_food_Order = Order(food_item_id=food_item_id,
                                 status=status, 
                                 grand_total=grand_total, 
                                 quantity=quantity, 
                                 address_id=address) 
      
    #inserting values
    db.session.add(new_food_Order)
    db.session.commit()
    return jsonify({'message':'New food Order created sucessfully','data': new_food_Order}),201
          
   
  
    

#get,edit and delete food Order by id
@orders.route('/order/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def handle_food_Order(id):
    order = Order.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            "id":order.id,
            "food_item_id": order.food_item_id,
            "status":order.status,
            "made_at": order.made_at
          
        }
        return {"success": True, "Order": response,"message":"Food Order details retrieved"}

    elif request.method == 'PATCH':
        data = request.get_json()

        if not data['status']:
            return jsonify({"message":"Food Order food_item_id is required"})
    
        
        # order.food_item_id = data['food_item_id']
        # order.grand_total = data['grand_total']
        # order.quantity = data['quantity']
        # order.address_id = data['address_id']
        order.status = data['status']
        

        db.session.add(order)
        db.session.commit()
        return {"message": f"{order.id}  Food Order updated successfully"}

    elif request.method == 'DELETE':
        db.session.delete(order)
        db.session.commit()
        return {"message": f"{order.id} Food Order successfully deleted."}   
  
        
  
   





        
  


