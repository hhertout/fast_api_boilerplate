from typing import Union

from fastapi import FastAPI
from src.controller import item_controller

from src.migrate import run_migration
from src.db import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    run_migration()
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(item_controller.router, prefix="/api/items")