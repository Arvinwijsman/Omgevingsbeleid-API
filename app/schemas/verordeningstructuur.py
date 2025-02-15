from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel
from pydantic.utils import GetterDict

from app.util.legacy_helpers import to_ref_field

from .gebruiker import GebruikerInline


# Shared properties
class VerordeningstructuurBase(BaseModel):
    Titel: Optional[str] = None
    Structuur: Optional[str] = None
    Status: Optional[str] = None


class VerordeningstructuurCreate(VerordeningstructuurBase):
    Begin_Geldigheid: datetime
    Eind_Geldigheid: datetime


class VerordeningstructuurUpdate(VerordeningstructuurBase):
    pass


class VerordeningstructuurInDBBase(VerordeningstructuurBase):
    ID: int
    UUID: str

    Created_By: str
    Created_Date: datetime
    Modified_By: str
    Modified_Date: datetime
    Begin_Geldigheid: datetime
    Eind_Geldigheid: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


# Properties to return to client
class Verordeningstructuur(VerordeningstructuurInDBBase):
    Created_By: GebruikerInline
    Modified_By: GebruikerInline

    class Config:
        allow_population_by_field_name = True
        alias_generator = to_ref_field


# Properties properties stored in DB
class VerordeningstructuurInDB(VerordeningstructuurInDBBase):
    pass
