from src.models import GroupOrm, TicketOrm, TotalOrm, ThemeOrm
from src.repositories.mappers.base import DataMapper

from src.models.users import UsersOrm
from src.models.images import AvatarOrm, ImagesOrm
from src.models.questions import QuestionOrm
from src.models.answers import AnswerOrm
from src.schemas.answers import Answer
from src.schemas.avatars import Avatar
from src.schemas.questions import Question
from src.schemas.tickets import Ticket
from src.schemas.users import User


class UserDataMapper(DataMapper):
    db_model = UsersOrm
    schema = User


class AvatarDataMapper(DataMapper):
    db_model = AvatarOrm
    schema = Avatar

class ImageDataMapper(DataMapper):
    db_model = ImagesOrm
    schema = Images


class QuestionDataMapper(DataMapper):
    db_model = QuestionOrm
    schema = Question


class AnswerDataMapper(DataMapper):
    db_model = AnswerOrm
    schema = Answer


class GroupDataMapper(DataMapper):
    db_model = GroupOrm
    schema = Group


class TicketDataMapper(DataMapper):
    db_model = TicketOrm
    schema = Ticket

class TotalDataMapper(DataMapper):
    db_model = TotalOrm
    schema = Total

class ThemeDataMapper(DataMapper):
    db_model = ThemeOrm
    schema = Theme