from model.explorer import Explorer
# фиктивные данные, в главе 10 они будут заменены на реальную базу данных и SQL
_explorers = [
    Explorer(name="Claude Hande",
        country="FR",
        description="Scarce during full moons"),
    Explorer(name="Noah Weiser",
        country="DE",
        description="Myopic machete man"),
    ]

def get_all() -> list[Explorer]:
    return _explorers

def get_one(name:str) -> Explorer | None:
    for explorer in _explorers:
        if explorer.name == name:
            return explorer
    return None

def create(explorer: Explorer) -> Explorer:
    return explorer

def modify(explorer: Explorer) -> Explorer:
    return explorer

def replace(explorer: Explorer) -> Explorer:
    return explorer

def delete(name: str):
    return False