import os
import pytest
from model.user import User
from fastapi import HTTPException

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from web import user

@pytest.fixture
def sample() -> User:
    return User(name="Mr.Smith",
        hash="qwerty")

def test_create(sample):
    resp = user.create(sample)
    assert resp == sample

def test_create_duplicate(sample):
    with pytest.raises(HTTPException):
        _ = user.create(sample)

def test_get_one(sample):
    resp = user.get_one(sample.name)
    assert resp == sample

def test_get_one_missing():
    with pytest.raises(HTTPException):
        _ = user.get_one("boxturtle")

def test_modify(sample):
    sample.hash = "Street"
    resp = user.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing():
    thing: user = User(name="Ms.Labuba", hash="qwerty")
    with pytest.raises(HTTPException):
        user.modify(thing.name, thing)

def test_delete(sample):
    resp = user.delete(sample.name)
    assert resp is None

def test_delete_missing(sample):
    with pytest.raises(HTTPException):
        user.delete(sample.name)

def test_unarchive(sample):
    resp = user.unarchive(sample.name)
    assert resp == User(name="Mr.Smith", hash="Street")