from pydantic import BaseModel, EmailStr
from datetime import datetime


class ContactMessageCreate(BaseModel):
    name: str
    email: EmailStr
    message: str


class ContactMessageResponse(ContactMessageCreate):
    id: int 
    created_at: datetime

    # Allow Pydantic to read fields from SQLAlchemy model attributes
    class Config:
        from_attributes = True

