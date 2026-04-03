from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from .enums import Frequency, IncomeType, HoldingType
from .user import User
from .income import Income
from .holding import Holding
from .expense import Expense
from .goal import Goal

