from fastapi import Depends, Query, Request, HTTPException
from pydantic import BaseModel
from typing import Annotated

from src.database import async_session_maker
from src.exeptions import InvalidTokenException
from src.services.auth import AuthService
from src.utils.db_manager import DBManager


class PaginationParams(BaseModel):
    page: Annotated[int | None, Query(1, ge=1)]
    per_page: Annotated[int | None, Query(None, ge=1, lt=100)]


PaginationDep = Annotated[PaginationParams, Depends()]


def get_token(request: Request) -> str:
    token = request.cookies.get("access_token", None)
    if not token:
        raise HTTPException(status_code=401, detail="Вы не предоставили токен доступа")
    return token


def get_current_user_id(token: str = Depends(get_token)) -> int:
    try:
        data = AuthService().decode_access_token(token)
    except InvalidTokenException:
        raise HTTPException(status_code=401, detail="Неправильный токен доступа")
    return data["user_id"]


def get_current_is_superuser(token: str = Depends(get_token)) -> bool:
    try:
        data = AuthService().decode_access_token(token)
        return data.get("is_superuser", False)
    except InvalidTokenException:
        raise HTTPException(status_code=401, detail="Неправильный токен доступа")


def get_current_admin(token: str = Depends(get_token)) -> bool:
    try:
        data = AuthService().decode_access_token(token)
        return data.get("admin", False)
    except InvalidTokenException:
        raise HTTPException(status_code=401, detail="Неправильный токен доступа")


def get_current_user(token: str = Depends(get_token)) -> bool:
    try:
        data = AuthService().decode_access_token(token)
        return data.get("user", False)
    except InvalidTokenException:
        raise HTTPException(status_code=401, detail="Неправильный токен доступа")


UserIdDep = Annotated[int, Depends(get_current_user_id)]
RoleSuperuserDep = Annotated[str, Depends(get_current_is_superuser)]
RoleAdminDep = Annotated[str, Depends(get_current_admin)]
UserDep = Annotated[str, Depends(get_current_user)]


def get_db_manager():
    return DBManager(session_factory=async_session_maker)


async def get_db():
    async with get_db_manager() as db:
        yield db


DBDep = Annotated[DBManager, Depends(get_db)]
