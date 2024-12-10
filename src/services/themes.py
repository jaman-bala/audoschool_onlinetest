import uuid
from datetime import datetime

from src.exeptions import ThemeNotFoundException
from src.schemas.themes import ThemeAddRequest, ThemeAdd, ThemePatch
from src.services.base import BaseService


class ThemesService(BaseService):
    async def create_themes(self, data: ThemeAddRequest):
        new_theme = ThemeAdd(
            title=data.title,
            created_date=datetime.utcnow(),
            updated_date=datetime.utcnow(),
        )
        await self.db.themes.add(new_theme)
        await self.db.commit()

    async def get_theme(self):
        theme = await self.db.themes.get_all()
        return theme

    async def patch_theme(self, theme_id: uuid.UUID, data: ThemePatch, exclude_unset: bool = False):
        theme = await self.db.themes.get_one_or_none(id=theme_id)
        if not theme:
            raise ThemeNotFoundException
        await self.db.themes.edit_patch(data, exclude_unset=exclude_unset, id=theme_id)
        await self.db.commit()

    async def delete_theme(self, theme_id: uuid.UUID):
        await self.db.themes.delete(id=theme_id)
        await self.db.commit()
