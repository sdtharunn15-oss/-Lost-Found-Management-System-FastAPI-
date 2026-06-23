from pydantic import BaseModel, EmailStr
from datetime import date


# USER

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str

    class Config:
        from_attributes = True


# LOST ITEM

class LostItemCreate(BaseModel):
    item_name: str
    category: str
    description: str
    lost_date: date
    lost_location: str
    image_url: str


class LostItemResponse(LostItemCreate):
    id: int
    status: str

    class Config:
        from_attributes = True


# FOUND ITEM

class FoundItemCreate(BaseModel):
    item_name: str
    category: str
    description: str
    found_date: date
    found_location: str
    image_url: str


class FoundItemResponse(FoundItemCreate):
    id: int
    status: str

    class Config:
        from_attributes = True


from typing import Optional

class LostItemUpdate(BaseModel):
    item_name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    lost_date: Optional[date] = None
    lost_location: Optional[str] = None
    image_url: Optional[str] = None
    status: Optional[str] = None        


   

class FoundItemUpdate(BaseModel):
    item_name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    found_date: Optional[date] = None
    found_location: Optional[str] = None
    image_url: Optional[str] = None
    status: Optional[str] = None