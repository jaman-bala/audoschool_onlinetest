from src.repositories.group import GroupsRepository
from src.repositories.images import ImagesRepository
from src.repositories.payments import PaymentsRepository
from src.repositories.questions import QuestionsRepository
from src.repositories.answers import AnswersRepository
from src.repositories.themes import ThemesRepository
from src.repositories.tickets import TicketsRepository
from src.repositories.totals import TotalsRepository
from src.repositories.users import UsersRepository


class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.users = UsersRepository(self.session)
        self.images = ImagesRepository(self.session)
        self.answers = AnswersRepository(self.session)
        self.groups = GroupsRepository(self.session)
        self.payments = PaymentsRepository(self.session)
        self.questions = QuestionsRepository(self.session)
        self.reports = PaymentsRepository(self.session)
        self.themes = ThemesRepository(self.session)
        self.tickets = TicketsRepository(self.session)
        self.totals = TotalsRepository(self.session)

        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()
