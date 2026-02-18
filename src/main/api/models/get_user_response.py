from typing import List
from src.main.api.models.base_model import BaseModel
from pydantic import RootModel


class GetUserItem(BaseModel):
    id: int
    username: str
    role: str


class GetUserResponse(RootModel[List[GetUserItem]]):
    pass