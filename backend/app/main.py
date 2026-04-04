from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import router as auth_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)

@app.get("/")
async def health_check():
    return {"status": "ok"}

from middleware.auth import get_current_user
from database.db_models import User

@app.get("/protected-test")
def protected_test(current_user: User = Depends(get_current_user)):
    return {"message": f"hello {current_user.email}"}