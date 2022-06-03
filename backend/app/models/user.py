from sqlalchemy import Boolean, Column, String

from .common import PrimaryKeyMixin, CreatedMixin, UpdatedMixin
from app.db.base_class import Base


class User(PrimaryKeyMixin, Base, CreatedMixin, UpdatedMixin):
    email = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password = Column(String(length=72), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def __repr__(self):
        return self.email
