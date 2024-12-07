from src.repositories.group import ExamsRepository
from src.repositories.history import HistoriesRepository
from src.repositories.images import ImagesRepository
from src.repositories.questions import QuestionsRepository
from src.repositories.answers import AnswersRepository
from src.repositories.tickets import TicketsRepository
from src.repositories.users import UsersRepository


class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.users = UsersRepository(self.session)
        self.images = ImagesRepository(self.session)
        self.questions = QuestionsRepository(self.session)
        self.answers = AnswersRepository(self.session)
        self.exams = ExamsRepository(self.session)
        self.tickets = TicketsRepository(self.session)
        self.histories = HistoriesRepository(self.session)

        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()
