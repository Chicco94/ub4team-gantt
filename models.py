from dataclasses import dataclass

@dataclass(init=True)
class FantasyRecord():
    fr_id: int
    fr_descr: str
    fr_fk1: int = None
    fr_idcliente: int = None
    cliente: str = None

    def __eq__(self, obj)->bool:
        return self.fr_id == obj.fr_id

@dataclass(init=True)
class Utente():
    database: str
    telegram: str