from republica_facil.repository.user_repository import create_user
from republica_facil.schemas.user_schema import UserDB, UserSchema


def create_user_service(user: UserSchema) -> UserDB:
    return create_user(user)
