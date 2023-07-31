import fastapi as _fastapi
import fastapi.security as _security
import jwt as _jwt
import datetime as _dt
import sqlalchemy.orm as _orm
import passlib.hash as _hash
import models as _models
import database as _database, schemas as _schemas
# , models_lo as _models
oauth2schema = _security.OAuth2PasswordBearer(tokenUrl="/login_register/api/token") # if change the url of the code change it!!!!

JWT_SECRET = "myjwtsecret"


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_user_by_email(email: str, db: _orm.Session):
    return db.query(_models.User).filter(_models.User.email == email).first()


async def create_user(user: _schemas.UserCreate, db: _orm.Session):
    user_obj = _models.User(
        email=user.email, hashed_password=_hash.bcrypt.hash(user.hashed_password)
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


async def authenticate_user(email: str, password: str, db: _orm.Session):
    user = await get_user_by_email(db=db, email=email)

    if not user:
        return False

    if not user.verify_password(password):
        return False

    return user


async def create_token(user: _models.User):
    user_obj = _schemas.User.from_orm(user)

    token = _jwt.encode(user_obj.dict(), JWT_SECRET)

    return dict(access_token=token, token_type="bearer")


async def get_current_user(
    db: _orm.Session = _fastapi.Depends(get_db),
    token: str = _fastapi.Depends(oauth2schema),
):
    try:
        payload = _jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = db.query(_models.User).get(payload["id"])
    except:
        raise _fastapi.HTTPException(
            status_code=401, detail="Invalid Email or Password"
        )

    return _schemas.User.from_orm(user)


async def create_information(user: _schemas.User, db: _orm.Session, information: _schemas.InformationCreate):
    info = await get_information(user,db)
    
    if (info):
        return "already have account"
    
    information = _models.Information(**information.dict(), owner_id=user.id)
    db.add(information)
    db.commit()
    db.refresh(information)

    return _schemas.Information.from_orm(information)


async def get_information(user: _schemas.User, db: _orm.Session):
    leads = db.query(_models.Information).filter_by(owner_id=user.id).filter(_models.Information.id == user.id).first()

    return leads

async def update_information(information: _schemas.InformationCreate, user: _schemas.User, db: _orm.Session):
    info_db = await get_information(user, db)

    info_db.name = information.name
    info_db.phone = information.phone
    info_db.type_acc = "none"

    db.commit()
    db.refresh(info_db)
    return _schemas.Information.from_orm(info_db)

async def create_adderss(user: _schemas.User, db: _orm.Session, address: _schemas.AddressCreate):
    address = _models.Address(**address.dict(), owner_id=user.id)
    db.add(address)
    db.commit()
    db.refresh(address)

    if (address) is None:
        raise _fastapi.HTTPException(status_code=404,detail="something error")
    
    return _schemas.Address.from_orm(address)

async def get_adderss(user: _schemas.User, db: _orm.Session):
    leads = db.query(_models.Address).filter_by(owner_id=user.id).filter(_models.Address.id == user.id).first()
    return leads
    # return list(map(_schemas.Address.from_orm, leads))

async def update_type(type: str, user: _schemas.User, db: _orm.Session):
    infor_db = await get_information(user, db)

    infor_db.type_acc = type

    db.commit()
    db.refresh(infor_db)
    return _schemas.Information.from_orm(infor_db)

async def create_carbon_cc(user: _schemas.User, db: _orm.Session, carbon_cc: _schemas.Carboon_CCCreate):
    carbon_cc = _models.Carbon_CC(**carbon_cc.dict(), owner_id=user.id)
    db.add(carbon_cc)
    db.commit()
    db.refresh(carbon_cc)

    return _schemas.Carbon_CC.from_orm(carbon_cc)

async def get_carbon_cc(user: _schemas.User, db: _orm.Session):
    leads = db.query(_models.Carbon_CC).filter_by(owner_id=user.id).filter(_models.Carbon_CC.id == user.id).first()

    return leads

async def get_carbon_cc_id(id: int,user: _schemas.User, db: _orm.Session):
    leads = db.query(_models.Carbon_CC).filter(_models.Carbon_CC.id == id).first()

    return leads

async def update_carbon(amount: str, user: _schemas.User, db: _orm.Session):
    cc = await get_carbon_cc(user, db)

    cc.carbon_cc = amount
    cc.date_updated = _dt.datetime.utcnow()

    db.commit()
    db.refresh(cc)
    # return "complete"
    return _schemas.Carbon_CC.from_orm(cc)

async def update_carbon_id(id: int, amount: str, user: _schemas.User, db: _orm.Session):
    cc = await get_carbon_cc_id(id,user, db)

    cc.carbon_cc = amount
    cc.date_updated = _dt.datetime.utcnow()

    db.commit()
    db.refresh(cc)
    return "complete"
    # return _schemas.Carbon_CC.from_orm(cc)

async def delete_address(user: _schemas.User, db: _orm.Session):
    add_db = await get_adderss(user, db)

    db.delete(add_db)
    db.refresh(add_db)
    # return _schemas.Address.from_orm(add_db)
    
async def delete_information(user: _schemas.User, db: _orm.Session):
    infor_db = await get_information(user, db)

    db.delete(infor_db)
    db.refresh(infor_db)
    return _schemas.Information.from_orm(infor_db)

async def delete_carbon_cc(id: int, user: _schemas.User, db: _orm.Session):
    cc_db = await get_carbon_cc_id(id,user, db)

    db.delete(cc_db)
    db.refresh(cc_db)
    return _schemas.Carbon_CC.from_orm(cc_db)

async def sent_cc(sent_id: int,amount: str, user: _schemas.User, db: _orm.Session):
    amount_cc = await get_carbon_cc_id(sent_id,user,db)  
    now_cc = float(amount_cc.carbon_cc)
    cut_cc = float(amount)

    update_cc = now_cc - cut_cc

    update_cc = str(update_cc)
    await update_carbon_id(sent_id,update_cc,user,db)   
    return "update f'{update_cc}"

async def recive_cc(recive_id: int,amount: str, user: _schemas.User, db: _orm.Session):
    amount_cc = await get_carbon_cc_id(recive_id,user,db)  
    now_cc = float(amount_cc.carbon_cc)
    add_cc = float(amount)

    update_cc = now_cc + add_cc

    update_cc = str(update_cc)
    await update_carbon_id(recive_id,update_cc,user,db)   
    return "update f'{update_cc}"

async def history(history: _schemas.History, user: _schemas.User, db: _orm.Session):
    history = _models.History(**history.dict(), owner_id=user.id)
    db.add(history)
    db.commit()
    db.refresh(history)

    return _schemas.History.from_orm(history)

async def get_history(user: _schemas.User, db: _orm.Session):
    leads = db.query(_models.History).filter_by(owner_id=user.id)
    # return leads
    return list(map(_schemas.History.from_orm, leads))

async def get_history_id(id: int, user: _schemas.User, db: _orm.Session):
    leads = db.query(_models.History).filter_by(owner_id=user.id).filter(_models.History.id == id).first()
    return leads
    # return list(map(_schemas.History.from_orm, leads))

async def delete_history(id: int, user: _schemas.User, db: _orm.Session):
    cc_db = await get_history_id(id,user, db)

    db.delete(cc_db)
    db.refresh(cc_db)
    return _schemas.History.from_orm(cc_db)