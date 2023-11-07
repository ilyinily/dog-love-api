from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
import datetime

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name="Bob", pk=0, kind="terrier"),
    1: Dog(name="Marli", pk=1, kind="bulldog"),
    2: Dog(name="Snoopy", pk=2, kind="dalmatian"),
    3: Dog(name="Rex", pk=3, kind="dalmatian"),
    4: Dog(name="Pongo", pk=4, kind="dalmatian"),
    5: Dog(name="Tillman", pk=5, kind="bulldog"),
    6: Dog(name="Uga", pk=6, kind="bulldog")
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get("/")
def root():
    return ("Вас приветствует ветеринарная клиника имени Тим. Собакина. Используйте команды из документации. Для "
            "просмотра документации используйте ключ docs.")


@app.post("/post")
def get_post():
    post_db.append(Timestamp(id=post_db[-1].id + 1, timestamp=datetime.datetime.now()))
    return post_db[-1]

# ваш код здесь
