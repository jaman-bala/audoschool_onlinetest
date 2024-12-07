from datetime import date
import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "inn, name, surname, middle_name, phone_number, email, password, birthday, status_code",
    [
        (
            "21405199002504",  # Пример ИНН
            "John",  # Пример имени
            "Doe",  # Пример фамилии
            "Middle",  # Пример отчества
            "1234567890",  # Пример номера телефона
            "mamalak@gmail.com",  # Пример email
            "Mamalak312!*",  # Пример пароля
            date(1990, 1, 1),  # Пример даты рождения
            200,  # Ожидаемый статус код
        ),
    ],
)
async def test_auth_flow(
    inn,
    name,
    surname,
    middle_name,
    phone_number,
    email: str,
    password: str,
    birthday: date,
    status_code: int,
    ac: AsyncClient,
):
    # Шаг 1: Регистрация пользователя
    resp_register = await ac.post(
        "/auth/create",
        json={
            "inn": inn,
            "name": name,
            "surname": surname,
            "middle_name": middle_name,
            "phone_number": phone_number,
            "email": email,
            "password": password,
            "birthday": birthday.isoformat(),  # Преобразуем дату в строку
            "is_verified": True,
            "is_staff": True,
            "is_active": True,
            "is_superuser": False,
            "admin": True,
        },
    )
    assert resp_register.status_code == status_code
    if status_code != 200:
        return  # Если регистрация не успешна, выходим из теста

    resp_login = await ac.post(
        "/auth/login",
        json={
            "email": email,
            "password": password,
        },
    )
    assert resp_login.status_code == 200
    assert ac.cookies["access_token"]
    assert "access_token" in resp_login.json()

    resp_me = await ac.get("/auth/me")
    assert resp_me.status_code == 200
    user = resp_me.json()["data"]
    print(user)
    assert user["email"] == email
    assert "id" in user
    assert "password" not in user
    assert "hashed_password" not in user

    resp_logout = await ac.delete("/auth/logout")
    assert resp_logout.status_code == 200
    assert "access_token" not in ac.cookies
