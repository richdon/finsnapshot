from decimal import Decimal
from sqlalchemy import ForeignKey, Enum 
from sqlalchemy.orm import Mapped, mapped_column
from . import Base, IncomeType, Frequency

class Income(Base):
    __tablename__ = 'income'
    income_id: Mapped[int] = mapped_column(primary_key=True)
    income_type: Mapped[IncomeType] = mapped_column(Enum(IncomeType))    
    amount: Mapped[Decimal]
    frequency: Mapped[Frequency] = mapped_column(Enum(Frequency))    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
