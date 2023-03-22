#register a new user
from flask import  jsonify, request, Blueprint
from backend.users.model import User
from backend.db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token

users = Blueprint('users', __name__, url_prefix='/users')

#user login
@users.route("/login", methods=["POST"])
def login():
    email = request.json.get("email")
    user_password = request.json.get("password")
    user = User.query.filter_by(email=email).first()

    if not email or not user_password:
        return jsonify({"message": "All fields are required"})
    
  
    
    if user:
      is_password_correct=check_password_hash(user.password, user_password)
      if is_password_correct:
          access_token = create_access_token(identity=user.email) #to make JSON Web Tokens for authentication
          return jsonify({
           "message":"Successfully logged in a user",
          "access_token":access_token,
          "user":user}) #to access a token
      else:
        return jsonify({"message": "Invalid password"})
    else:
        return jsonify({"message": "email address doesn't exist"})
    

#get all users
@users.route("/all")
def all_users():
    users= User.query.all()
    return jsonify({
            "success":True,
            "data":users,
            "total":len(users)
        }),200

@users.route('/register',methods=['POST'])
def create_user():
    user_name =request.json['name']
    user_email = request.json['email']
    user_contact =request.json['contact']  
    user_password = request.json['password']
    user_user_type=request.json['user_type']
    password_hash = generate_password_hash(user_password)
  


    # validations
    #getting the user a data
    if not user_name:
        return jsonify({'Message':"Username is required"}),400
    
    if not user_email:
        return jsonify({'Message':"Email is required"}),400
    
    if not user_contact:
        return jsonify({'Message':"Contact is required"}),400
    
    if not user_password:
        return jsonify({'Message':"Password is required"}),400
    
    # password validation length
    if len(user_password)<6:
        return jsonify({'Message':"Password must be atleast 6 characters long"})
    
    # if not user_address:
    #     return jsonify({'Message':"Address is required"}),400
    
    #constaints
    if User.query.filter_by(email=user_email).first():
       return jsonify({'Message':"user_email already exists"}),409
    
    
    existing_user_contact=User.query.filter_by(contact=user_contact).first()
    if existing_user_contact:
            return jsonify({'Message':"user_contact already in use"}),409
     
    

    #storing new user
    new_user = User( name = user_name,
                    email = user_email,
                    contact = user_contact,
                    password=password_hash,
                     user_type=user_user_type)
    #  address = user_address,
    

    #adding a new users to the database
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
                    'Success':True,
                    'Message':f"{new_user.name} you have successfully created an account",
                    }),201




    


@users.route('/user/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == 'GET':
        response = {
            "id":user.id,
            "name": user.name,
            "user_type":user.user_type,
            "email": user.email,
            "contact": user.contact
        }
        return {"success": True,"message":"User details retrieved", "user": response}

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['name']:
            return jsonify({"message":"Your name is required"})
        
        if not data['email']:
            return jsonify({"message":"Your email address is required"})
        
        if not data['contact']:
            return jsonify({"message":"Your contact is required"})
        
        if not data['password'] or len(data['password'])<6:
            return jsonify({"message":"Your password is required and must be greater than 6 characters"})
        
        user.name = data['name']
        user.email = data['email']
        user.contact = data['contact']
        user.password = generate_password_hash(data['password'])
        user.updated_at = datetime.now()
        db.session.add(user)
        db.session.commit()
        return {"message": f"User details of {user.name} updated successfully"}

    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {user.name} successfully deleted."}   
  



