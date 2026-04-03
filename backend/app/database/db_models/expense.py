from decimal import Decimal

from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from . import Base, Frequency

class Expense(Base):
    __tablename__ = 'expenses'
    expense_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    amount: Mapped[Decimal]
    frequency: Mapped[Frequency] = mapped_column(Enum(Frequency))    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
