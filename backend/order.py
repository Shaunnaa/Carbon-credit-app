from fastapi import APIRouter
import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas

app = _fastapi.FastAPI()

app = APIRouter(
    prefix="/order",
    tags=["order"],
    responses={404: {"message": "Not found"}}
)

@app.put("/order/new_order", status_code=200)
async def order_happend(sent_id: int, recive_id: int, amount_cc: str, user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db),):
     await _services.sent_cc(sent_id,amount_cc,user,db)
     await _services.recive_cc(recive_id,amount_cc,user,db)
     return "complete tranfers"

@app.post("/create_history", response_model=_schemas.History)
async def create_history(histoty: _schemas.HistoryCreate, user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db)):
     await _services.history(history=histoty, user=user, db=db)
     return "create success"

@app.get("/history", response_model=list[_schemas.History])
async def get_history(user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db)):
     return await _services.get_history(user=user, db=db)

@app.delete("/delete_history")
async def delete_history(id: int ,user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db)):
    await _services.history(id ,user, db)
    return {"message", "Successfully Deleted"}