# FinSnapshot API Routes

## Base URL
```
http://localhost:8000/api/v1
```

## Authentication
All protected routes require a JWT token in the request header:
```
Authorization: Bearer <token>
```

---

## Auth Routes
> No token required

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/register | Register a new account |
| POST | /auth/login | Login and receive JWT token |

### POST /auth/register
**Request Body:**
```json
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "password": "plaintext_password"
}
```
**Response:**
```json
{
  "user_id": 1,
  "full_name": "John Doe",
  "email": "john@example.com"
}
```

### POST /auth/login
**Request Body:**
```json
{
  "email": "john@example.com",
  "password": "plaintext_password"
}
```
**Response:**
```json
{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}
```

---

## User Routes
> Token required

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /user/me | Get current user details |
| PATCH  | /user/me | Update user details (name, email, cash_balance) |

### GET /user/me
**Response:**
```json
{
  "user_id": 1,
  "full_name": "John Doe",
  "email": "john@example.com",
  "cash_balance": 5000.00,
  "created_at": "2025-01-01"
}
```

### PATCH /user/me
**Request Body** (any updatable field):
```json
{
  "cash_balance": 6000.00
}
```

---

## Income Routes
> Token required

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /income | Get income details for current user |
| POST   | /income | Create an income record |
| PATCH  | /income/{income_id} | Update an income record |

### GET /income
**Response:**
```json
{
  "income_id": 1,
  "income_type": "salary",
  "amount": 5000.00,
  "frequency": "monthly"
}
```

### POST /income
**Request Body:**
```json
{
  "income_type": "salary",
  "amount": 5000.00,
  "frequency": "monthly"
}
```

### PATCH /income/{income_id}
**Request Body** (any updatable field):
```json
{
  "amount": 5500.00
}
```

---

## Holdings Routes
> Token required

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /holdings | Get all holdings for current user (with live prices) |
| POST   | /holdings | Add a new holding |
| PATCH  | /holdings/{holding_id} | Update a holding |
| DELETE | /holdings/{holding_id} | Remove a holding |

### GET /holdings
**Response:**
```json
[
  {
    "holding_id": 1,
    "ticker": "AAPL",
    "quantity": 10,
    "holding_type": "stock",
    "current_price": 195.00,
    "total_value": 1950.00
  },
  {
    "holding_id": 2,
    "ticker": "BTC",
    "quantity": 0.5,
    "holding_type": "crypto",
    "current_price": 82000.00,
    "total_value": 41000.00
  }
]
```
> Note: `current_price` and `total_value` are not stored in DB — they are fetched from yfinance/CoinGecko at request time.

### POST /holdings
**Request Body:**
```json
{
  "ticker": "AAPL",
  "quantity": 10,
  "holding_type": "stock"
}
```

### PATCH /holdings/{holding_id}
**Request Body** (any updatable field):
```json
{
  "quantity": 15
}
```

---

## Expenses Routes
> Token required

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /expenses | Get all expenses for current user |
| POST   | /expenses | Add an expense |
| PATCH  | /expenses/{expense_id} | Update an expense |
| DELETE | /expenses/{expense_id} | Delete an expense |

### GET /expenses
**Response:**
```json
[
  {
    "expense_id": 1,
    "name": "Rent",
    "amount": 1500.00,
    "frequency": "monthly"
  },
  {
    "expense_id": 2,
    "name": "Netflix",
    "amount": 15.99,
    "frequency": "monthly"
  }
]
```

### POST /expenses
**Request Body:**
```json
{
  "name": "Rent",
  "amount": 1500.00,
  "frequency": "monthly"
}
```

### PATCH /expenses/{expense_id}
**Request Body** (any updatable field):
```json
{
  "amount": 1600.00
}
```

---

## Goal Routes
> Token required

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /goals | Get all goals for current user |
| POST   | /goals | Create a new goal |
| PATCH  | /goals/{goal_id} | Update a goal |
| DELETE | /goals/{goal_id} | Delete a goal |

### GET /goals
**Response:**
```json
[
  {
    "goal_id": 1,
    "name": "New Car",
    "target_amount": 10000.00,
    "contribution_amount": 500.00,
    "contributed_amount": 1500.00,
    "frequency": "monthly",
    "start_date": "2025-01-01",
    "target_date": "2025-12-01",
    "expected_amount": 2000.00     
  }
]
```
> Note: `expected_amount` is calculated in the backend — not stored in DB.
> Formula: `contribution_amount × periods_elapsed`

### POST /goals
**Request Body:**
```json
{
  "name": "New Car",
  "target_amount": 10000.00,
  "contribution_amount": 500.00,
  "frequency": "monthly",
  "start_date": "2025-01-01",
  "target_date": "2025-12-01"
}
```

### PATCH /goals/{goal_id}
**Request Body** (any updatable field):
```json
{
  "contributed_amount": 2000.00
}
```

---

## Dashboard Route
> Token required

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /dashboard | Returns full financial snapshot for current user |

### GET /dashboard
**Response:**
```json
{
  "net_worth": {
    "cash_balance": 5000.00,
    "holdings_value": 42950.00,
    "total": 47950.00
  },
  "budget": {
    "monthly_income": 5000.00,
    "monthly_expenses": 2000.00,
    "surplus": 3000.00
  },
  "goals": [
    {
      "goal_id": 1,
      "name": "New Car",
      "target_amount": 10000.00,
      "contributed_amount": 1500.00,
      "expected_amount": 2000.00,
      "difference": -500.00,
      "target_date": "2025-12-01"
    }
  ]
}
```
> Note: This route aggregates data from USER, INCOME, HOLDINGS, EXPENSES, and GOAL tables in a single response.

---

## Route Structure Reference
```
POST   → Create
GET    → Read
PATCH  → Update (partial)
DELETE → Delete
```

## HTTP Status Codes
```
200 OK           → Successful GET / PATCH
201 Created      → Successful POST
204 No Content   → Successful DELETE
400 Bad Request  → Invalid input
401 Unauthorized → Missing or invalid token
404 Not Found    → Resource does not exist
500 Server Error → Something went wrong
```