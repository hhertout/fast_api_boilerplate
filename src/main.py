from typing import Union

from fastapi import FastAPI
from src.controller import item_controller

app = FastAPI()

app.include_router(item_controller.router, prefix="/api/items")