import os
import shutil
import uuid

from src.config import settings
from src.services.base import BaseService
from fastapi import UploadFile


class ImagesService(BaseService):
    async def upload_image(
        self,
        user_id: int,
        file: UploadFile,
    ):
        image_filename = f"{user_id}_{file.filename}"
        image_path = os.path.join(settings.LINK_IMAGES, image_filename)
        with open(image_path, "wb+") as new_file:
            shutil.copyfileobj(file.file, new_file)
        return {"user_id": user_id, "avatar": image_path}

    async def get_all_images(
        self,
        user_id: int,
    ):
        directory = settings.LINK_IMAGES
        images = []
        for filename in os.listdir(directory):
            if filename.startswith(f"{user_id}_"):
                images.append({"user_id": user_id, "avatar": os.path.join(directory, filename)})

        return images

    async def update_image(
        self,
        user_id: int,
        file: UploadFile,
    ):
        old_image = self._get_user_image_path(user_id)
        if old_image and os.path.exists(old_image):
            os.remove(old_image)
        return await self.upload_image(user_id, file)

    async def delete_image(
        self,
        user_id: int,
    ):
        image_path = self._get_user_image_path(user_id)
        if image_path and os.path.exists(image_path):
            os.remove(image_path)
            return {"status": "Изображение удалено"}
        return {"status": "Изображение не найдено"}

    def _get_user_image_path(self, user_id: int) -> str | None:
        directory = settings.LINK_IMAGES
        for filename in os.listdir(directory):
            if filename.startswith(f"{user_id}_"):
                return os.path.join(directory, filename)
        return None

    async def upload_image_question(
        self,
        question_id: uuid.UUID,
        file: UploadFile,
    ):
        image_filename = f"{question_id}_{file.filename}"
        image_path = os.path.join(settings.LINK_UPLOAD_PHOTO, image_filename)
        with open(image_path, "wb+") as new_file:
            shutil.copyfileobj(file.file, new_file)
        return {"question_id": question_id, "avatar": image_path}

    async def get_all_images_question(
        self,
        question_id: uuid.UUID,
    ):
        directory = settings.LINK_IMAGES
        images = []
        for filename in os.listdir(directory):
            if filename.startswith(f"{question_id}_"):
                images.append({"user_id": question_id, "avatar": os.path.join(directory, filename)})

        return images
