from sqlalchemy import Column, String, Float, Integer, ForeignKey, select, func, desc
from sqlalchemy.orm import relationship, column_property
from sqlalchemy.ext.hybrid import hybrid_property
from app.db.base_class import Base
from app.models.common import DecamelizeTableNameMixin, ModelMixin


class CurrencyPriceHistory(DecamelizeTableNameMixin, ModelMixin, Base):
    currency_id = Column(Integer, ForeignKey("currency.id", ondelete="SET NULL"), nullable=False)
    currency = relationship("Currency", foreign_keys=[currency_id], backref='prices', lazy='subquery')
    price = Column(Float(8, asdecimal=True, decimal_return_scale=2))

    @hybrid_property
    def currency_name(self):
        return self.currency.name

    @currency_name.expression
    def currency_name(cls):
        return select([Currency.name]).where(Currency.id == cls.currency_id).label('currency_name')

    @hybrid_property
    def currency_iso(self):
        return self.currency.iso

    @currency_iso.expression
    def currency_iso(cls):
        return select([Currency.iso]).where(Currency.id == cls.currency_id).label('currency_iso')

    def __repr__(self):
        return self.currency


class Currency(DecamelizeTableNameMixin, ModelMixin, Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    iso = Column(String(5))
    price = Column(Float(8, asdecimal=True, decimal_return_scale=2), default=0)

    actual_price = column_property(select([CurrencyPriceHistory.price]).where(
        CurrencyPriceHistory.currency_id == id
    ).order_by(desc(CurrencyPriceHistory.dt_create)).correlate_except(CurrencyPriceHistory).limit(1))

    def __repr__(self):
        return self.iso
