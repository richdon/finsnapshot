USER (
    user_id: SERIAL PK,
    full_name: TEXT NOT NULL,
    email: TEXT UNIQUE NOT NULL,
    password_hash: TEXT NOT NULL,
    cash_balance: NUMERIC,
    created_at: DATE
)

INCOME (
    income_id: SERIAL PK,
    income_type: TEXT,              -- CHECK: salary, hourly
    amount: NUMERIC,
    frequency: TEXT,                -- CHECK: weekly, biweekly, monthly
    user_id: INT FK
)

HOLDINGS (
    holding_id: SERIAL PK,
    ticker: TEXT NOT NULL,
    quantity: NUMERIC,
    holding_type: TEXT,             -- CHECK: stock, crypto
    user_id: INT FK
)

EXPENSES (
    expense_id: SERIAL PK,
    name: TEXT NOT NULL,
    amount: NUMERIC,
    frequency: TEXT,                -- CHECK: weekly, biweekly, monthly
    user_id: INT FK
)

GOAL (
    goal_id: SERIAL PK,
    name: TEXT NOT NULL,
    target_amount: NUMERIC,
    contribution_amount: NUMERIC,   -- how much per period (stored)
    contributed_amount: NUMERIC,    -- user manually updates (stored)
    frequency: TEXT,                -- CHECK: weekly, biweekly, monthly
    start_date: DATE,
    target_date: DATE,
    user_id: INT FK
)