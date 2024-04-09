from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserAuth, UserDetail
from services.user_service import UserService
import pymongo
user_router = APIRouter()

@user_router.post('/adiciona', summary='Adiciona usuário', response_model=UserDetail)
async def adiciona_usuario(data:UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
         raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Username ou e-mail deste usuário já existe'
         )