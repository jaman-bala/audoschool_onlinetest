from src.models import AvatarOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import AvatarDataMapper


class ImagesRepository(BaseRepository):
    model = AvatarOrm
    mapper = AvatarDataMapper

    async def upload(self, user_id: int, avatar_url: str):
        image = self.model(avatar_url=avatar_url, user_id=user_id)
        await self.session.add(image)
        await self.session.commit()
