from fastapi import APIRouter

from src.api.dependencies import DBDep


router = APIRouter(prefix="/payments", tags=["Платёж"])