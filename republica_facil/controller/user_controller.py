from http import HTTPStatus

from fastapi import APIRouter

from republica_facil.schemas.user_schema import Message, UserPublic, UserSchema
from republica_facil.service.user_service import create_user_service

router = APIRouter()


@router.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@router.post(
    '/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic
)
def create_user(user: UserSchema):
    return create_user_service(user)
