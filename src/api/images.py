from fastapi import APIRouter, UploadFile, File
from uuid import UUID

from src.services.images import ImagesService

router = APIRouter(prefix="/images", tags=["Изображения пользователей"])


@router.post("/upload/{user_id}")
async def upload_image(
    user_id: UUID,
    file: UploadFile = File(...),
):
    avatar = await ImagesService().upload_image(user_id, file)
    return {"status": "Изображение добавлено", "avatar": avatar}


@router.get("/images/{user_id}")
async def get_all_images(user_id: UUID):
    images = await ImagesService().get_all_images(user_id)
    return {"images": images}


@router.put("/update/{user_id}")
async def update_image(
    user_id: UUID,
    file: UploadFile = File(...),
):
    avatar = await ImagesService().update_image(user_id, file)
    return {"status": "Изображение обновлено", "avatar": avatar}


@router.delete("/delete/{user_id}")
async def delete_image(user_id: UUID):
    result = await ImagesService().delete_image(user_id)
    return result
