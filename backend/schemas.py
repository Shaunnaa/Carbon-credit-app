import datetime as _dt

import pydantic as _pydantic


class _UserBase(_pydantic.BaseModel):
    email: str


class UserCreate(_UserBase):
    hashed_password: str

    class Config:
        orm_mode = True


class User(_UserBase):
    id: int

    class Config:
        orm_mode = True


class _InformationBase(_pydantic.BaseModel):
    name: str
    phone: str
    type_acc: str
    


class InformationCreate(_InformationBase):
    pass


class Information(_InformationBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime
    class Config:
        orm_mode = True


class _AddressBase(_pydantic.BaseModel):
    # number: str
    # moo: int
    # building: str
    # alley: str
    # road: str
    # sub_district: str
    # district: str
    # province: str
    address: str
    post_code: str


class AddressCreate(_AddressBase):
    pass


class Address(_AddressBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class _HistoryBase(_pydantic.BaseModel):
    sent_id: int
    reciver_id: int
    cc_tranfers: float
    tranfer_type: str

class HistoryCreate(_HistoryBase):
    pass

class History(_HistoryBase):
    id: int
    owner_id: int
    date_tranfer: _dt.datetime

    class Config:
        orm_mode = True

class _CarbonBase(_pydantic.BaseModel):
    carbon_cc: str

class Carboon_CCCreate(_CarbonBase):
    pass

class Carbon_CC(_CarbonBase):
    id: int
    owner_id: int
    date_update: _dt.datetime

    class Config:
        orm_mode = True

