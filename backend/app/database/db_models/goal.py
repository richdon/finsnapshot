from datetime import date
from decimal import Decimal

from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from . import Base, Frequency

class Goal(Base):
    __tablename__ = 'goals'
    goal_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    target_amount: Mapped[Decimal]
    contribution_amount: Mapped[Decimal]
    contributed_amount: Mapped[Decimal]
    start_date: Mapped[date]
    target_date: Mapped[date]
    frequency: Mapped[Frequency] = mapped_column(Enum(Frequency))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
