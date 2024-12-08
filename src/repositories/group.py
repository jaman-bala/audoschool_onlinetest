from src.repositories.base import BaseRepository
from src.models import GroupOrm
from src.repositories.mappers.mappers import GroupDataMapper


class GroupsRepository(BaseRepository):
    model = GroupOrm
    mapper = GroupDataMapper
