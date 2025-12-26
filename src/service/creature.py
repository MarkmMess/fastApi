from model.creature import Creature
import data.creature as data

def get_all() -> list[Creature]:
    return data.get_all()

def get_one(name: str) -> Creature | None:
    return data.get_one(name)

def create(creature: Creature) -> Creature:
    return data.create(creature)

def modify(name: str, creature: Creature) -> Creature:
    return data.modify(name, creature)

def replace(creature: Creature) -> str:
    return f"No need to replace {creature.name}"

def delete(name: str) -> bool:
    return data.delete(name)