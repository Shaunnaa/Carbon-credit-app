# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# import login_register
# import order
# from fastapi import Request
# from fastapi.templating import Jinja2Templates
# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:8000"
#     "http://localhost:8080",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# app.include_router(login_register.app)
# app.include_router(order.app)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# templates = Jinja2Templates(directory="templates")
# # Mount a directory to serve static files like CSS and JS


# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("test.html", {"request": request})


import login_register
import order
from fastapi import FastAPI, Depends, HTTPException, Form, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

# Add CORS Middleware to allow requests from all origins. Adjust the list of allowed origins according to your needs.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(login_register.app)
app.include_router(order.app)


@app.get("/")
async def root():
    return {"message": "Hello World"}
