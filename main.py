# Building Social Media Clone API with FastAPI

from fastapi import FastAPI


app=FastAPI()

@app.get("/")
def read_root():                    # Async is used only when we have to do some I/O operations like database calls, file handling, etc. It is not necessary to use async if we are just returning a simple response.
    return {"Hello": "World"}               # In normal function , we can just use def instead of async def.
 
