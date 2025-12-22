from datetime import datetime
from sqlalchemy import String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


# python class definition, inheriting from Base = telling sqlalchemy this is not a regular class, it is a blueprint for database table
class ContactMessage(Base):
    __tablename__ = "contact_messages" # name the table

    # The Left Side (id: Mapped[int]): This is the Python Type. It is purely for your IDE and for FastAPI to understand the data format.
    # The Right Side (= mapped_column(...)): This is the Database Configuration. It handles the actual SQL rules like length, primary keys, and constraints.
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))
    message: Mapped[str] = mapped_column(Text())
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())