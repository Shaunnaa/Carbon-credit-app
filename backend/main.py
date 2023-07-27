from fastapi import FastAPI
import login_register
import order

app = FastAPI()

app.include_router(login_register.app)
app.include_router(order.app)

@app.get("/")
async def root():
    return {"message": "Hello World"}