FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y libgl1-mesa-glx

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD alembic upgrade head && python src/main.py
