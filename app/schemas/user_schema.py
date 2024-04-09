from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
class UserAuth(BaseModel):
    email: EmailStr = Field(...,description='E-mail do Usuário')
    username: str = Field(
        ...,
        min_length=5,
        max_length=50,
        description='Username'
    )
    password: str = Field(
        ...,
        min_length=5,
        max_length=20,
        description='Senha do Usuário'
    )

class UserDetail(BaseModel):
    user_id: UUID
    username: str
    email: str