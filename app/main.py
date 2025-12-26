from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db import Base, engine, get_db
from app.models import ContactMessage
from app.schemas import ContactMessageCreate, ContactMessageResponse

from fastapi.middleware.cors import CORSMiddleware



# Create tables on startup
Base.metadata.create_all(bind=engine)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)




@app.get("/hello")
def hello():
    return {"message": "Hello, World"}



@app.post("/contact", response_model=ContactMessageResponse)
def create_contact(payload: ContactMessageCreate, db: Session = Depends(get_db)): 
    
    # Create a SQLAlchemy ORM object based on payload/request
    row = ContactMessage(
        name=payload.name,
        email=payload.email,
        message=payload.message
    )

    db.add(row)
    db.commit()
    db.refresh(row)

    return row