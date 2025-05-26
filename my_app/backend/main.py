from fastapi import FastAPI
from backend.core.db import create_db_and_tables
from backend.models.fruit import Fruit
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

my_fast_api_app = FastAPI()

@my_fast_api_app.on_event("startup")
def on_startup():
    create_db_and_tables()

#mount static assets
my_fast_api_app.mount("/static", StaticFiles(directory="ui"), name="static")

#Serve index.html
@my_fast_api_app.get("/", response_class=HTMLResponse)
async def root():
    with open("ui/index.html") as f:
        return HTMLResponse(content=f.read())

from backend.routes.fruit import router as fruit_router
my_fast_api_app.include_router(fruit_router, prefix="/api", tags=["fruits"])