from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
import time

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
def root() -> str:
    return ("Вас приветствует ветеринарная клиника имени Тим. Собакина. Используйте команды из документации. Для "
            "просмотра документации используйте ключ docs.")


@app.post("/post")
def get_post() -> Timestamp:
    post_db.append(Timestamp(id=post_db[-1].id + 1, timestamp=int(time.time())))
    return post_db[-1]


@app.get("/dog")
def get_dogs(kind: DogType = "all_dogs") -> list:
    result = [dog for dog in dogs_db.values() if dog.kind == kind] if kind != "all_dogs" else [dog for dog in dogs_db.values()]
    return result


@app.post("/dog")
def create_dog(dog_dict: dict) -> Dog:
    dogs_db.update({len(dogs_db): Dog(name=dog_dict.get("name"), pk=dog_dict.get("pk"), kind=dog_dict.get("kind"))})
    return dogs_db.get(len(dogs_db) - 1)


@app.get("/dog/{pk}")
def get_dog_by_pk(pk: int) -> Dog:
    result: Dog
    for dog in dogs_db.values():
        if dog.pk == pk:
            result = dog
    return result

@app.patch("/dog/{pk}")
def update_dog(pk: int, dog_dict: dict) -> Dog:
    result: Dog
    for dog_id, dog in dogs_db.items():
        if dog.pk == pk:
            dogs_db.update({dog_id: Dog(name=dog_dict.get("name"), pk=dog_dict.get("pk"), kind=dog_dict.get("kind"))})
            result = dogs_db.get(dog_id)
    return result
