import uuid
from datetime import datetime

from src.exeptions import GroupNotFoundException
from src.schemas.group import GroupAddRequest, GroupAdd, GroupPatch
from src.services.base import BaseService


class GroupsService(BaseService):
    async def create_group(self, data: GroupAddRequest):
        new_group = GroupAdd(
            title=data.title,
            category=data.category,
            user_quantity=data.user_quantity,
            date_from=data.date_from,
            date_end=data.date_end,
            period=data.period,
            is_active=True,
            created_date=datetime.utcnow(),
            updated_date=datetime.utcnow(),
        )
        await self.db.groups.add(new_group)
        await self.db.commit()

    async def get_group(self):
        groups = await self.db.groups.get_all()
        return groups

    async def patch_group(self, group_id: uuid.UUID, data: GroupPatch, exclude_unset: bool = False):
        groups = await self.db.groups.get_one_or_none(id=group_id)
        if not groups:
            raise GroupNotFoundException
        await self.db.groups.edit_patch(data, exclude_unset=exclude_unset, id=group_id)
        await self.db.commit()

    async def delete_group(self, group_id: uuid.UUID):
        await self.db.groups.delete(id=group_id)
        await self.db.commit()
