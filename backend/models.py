import datetime as _dt


import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as _hash

import database as _database


class User(_database.Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    hashed_password = _sql.Column(_sql.String)
    
    address = _orm.relationship("Address", back_populates="owner")
    informations = _orm.relationship("Information", back_populates="owner")
    historys = _orm.relationship("History", back_populates="owner")
    carbon_ccs = _orm.relationship("Carbon_CC", back_populates="owner")
    def verify_password(self, password: str):
       return _hash.bcrypt.verify(password, self.hashed_password)




class Information(_database.Base):
    __tablename__ = "informations"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    name = _sql.Column(_sql.String, index=True)
    phone = _sql.Column(_sql.String, index=True, default="")
    type_acc = _sql.Column(_sql.String, index=True, default="none")
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)


    owner = _orm.relationship("User", back_populates="informations")


class Address(_database.Base):
    __tablename__ = "address"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    # number = _sql.Column(_sql.String, index=True)
    # moo = _sql.Column(_sql.Integer, index=True)
    # building = _sql.Column(_sql.String, index=True)
    # alley = _sql.Column(_sql.String, index=True)
    # road = _sql.Column(_sql.String, index=True)
    # sub_district = _sql.Column(_sql.String, index=True)
    # district = _sql.Column(_sql.String, index=True)
    # province = _sql.Column(_sql.String, index=True)
    address = _sql.Column(_sql.String, index=True)
    post_code = _sql.Column(_sql.String, index=True)

    owner = _orm.relationship("User", back_populates="address")


class History(_database.Base):
    __tablename__ = "historys"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    sent_id = _sql.Column(_sql.Integer, index=True)
    reciver_id = _sql.Column(_sql.Integer, index=True)
    cc_tranfers = _sql.Column(_sql.Float, index=True, default="0.00")
    tranfer_type = _sql.Column(_sql.String, index=True)
    date_tranfer = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    owner = _orm.relationship("User", back_populates="historys")

class Carbon_CC(_database.Base):
    __tablename__ = "carbon_ccs"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    carbon_cc = _sql.Column(_sql.String, index=True, default="0.00")
    date_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    owner = _orm.relationship("User", back_populates="carbon_ccs")
