# Building Social Media Clone API with FastAPI

from fastapi import FastAPI
from fastapi.params import Body # Body is used to define the request body for a POST or PUT request. It allows us to specify the expected structure of the data that will be sent in the request body.
from pydantic import BaseModel
from typing import Optional
app=FastAPI()
class Post(BaseModel):
    title: str
    content: str 
    published : bool =True
    rating: Optional[float]=None
@app.get("/")
def read_root():                    # Async is used only when we have to do some I/O operations like database calls, file handling, etc. It is not necessary to use async if we are just returning a simple response.
    return {"Hello": "World"}               # In normal function , we can just use def instead of async def.
 
@app.get("/posts")
def get_posts():
    return {"data":"This is your list of posts"}

@app.post("/createposts")
def create_posts(NewPost: Post):
    print(NewPost)
    return {"data":"New post created Successfully"} 


@app.post("/publishedpost")
def published_post(published: Post):
    print(published)
    return {"data":"Post published Successfully"}

@app.post("/ratingpost")
def rating_post(rating: Post):
    print(rating)
    return {"data":"Post rated Successfully"}


