from fastapi import APIRouter, Depends, HTTPException
from src.services.item_service import ItemService

router = APIRouter()

@router.get("/")
def get_all_items():
    return ItemService.get_all_items()