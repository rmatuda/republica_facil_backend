from republica_facil.schemas.user_schema import UserDB, UserSchema

database = []


def add_user(user: UserSchema) -> UserDB:
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id
