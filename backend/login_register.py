from fastapi import APIRouter
from typing import List
import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = _fastapi.FastAPI()

app = APIRouter(
    prefix="/login_register",
    tags=["login_register"],
    responses={404: {"message": "Not found"}}
)
# if have change in url go and change the token url !!!!!!

@app.post("/api/users")
async def create_user(
    user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db),email: str = _fastapi.Form(...), password: str = _fastapi.Form(...)
):
    user.email = email
    user.hashed_password = password
    db_user = await _services.get_user_by_email(user.email, db)
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="Email already in use")

    user = await _services.create_user(user, db)

    return await _services.create_token(user)

@app.post("/api/token")
async def generate_token(form_data: _security.OAuth2PasswordRequestForm = _fastapi.Depends(), db: _orm.Session = _fastapi.Depends(_services.get_db),username: str = _fastapi.Form(...) , password: str = _fastapi.Form(...)):
    form_data.username = username
    form_data.password = password
    user = await _services.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise _fastapi.HTTPException(status_code=401,detail="Invalid Credentials")
    
    return await _services.create_token(user)

@app.get("/api/users/me", response_model=_schemas.User)
async def get_user(user: _schemas.User = _fastapi.Depends(_services.get_current_user)):
    return user

@app.post("/api/information", response_model=_schemas.Information)
async def create_information(
        information: _schemas.InformationCreate, user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db),name: str = _fastapi.Form(...),phone: str = _fastapi.Form(...)
):
    information.name = name
    information.phone = phone
    information.type_acc = "none"
    return await _services.create_information(user=user, db=db, information=information)

@app.get("/api/information", status_code=200) 
async def get_information(user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_information(user=user, db=db)

@app.put("/api/update_information", status_code=200)
async def update_information(information: _schemas.InformationCreate, user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db),name: str = _fastapi.Form(...),phone: str = _fastapi.Form(...)):
    information.name = name
    information.phone = phone
    await _services.update_information(information, user, db)
    return {"message", "Successfully Updated"}

@app.put("/api/update_type", status_code=200)
async def update_type( user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db), type: str = _fastapi.Form(...)):
    await _services.update_type(type, user, db)
    return {"message", "Successfully Updated"}

@app.post("/api/carbon_cc", response_model=_schemas.Carbon_CC)
async def create_carbon_cc(
        carbon_cc: _schemas.Carboon_CCCreate, user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    carbon_cc.carbon_cc = "0"
    return await _services.create_carbon_cc(user=user, db=db, carbon_cc=carbon_cc)

@app.get("/api/get_now_cc", status_code=200)
async def get_carbon_cc(user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_carbon_cc(user=user, db=db)

@app.get("/api/get_now_cc_id", status_code=200)
async def get_carbon_cc_id(id: int, user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_carbon_cc_id(id=id, user=user, db=db)

@app.put("/api/carbon_cc_update/{amount}")
async def update_carbon_cc(
        amount: str,
        user: _schemas.User = _fastapi.Depends(_services.get_current_user), 
        db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    await _services.update_carbon(amount, user, db)
    return {"message", "Successfully Updated"}

@app.post("/api/create_address", response_model=_schemas.Address)
async def create_address(address: _schemas.AddressCreate, user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.create_adderss(user=user, db=db, address=address)

@app.get("/api/address", status_code=200)
async def get_adderss(user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_adderss(user=user, db=db)

@app.delete("/delete/address", status_code=204)
async def delete_address(user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db)):
    await _services.delete_address(user, db)
    return {"message", "Successfully Deleted"}

@app.delete("/delete/inforamtion", status_code=204)
async def delete_information(user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db)):
    await _services.delete_information(user, db)
    return {"message", "Successfully Deleted"}

@app.delete("/delete/carbon_cc", status_code=204)
async def delete_carbon_cc(id: int ,user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db)):
    await _services.delete_carbon_cc(id ,user, db)
    return {"message", "Successfully Deleted"}

@app.get("/api")
async def root():
    return {"message": "Register and Login"}
