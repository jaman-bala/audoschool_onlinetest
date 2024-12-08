from src.models import ThemeOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ThemeDataMapper


class ThemesRepository(BaseRepository):
    model = ThemeOrm
    mapper = ThemeDataMapper
