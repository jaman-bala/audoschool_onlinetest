import uuid
import aiofiles
from fastapi import UploadFile

from src.config import settings
from src.models.questions import QuestionOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import QuestionDataMapper


class QuestionsRepository(BaseRepository):
    model = QuestionOrm
    mapper = QuestionDataMapper

    async def save_photo(self, file: UploadFile) -> str:
        unique_filename = f"{uuid.uuid4()}_{file.filename}"
        file_path = f"{settings.LINK_UPLOAD_PHOTO}/{unique_filename}"
        async with aiofiles.open(file_path, "wb") as buffer:
            content = await file.read()
            await buffer.write(content)
        return f"/static/photo/{unique_filename}"

    async def upload_put(self, files: list[UploadFile]) -> list[str]:
        filenames = []
        if files:
            for file in files:
                unique_filename = f"{uuid.uuid4()}_{file.filename}"
                file_path = f"{settings.LINK_UPLOAD_FILES}/{unique_filename}"

                async with aiofiles.open(file_path, "wb") as buffer:
                    content = await file.read()
                    await buffer.write(content)

                filenames.append(f"/static/photo/{unique_filename}")

        return filenames
