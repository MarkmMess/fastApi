from model.user import User
from errors import Missing, Duplicate

fakes = [
    User(name="stive",
         hash="qwert"),
    User(name="Alex",
         hash="asdfg"),
]

def find(name: str) -> User | None:
    for u in fakes:
        if u.name == name:
            return u
    return None

def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f"User {name} not found")

def check_duplicate(name: str):
    if name in fakes:
        raise Duplicate(msg=f"User {name} already exists")

def get_all() -> list[User]:
    return fakes

def get_one(name: str) -> User:
    check_missing(name)
    return find(name)

def create(user: User) -> User:
    check_duplicate(user.name)
    fakes.append(user)
    return user

def modify(name:str, user: User) -> User:
    check_missing(name)
    return user

def delete(name:str) -> User:
    check_missing(name)
    return None



