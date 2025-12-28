from fastapi import APIRouter, HTTPException
from errors import Duplicate
from model.creature import Creature
import service.creature as service

router = APIRouter(prefix = "/creature")

@router.get("")
@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
def get_one(name: str) -> Creature | None:
    return service.get_one(name)

@router.post("")
@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create(creature)

@router.patch("/")
def modify(name: str, creature: Creature) -> Creature:
    try:
        return service.modify(name, creature)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.put('/')
def replace(creature: Creature) -> str:
    return service.replace(creature)

@router.delete('/{name}')
def delete(name: str):
    return service.delete(name)


