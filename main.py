from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


# Validate the data
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {'title': 'Post One', 'content': 'Welcome back', 'id': 1},
    {'title': 'Manchester United', 'content': 'glory glory glory', 'id': 2}
]

"""path operation"""


@app.get("/")
def read_root():
    return {"Message": "This is my first API"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    my_posts.append(post.dict())
    return {"data": "post"}
