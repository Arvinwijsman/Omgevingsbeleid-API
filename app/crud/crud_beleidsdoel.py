from datetime import datetime

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import joinedload

from app.crud.base import CRUDBase
from app.models.beleidsdoel import Beleidsdoel
from app.schemas.beleidsdoel import BeleidsdoelCreate, BeleidsdoelUpdate


class CRUDBeleidsdoel(CRUDBase[Beleidsdoel, BeleidsdoelCreate, BeleidsdoelUpdate]):
    def get(self, uuid: str) -> Beleidsdoel:
        return (
            self.db.query(self.model)
            .options(
                joinedload(Beleidsdoel.Beleidskeuzes),
            )
            .filter(self.model.UUID == uuid)
            .one()
        )


beleidsdoel = CRUDBeleidsdoel(Beleidsdoel)
