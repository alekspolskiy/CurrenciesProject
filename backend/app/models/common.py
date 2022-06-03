import uuid
import humps
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declared_attr

from app.db.sqlalchemy import GUID


class PrimaryKeyMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)
    unique_id = Column(GUID, unique=True, default=uuid.uuid4)


class CreatedMixin:
    dt_create = Column(DateTime, default=datetime.utcnow)


class UpdatedMixin:
    dt_update = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class ModelMixin(PrimaryKeyMixin, CreatedMixin, UpdatedMixin):
    pass


class DecamelizeTableNameMixin:
    @declared_attr
    def __tablename__(cls) -> str:
        return humps.decamelize(cls.__name__)
