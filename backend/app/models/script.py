from sqlalchemy import String, Column
from app.db.base_class import Base
from app.models.common import DecamelizeTableNameMixin, ModelMixin


class ScriptWorker(DecamelizeTableNameMixin, Base, ModelMixin):
    """
    Model for accounting for scripts processing
    """
    script = Column(String(255))

    def __repr__(self):
        """
        For admin
        :return:
        """
        return self.script
