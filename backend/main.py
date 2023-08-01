from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import login_register
import order
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
<<<<<<< HEAD
=======

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


>>>>>>> 8704f2327cf3497b77a81e82354daeac889660aa
app.include_router(login_register.app)
app.include_router(order.app)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
# Mount a directory to serve static files like CSS and JS


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})