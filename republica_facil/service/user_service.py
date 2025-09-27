from republica_facil.repository.user_repository import add_user
from republica_facil.schemas.user_schema import UserDB, UserSchema


def create_user_service(user: UserSchema) -> UserDB:
    return add_user(user)
