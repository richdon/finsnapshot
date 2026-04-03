from enum import StrEnum

class HoldingType(StrEnum):
    STOCK = 'stock'
    CRYPTO = 'crypto'

class Frequency(StrEnum):
    WEEKLY = 'weekly'
    BIWEEKLY = 'biweekly'
    MONTHLY = 'monthly'

class IncomeType(StrEnum):
    SALARY = 'salary'
    HOURLY = 'houlry'