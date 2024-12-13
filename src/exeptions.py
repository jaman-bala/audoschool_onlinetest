from fastapi import HTTPException


class AllErrorException(Exception):
    detail = "Неожиданная ошибка"

    def __init__(self, *args, **kwargs):
        super().__init__(self.detail, *args, **kwargs)


class PasswordNoCorrect(AllErrorException):
    detail = "Валидация пароля не прошла"


class ObjectNotFoundException(AllErrorException):
    detail = "Объект не найден"


class ObjectAlreadyExistsException(AllErrorException):
    detail = "Похожий объект уже существует"


class UserNotFoundException(AllErrorException):
    detail = "Пользователь не найден"


class UserAlreadyExistsException(AllErrorException):
    detail = "Пользователь уже существует"


class AuthServiceException(AllErrorException):
    detail = "Ошибка авторизации"


class InvalidTokenException(AllErrorException):
    detail = "Неверный токен"


class EmailNotFoundException(AllErrorException):
    detail = "Пользователь с таким email уже зарегистрирован"


class IncorrectPasswordException(AllErrorException):
    detail = "Пароль неверный"


class PhoneAlreadyExistsException(AllErrorException):
    detail = "Пользователь с таким номером телефона уже существует"


class ExpiredTokenException(AllErrorException):
    detail = "Срок действия токена истек. Пожалуйста, авторизуйтесь заново."


class FaceNoCorrectionException(AllErrorException):
    detail = "Ошибка распознавания лица"


class AnswerNotFoundException(AllErrorException):
    detail = "Ответ не найден"


class GroupNotFoundException(AllErrorException):
    detail = "Группа не найден"


class PaymentNotFoundException(AllErrorException):
    detail = "Платёж не найден"


class QuestionNotFoundException(AllErrorException):
    detail = "Вопрос не найден"


class ReportNotFoundException(AllErrorException):
    detail = "Отчёт не найден"


class ThemeNotFoundException(AllErrorException):
    detail = "Тема не найден"


class TicketNotFoundException(AllErrorException):
    detail = "Билет не найден"


class TotalNotFoundException(AllErrorException):
    detail = "Финальный отчёт не найден"


class AllErrorHTTPException(HTTPException):
    status_code = 500
    detail = None

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserEmailAlreadyExistsHTTPException(AllErrorHTTPException):
    status_code = 409
    detail = "Пользователь с таким email не зарегистрирован"


class UserAlreadyHTTPException(AllErrorHTTPException):
    status_code = 409
    detail = "Пользователь не найден"


class UserEmailAlreadyHTTPException(AllErrorHTTPException):
    status_code = 409
    detail = "Пользователь с таким email зарегистрирован"


class IncorrectPasswordHTTPException(AllErrorHTTPException):
    status_code = 401
    detail = "Пароль неверный"


class IncorrectTokenHTTPException(AllErrorHTTPException):
    status_code = 401
    detail = "Неправильный токен доступа"


class InnAlreadyExistsHTTPException(AllErrorHTTPException):
    status_code = 409
    detail = "Пользователь с таким ИНН уже существует"


class UserNotRegisteredHTTPException(AllErrorHTTPException):
    status_code = 404
    detail = "Пользователь не зарегистрирован"


class ExpiredTokenHTTPException(AllErrorHTTPException):
    status_code = 401
    detail = "Срок действия токена истек"


class FaceNotImagesHTTPException(AllErrorHTTPException):
    status_code = 401
    detail = "Лицо не найдено в базе данных"


class ForbiddenHTTPException(AllErrorHTTPException):
    status_code = 403
    detail = "Недостаточно прав!"


class ImagesFormatHTTPException(AllErrorHTTPException):
    status_code = 400
    detail = "Неподдерживаемый тип файла. Допустимы только JPEG или PNG."


class ImagesSizeHTTPException(AllErrorHTTPException):
    status_code = 400
    detail = "Размер изображения превышает допустимый размер."


class ImagesAlreadyHTTPException(AllErrorHTTPException):
    status_code = 404
    detail = "Изображение не найдено"


class CurrentRolesHTTPException(AllErrorHTTPException):
    status_code = 401
    detail = "Недостаточно прав для выполнения этого действия."


class RolesSuperuserHTTPException(AllErrorHTTPException):
    status_code = 403
    detail = "Доступ запрещен. Только суперпользователь может использовать эту ручку."


class RolesAdminHTTPException(AllErrorHTTPException):
    status_code = 403
    detail = "Доступ запрещен. Только администратор может использовать эту ручку."


class RolesUserHTTPException(AllErrorHTTPException):
    status_code = 403
    detail = "Доступ запрещен. У вас нет прав."


class AnswerHTTPException(AllErrorHTTPException):
    status_code = 404
    detail = "Ответ не найден"
