from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum


class Role(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"


class UserRequestAdd(BaseModel):
    firstname: str = Field(default=None, max_length=100)
    lastname: str = Field(default=None, max_length=100)
    password: str
    phone: str
    is_ready: int = Field(default=None)
    group_id: UUID
    is_active: bool | None = True
    roles: list[Role] = Field(default_factory=lambda: [Role.USER])


class UserAdd(BaseModel):
    firstname: str = Field(default=None, max_length=100)
    lastname: str = Field(default=None, max_length=100)
    phone: str
    hashed_password: str
    is_ready: int = Field(default=None)
    group_id: UUID
    is_active: bool | None = True
    roles: list[Role]
    created_date: datetime
    updated_date: datetime


class UserUpdateRequest(BaseModel):
    firstname: str = Field(default=None, max_length=100)
    lastname: str = Field(default=None, max_length=100)
    avatar: str = Field(default=None, max_length=200)
    phone: str = Field(default=None, max_length=20)
    is_ready: int = Field(default=None)
    group_id: UUID = Field(default=None)
    is_active: bool = Field(default=None)
    roles: list[Role] = Field(default=None)


class UserPatchRequest(BaseModel):
    firstname: str = Field(default=None, max_length=100)
    lastname: str = Field(default=None, max_length=100)
    avatar: str = Field(default=None, max_length=200)
    phone: str = Field(default=None, max_length=20)
    is_ready: int = Field(default=None)
    group_id: UUID = Field(default=None)
    is_active: bool = Field(default=None)
    roles: list[Role] = Field(default=None)


class UserRequestLogin(BaseModel):
    phone: str
    password: str


class User(BaseModel):
    id: UUID
    firstname: str = Field(default=None, max_length=100)
    lastname: str = Field(default=None, max_length=100)
    avatar: str = Field(default=None, max_length=200)
    phone: str = Field(default=None, max_length=20)
    is_ready: int = Field(default=None)
    group_id: UUID
    is_active: bool
    roles: list[Role]
    created_date: datetime
    updated_date: datetime


class UserWithHashedPassword(User):
    hashed_password: str


class UserRequestUpdatePassword(BaseModel):
    new_password: str
    change_password: str
