from fastapi import FastAPI
from core.config import API_PREFIX
from routers import auth_router, user_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router, prefix=API_PREFIX)
app.include_router(auth_router.router, prefix=API_PREFIX)


@app.get("/")
def read_root():
    return {"message": "Welcome to FestSpot Plus!"}
