# FinSnapshot

> A personal finance dashboard for users who want a clear picture of their financial standing and track progress towards savings goals.

---

## Who is it for?
Users who want to:
- Understand their current net worth across income, holdings, and cash
- Track recurring expenses and plan a budget
- Set savings goals and see a realistic timeline to achieve them

---

## What can users do?
- Log in / create an account
- Enter income type (salary or hourly) + amount
- Add financial holdings (stocks, crypto, cash)
- View live stock and crypto prices/values via external API
- Add and manage recurring expenses
- Add non-recurring expenses
- Define a savings goal with a target amount and date

---

## What users see (Dashboard)
After entering income, holdings, and expenses, users see:

- **Net Worth** — total value of holdings (stocks + crypto + cash)
  - Net Worth = Assets (stocks + crypto + cash) — this is your snapshot of what you own
  - Budget Surplus = Income - Recurring Expenses — this is separate, showing monthly cash flow
  - These are two distinct numbers. Expenses are not subtracted from net worth.
- **Budget Summary** — income minus recurring expenses for the period
- **Savings Goal Section** — funds set aside towards goal, separate from net worth calculation
  - Time needed counter to reach goal based on current surplus
- **Breakdown option** — view how net worth is calculated
- Option to add/edit/remove recurring expenses
- Option to add a non-recurring expense
- Option to add/update savings goal

---

## Savings Goal Breakdown
When a user sets a savings goal:
- Enter goal name, target amount, and target date
- App calculates how much needs to be set aside per month
- Funds towards the goal are tracked separately from net worth
- Dashboard shows current progress and estimated time to completion
- If current surplus is less than required, a shortfall is displayed

---

## Out of Scope (v1)
- Connecting to any actual financial institution (e.g. Plaid)
- 30-day net worth graph
- Breakdown of holdings by individual asset class (cash/stock/crypto)
- Tracking buy/sell transactions for holdings
- Mobile app

---

## Tech Stack
| Layer | Technology |
|---|---|
| Frontend | React (JSX) |
| Backend | Python / FastAPI |
| Database | PostgreSQL |
| Auth | JWT — Secret key stored in `.env` file on the server (never in DB or frontend). Frontend stores the token in memory or httpOnly cookie. |
| Stock Prices | `yfinance` (Python library) — unofficial but actively maintained, free, good for learning projects. Note: not for production use as it can break if Yahoo changes their site structure. |
| Crypto Prices | CoinGecko API — fully free, no API key required for basic use, more stable than yfinance for crypto |

---

## Data Model
USER (
    user_id: SERIAL PK,
    full_name: TEXT NOT NULL,
    email: TEXT UNIQUE NOT NULL,
    password_hash: TEXT NOT NULL,
    cash_balance: NUMERIC,
    created_at: DATE,
)

INCOME (
    income_id: SERIAL PK,
    income_type: TEXT,              -- CHECK: salary, hourly
    amount: NUMERIC,
    frequency: TEXT,                -- CHECK: weekly, biweekly, monthly
    next_pay_date: DATE,
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
    is_recurring: BOOLEAN NOT NULL,
    frequency: TEXT NULL,           -- CHECK: weekly, biweekly, monthly | null if one-time
    next_due_date: DATE NULL,       -- null if one-time
    amount: NUMERIC,
    user_id: INT FK
)

GOAL (
    goal_id: SERIAL PK,
    name: TEXT NOT NULL,
    target_amount: NUMERIC,
    start_date: DATE,
    target_date: DATE,
    contribution_amount: NUMERIC,   -- amount per period (stored)
    contributed_amount: NUMERIC,    -- what user actually put away (stored)
    frequency: TEXT,                -- CHECK: weekly, biweekly, monthly
    user_id: INT FK
)

---

## API Routes
⚠️ TODO: Define endpoints

Think about: which routes require authentication and which don't?

---

## Getting Started

### Prerequisites
⚠️ TODO

### Installation
⚠️ TODO

### Running Locally
⚠️ TODO

---

## Roadmap (v2 Ideas)
- 30-day net worth graph in daily intervals
- Breakdown of graph by individual asset class
- Update holdings (e.g. user bought/sold stock)
- AI-powered budget recommendations to hit savings goals faster
- Bank integration (Plaid)

