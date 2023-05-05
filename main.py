from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    # true is the default value
    published:bool = True
    # optional filed , if user dosnt provide it , it ll defalt to None
    rating:Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data":"This is your post"}

@app.post("/createposts")
def create_posts(post:Post):
    # new post is a pydantic model 
    # can we converted into python dict - post.dict()
    # print(post.dict())
    # print(post.published)
    # print(post.rating)
    return {"new_post":f"title: {post.title} ,content: {post.content}"}