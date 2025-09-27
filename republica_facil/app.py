from fastapi import FastAPI

from republica_facil.controller.user_controller import router

app = FastAPI()
app.include_router(router)
