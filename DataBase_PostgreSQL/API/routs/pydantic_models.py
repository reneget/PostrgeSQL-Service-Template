import datetime

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    user_id: int
    name: str
    login: str
    password: str
    is_active: bool
    create_time: datetime.datetime

class UserUpdate(BaseModel):
    name: Optional[str] = None
    login: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None


class UserCreate(BaseModel):
    name: str
    login: str
    password: str
    create_time: datetime.datetime

