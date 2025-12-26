from sqlite3 import IntegrityError
from model.user import User
from .init import curs
from errors import Missing, Duplicate

curs.execute("""create table if not exists users (
                name text primary key,
                hash text primary key)""")

curs.execute("""create table if not exists xusers (
                name text primary key,
                hash text primary key)""")

def row_to_model(row: tuple) -> User:
    name, hash = row
    return User(name=name, hash=hash)

def model_to_dict(user: User) -> dict:
    return user.model_dump()

def get_one(name: str) -> User:
    qry = "select * from users where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"User {name} not found")

def get_all() -> list[User]:
    qry = "select * from users"
    curs.execute(qry)
    rows = curs.fetchall()
    return [row_to_model(user) for user in rows]

def create(user: User, table:str = "users"):
    qry = f"insert into {table} (name, hash) values (:name, :hash)"
    params = model_to_dict(user)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(msg=f"User {user.name} already exists")
    return get_one(user.name)


def modify(name: str, user: User) -> User:
    qry = "update users set name=:name, hash=:hash where name=:name_orig"
    params = {
        "name": user.name,
        "hash": user.hash,
        "name_orig": name
    }
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(user.name)
    else:
        raise Missing(msg=f"User {name} not found")

def delete(name: str) -> None:
    user = get_one(name)
    qry = f"delete from users where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"Creature {name} not found")
    create(user, table="xusers")

