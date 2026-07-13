from pydantic import BaseModel # type: ignore

class GameResponse(BaseModel):
    story: str
    inventory_add: list[str]
    journal_add: list[str]
    visible_objects: list[str]
    objective_completed: list[str]