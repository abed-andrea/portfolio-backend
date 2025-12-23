from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db import Base, engine, get_db
from app.models import ContactMessage
from app.schemas import ContactMessageCreate, ContactMessageResponse


# can implement lifespan event later (check comments at bottom)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# when someone visits this route, the root function will run and will return the Hello World object
@app.get("/hello")
def hello():
    return {"message": "Hello, World"}



@app.post("/contact", response_model=ContactMessageResponse)
def create_contact(payload: ContactMessageCreate, db: Session = Depends(get_db)): 
    # payload: ContactMessageCreate = Request body validated by Pydantic
    # db:Session ..... Per-request database session


    # Create a SQLAlchemy ORM object
    # This is just a Python object right now
    # NO database interaction happens here
    row = ContactMessage(
        name=payload.name,
        email=payload.email,
        message=payload.message
    )


    db.add(row) # Tell SQLAlchemy: Track this object and prepare it for insertion"

    db.commit() # This executes the actual INSERT statement, Postgres generates id and created_at

    db.refresh(row) #Refresh pulls the DB-generated values back into the Python object, After this: row.id and row.created_at exist

    return row # Return the ORM object
    # FastAPI:
    # - Uses response_model
    # - Converts ORM → JSON using Pydantic
    # - Only exposes fields defined in ContactMessageResponse








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


