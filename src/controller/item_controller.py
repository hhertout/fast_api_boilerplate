from fastapi import APIRouter, Depends, HTTPException
from src.services.item_service import ItemService
from src.models.item_model import Items
from pydantic import BaseModel

router = APIRouter()

class ItemBody(BaseModel):
    name: str

@router.get("/")
async def get_all_items(item_service: ItemService = Depends(ItemService)):
    try:
        items = await item_service.get_all_items()
        return items
    except Exception as e:
        print(e)
        return {"error": str(e)}

@router.post("/")
async def create_item(item: ItemBody, item_service: ItemService = Depends(ItemService)):
    print(item)
    try: 
        created_item = await item_service.create_item(Items(name=item.name))
        return created_item
    except Exception as e:
        print(e)
        return {"error": str(e)}