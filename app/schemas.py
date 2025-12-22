# BaseModel is base class for all schemas (aka "This class defines validated input/output data"), EmailStr is special type provided by Pydantic
from pydantic import BaseModel, EmailStr


# defines what the client is allowed to send to your API
class ContactMessageCreate(BaseModel):
    name: str
    email: EmailStr
    message: str

# for output/response... inherits from ContactMessageCreate because output includes everything the user sent PLUS extra fields added by the server 
# DB generates the id, the client does not send it but the client should recieve it
class ContactMessageResponse(ContactMessageCreate):
    id: int 

    # tells pydantic that you will recieve SQLAlchemy objects, not dictionaries
    # without this, FastAPI cannot convert ORM objects to JSON
    class Config:
        from_attributes = True

