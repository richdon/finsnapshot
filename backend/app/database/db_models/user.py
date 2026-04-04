from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

from . import Base

class User(Base):
    __tablename__ = 'users'
    user_id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] 
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    cash_balance: Mapped[float | None]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
