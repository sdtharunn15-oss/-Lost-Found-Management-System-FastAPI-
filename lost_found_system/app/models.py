from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String, default="User")

    lost_items = relationship("LostItem", back_populates="owner")
    found_items = relationship("FoundItem", back_populates="owner")


class LostItem(Base):
    __tablename__ = "lost_items"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String)
    category = Column(String)
    description = Column(String)
    lost_date = Column(Date)
    lost_location = Column(String)
    image_url = Column(String)
    status = Column(String, default="Open")

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="lost_items")


class FoundItem(Base):
    __tablename__ = "found_items"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String)
    category = Column(String)
    description = Column(String)
    found_date = Column(Date)
    found_location = Column(String)
    image_url = Column(String)
    status = Column(String, default="Available")

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="found_items")
    claims = relationship("Claim", back_populates="found_item")


class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)

    found_item_id = Column(Integer, ForeignKey("found_items.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    status = Column(String, default="Pending")

    created_at = Column(DateTime, default=datetime.utcnow)

    found_item = relationship("FoundItem", back_populates="claims")