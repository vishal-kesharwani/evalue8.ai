import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.model_registry import ModelRegistryEntry
from app.schemas.model import ModelCreate


class ModelRegistryService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: ModelCreate) -> ModelRegistryEntry:
        entry = ModelRegistryEntry(**data.model_dump())
        self.db.add(entry)
        await self.db.commit()
        await self.db.refresh(entry)
        return entry

    async def list_active(self) -> list[ModelRegistryEntry]:
        result = await self.db.execute(select(ModelRegistryEntry).where(ModelRegistryEntry.active.is_(True)))
        return list(result.scalars().all())

    async def list_all(self) -> list[ModelRegistryEntry]:
        result = await self.db.execute(select(ModelRegistryEntry))
        return list(result.scalars().all())

    async def deactivate(self, model_id: uuid.UUID) -> None:
        entry = await self.db.get(ModelRegistryEntry, model_id)
        if entry is not None:
            entry.active = False
            await self.db.commit()
