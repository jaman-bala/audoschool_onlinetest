import uuid
from src.models import ImagesOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ImageDataMapper


class ImagesRepository(BaseRepository):
    model = ImagesOrm
    mapper = ImageDataMapper

    async def upload(self, question_id: uuid.UUID, photo_filename: str):
        image = self.model(filename=photo_filename, question_id=question_id)
        await self.session.add(image)
        await self.session.commit()
