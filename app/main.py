from fastapi import FastAPI
from app.db import Base, engine
import app.models


# can implement lifespan event later (check comments at bottom)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# when someone visits this route, the root function will run and will return the Hello World object
@app.get("/hello")
def hello():
    return {"message": "Hello, World"}



# from contextlib import asynccontextmanager
# from fastapi import FastAPI
# from app.db import engine, Base
# import app.models  

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     print("Initializing database tables...")
#     Base.metadata.create_all(bind=engine)
#     print("Tables initialized!")
    
#     yield  

#     print("Shutting down...")


# app = FastAPI(lifespan=lifespan)

# @app.get("/hello")
# def hello():
#     return {"message": "Hello, World"}


