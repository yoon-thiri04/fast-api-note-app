from app.db import db
from app.models.user import  UserRegister,UserLogin,UserResponse
from app.utils.password import hash
user_collection= db["users"]
# user register
async def register_user(user:UserRegister):
    hashed_password= hash(user.password)
    user_data =user.model_dump()
    user_data['password']=hashed_password
   
    result = await user_collection.insert_one(
        user_data
    )
    return UserResponse(id=str(result.inserted_id), **user_data)

# get_user by email
async def get_user_by_email(email:str):
    user = await user_collection.find_one(
        {"email":email}
    )

    if user:
        return UserResponse(id=str(user["_id"]), **user)
    
    return None