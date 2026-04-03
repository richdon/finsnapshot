from decimal import Decimal
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from . import Base, HoldingType

class Holding(Base):
    __tablename__ = 'holdings'
    holding_id: Mapped[int] = mapped_column(primary_key=True)
    ticker: Mapped[str]
    quantity: Mapped[Decimal]
    holding_type: Mapped[HoldingType] = mapped_column(Enum(HoldingType))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
