from dataclasses import dataclass


@dataclass
class TableItem:

    website: str
    popularity: int
    frontend: list
    backend: list
    database: list
    notes: str
