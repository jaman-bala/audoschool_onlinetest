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


class InnAlreadyExistsException(AllErrorException):
    detail = "Пользователь с таким ИНН уже существует"


class ExpiredTokenException(AllErrorException):
    detail = "Срок действия токена истек. Пожалуйста, авторизуйтесь заново."


class FaceNoCorrectionException(AllErrorException):
    detail = "Ошибка распознавания лица"


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


class ForbiddenException(AllErrorHTTPException):
    status_code = 403
    detail = "Недостаточно прав!"


class ImagesFormatException(AllErrorHTTPException):
    status_code = 400
    detail = "Неподдерживаемый тип файла. Допустимы только JPEG или PNG."


class ImagesSizeException(AllErrorHTTPException):
    status_code = 400
    detail = "Размер изображения превышает допустимый размер."


class ImagesAlreadyException(AllErrorHTTPException):
    status_code = 404
    detail = "Изображение не найдено"


class CurrentRolesException(AllErrorHTTPException):
    status_code = 401
    detail = "Недостаточно прав для выполнения этого действия."


class RolesSuperuserException(AllErrorHTTPException):
    status_code = 403
    detail = "Доступ запрещен. Только суперпользователь может использовать эту ручку."


class RolesAdminException(AllErrorHTTPException):
    status_code = 403
    detail = "Доступ запрещен. Только администратор может использовать эту ручку."


class RolesUserException(AllErrorHTTPException):
    status_code = 403
    detail = "Доступ запрещен. У вас нет прав."
