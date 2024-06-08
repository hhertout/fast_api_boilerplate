from src.db import SessionLocal
from src.models.item_model import Items
from src.db import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert
from typing import List
from src.models.item_model import Items

class ItemService:
    def __init__(self, db: AsyncSession = Depends(get_db)):
        self.db = db
    
    async def get_all_items(self) -> List[Items]:
        async with self.db as session:
            result = await session.execute(
                select(Items)
            )
            items = result.scalars().all()
        return items
    
    async def create_item(self, item: Items) -> Items:
        db_item = Items(name=item.name)
        async with self.db.begin():
            self.db.add(db_item)
            await self.db.commit()
        return db_item