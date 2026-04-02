finsnapshot/
├── backend/
│   └── app/
│       ├── main.py                  -- FastAPI app entry point, registers all routes
│       ├── routes/
│       │   ├── auth.py
│       │   ├── user.py
│       │   ├── income.py
│       │   ├── holdings.py
│       │   ├── expenses.py
│       │   ├── goals.py
│       │   └── dashboard.py
│       ├── schemas/
│       │   ├── user.py              -- request/response shapes for each route
│       │   ├── income.py
│       │   ├── holdings.py
│       │   ├── expenses.py
│       │   └── goals.py
│       ├── database/
│       │   ├── session.py           -- DB connection and session management
│       │   └── db_models/
│       │       ├── user.py          -- one file per table
│       │       ├── income.py
│       │       ├── holdings.py
│       │       ├── expenses.py
│       │       └── goals.py
│       ├── services/
│       │   ├── auth_service.py      -- password hashing, token generation
│       │   ├── income_service.py
│       │   ├── holdings_service.py  -- calls yfinance/CoinGecko here
│       │   ├── expenses_service.py
│       │   ├── goals_service.py     -- calculates expected_amount here
│       │   └── dashboard_service.py -- aggregates all data for dashboard
│       ├── middleware/
│       │   └── auth.py              -- JWT token validation on protected routes
│       ├── config/
│       │   └── settings.py          -- loads values from .env (not connection_strings.py)
│       └── utils/
│           └── helpers.py           -- shared utility functions
│
├── frontend/
│   └── src/
│       ├── pages/
│       │   ├── Login.jsx
│       │   ├── Register.jsx         -- was missing, needed for /auth/register
│       │   ├── Dashboard.jsx        -- main home screen
│       │   └── Onboarding.jsx       -- first time setup: income, holdings, expenses
│       ├── components/
│       │   ├── NetWorthCard.jsx     -- shows total net worth
│       │   ├── BudgetSummary.jsx    -- shows income vs expenses
│       │   ├── HoldingsList.jsx     -- lists stocks and crypto with live prices
│       │   ├── ExpensesList.jsx     -- lists recurring expenses
│       │   ├── GoalCard.jsx         -- shows goal progress
│       │   ├── AddHoldingForm.jsx   -- reusable form for adding a holding
│       │   ├── AddExpenseForm.jsx   -- reusable form for adding an expense
│       │   └── Navbar.jsx
│       ├── services/
│       │   ├── api.js               -- base axios/fetch instance with base URL + auth header
│       │   ├── authService.js       -- calls /auth/register and /auth/login
│       │   ├── userService.js       -- calls /user/me
│       │   ├── incomeService.js     -- calls /income routes
│       │   ├── holdingsService.js   -- calls /holdings routes
│       │   ├── expensesService.js   -- calls /expenses routes
│       │   ├── goalsService.js      -- calls /goals routes
│       │   └── dashboardService.js  -- calls /dashboard
│       ├── context/
│       │   └── AuthContext.jsx      -- stores JWT token, current user, login/logout functions
│       └── utils/
│           ├── formatCurrency.js    -- formats numbers as $1,000.00
│           └── dateHelpers.js       -- calculates periods elapsed for goal expected_amount
│
├── .gitignore
├── .env
└── docker-compose.yml