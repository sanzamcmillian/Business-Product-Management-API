from fastapi import FastAPI
from api.routes import router
from storage.database import engine
from storage.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
