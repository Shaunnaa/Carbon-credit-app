from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import login_register
import order

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000"
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(login_register.app)
app.include_router(order.app)

@app.get("/")
async def root():
    return {"message": "Hello World"}