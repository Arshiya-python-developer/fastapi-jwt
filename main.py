from fastapi import FastAPI , HTTPException ,Depends
from src.model import Postschema , UserSchema , UserLoginSchema
from src.auth.jwt_handler import SignJWT
from src.auth.jwt_bearer import JwtBearer

import json
import os

data_dir = os.path.join(os.path.dirname(__file__), 'data')
posts_file = os.path.join(data_dir, 'posts.json')

with open(posts_file, 'r') as file:
    posts = json.load(file)

users = []



app = FastAPI()



@app.get("/")
async def root():
    return {"Hello":"(:"}


# get posts
@app.get("/posts",tags=["posts"])
async def get_posts():
    return {"data":posts}


@app.get("/posts/{id}",tags=["posts"])
async def get_posts_by_id(id:int):
    if id > len(posts):
        raise HTTPException(status_code=404,detail="not fount")

    for post in posts:
        if post["id"] == id:
            return {"data":post}
        else:
            raise HTTPException(status_code=404,detail="not fount")



@app.post("/posts",dependencies=[Depends(JwtBearer())],tags=["posts"])
async def insert_post(post:Postschema):
    new_id = len(posts) + 1
    post_data = post.dict()
    post_data["id"] = new_id

    posts.append(post_data)

    with open(posts_file, 'w') as file:
        json.dump(posts, file, indent=4)
    raise HTTPException(status_code=200,detail="insert successfully")



@app.post("/user/signup",tags=["users"])
def user_signup(user:UserSchema):
    users.append(user)

    return  SignJWT(user.email)


def check_user(data:UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        else:
            False



@app.post("/user/login",tags=["users"])
def user_login(user:UserLoginSchema):
    if check_user(user):
        return  SignJWT(user.email)
    else:
        return {
            "error":"Invalid login details"
        }

