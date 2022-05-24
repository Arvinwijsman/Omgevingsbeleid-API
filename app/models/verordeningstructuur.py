from typing import TYPE_CHECKING

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    text,
    DateTime,
    Unicode,
    Sequence,
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER, XML
from sqlalchemy.ext.declarative import declared_attr

from app.db.base_class import Base


if TYPE_CHECKING:
    from .gebruiker import Gebruiker  # noqa: F401
    from .beleidskeuze import Beleidskeuze  # noqa: F401


class Verordeningstructuur(Base):
    __tablename__ = "Verordeningstructuur"

    @declared_attr
    def ID(cls):
        seq_name = "seq_Verordeningstructuur"
        seq = Sequence(seq_name)
        return Column(Integer, seq, nullable=False, server_default=seq.next_value())

    UUID = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newid())"))
    Begin_Geldigheid = Column(DateTime, nullable=False)
    Eind_Geldigheid = Column(DateTime, nullable=False)
    Created_Date = Column(DateTime, nullable=False)
    Modified_Date = Column(DateTime, nullable=False)

    Created_By_UUID = Column(
        "Created_By", ForeignKey("Gebruikers.UUID"), nullable=False
    )
    Modified_By_UUID = Column(
        "Modified_By", ForeignKey("Gebruikers.UUID"), nullable=False
    )

    Titel = Column(Unicode(150), nullable=False)
    Structuur = Column(XML, nullable=False)
    Status = Column(Unicode(50))

    Created_By = relationship(
        "Gebruiker",
        primaryjoin="Verordeningstructuur.Created_By_UUID == Gebruiker.UUID",
    )
    Modified_By = relationship(
        "Gebruiker",
        primaryjoin="Verordeningstructuur.Modified_By_UUID == Gebruiker.UUID",
    )
