from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, text, DateTime, Unicode, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declared_attr

from app.db.base_class import Base


if TYPE_CHECKING:
    from .gebruiker import Gebruiker  # noqa: F401
    from .beleidskeuze import Beleidskeuze  # noqa: F401


class Beleidskeuze_Beleidsprestaties(Base):
    __tablename__ = "Beleidskeuze_Beleidsprestaties"

    Beleidskeuze_UUID = Column(
        "Beleidskeuze_UUID", ForeignKey("Beleidskeuzes.UUID"), primary_key=True
    )
    Beleidsprestatie_UUID = Column(
        "Beleidsprestatie_UUID", ForeignKey("Beleidsprestaties.UUID"), primary_key=True
    )
    Koppeling_Omschrijving = Column(
        "Koppeling_Omschrijving", String(collation="SQL_Latin1_General_CP1_CI_AS")
    )

    Beleidskeuze = relationship("Beleidskeuze", back_populates="Beleidsprestaties")
    Beleidsprestatie = relationship("Beleidsprestatie", back_populates="Beleidskeuzes")


class Beleidsprestatie(Base):
    __tablename__ = "Beleidsprestaties"

    @declared_attr
    def ID(cls):
        seq_name = "seq_Beleidsprestaties"
        seq = Sequence(seq_name)
        return Column(Integer, seq, nullable=False, server_default=seq.next_value())

    UUID = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=text("(newid())"))
    Begin_Geldigheid = Column(DateTime, nullable=False)
    Eind_Geldigheid = Column(DateTime, nullable=False)
    Created_Date = Column(DateTime, nullable=False)
    Modified_Date = Column(DateTime, nullable=False)

    Created_By_UUID = Column('Created_By', UNIQUEIDENTIFIER, ForeignKey("Gebruikers.UUID"), nullable=False)
    Modified_By_UUID = Column('Modified_By', UNIQUEIDENTIFIER, ForeignKey("Gebruikers.UUID"), nullable=False)

    Titel = Column(Unicode(150), nullable=False)
    Omschrijving = Column(Unicode)
    Weblink = Column(Unicode)

    Created_By = relationship(
        "Gebruiker", primaryjoin="Beleidsprestatie.Created_By_UUID == Gebruiker.UUID"
    )
    Modified_By = relationship(
        "Gebruiker", primaryjoin="Beleidsprestatie.Modified_By_UUID == Gebruiker.UUID"
    )
    Beleidskeuzes = relationship("Beleidskeuze_Beleidsprestaties", back_populates="Beleidsprestatie")
