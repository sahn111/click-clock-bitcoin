from code import interact
import json
from typing import Any, Dict, Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Time, Date, Integer
from ..base import Base
from ..helper import OrmHelper
from datetime import time, date

JSONObject = Dict[str, Any]

class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "btc"}

    email = Column(String, primary_key=True)
    phone = Column(String, primary_key=True)
    pin = Column(String)

    def __repr__(self) -> str:
        return json.dumps(self.dict())
    def __str__(self) -> str:
        return json.dumps(self.dict())
    def dict(self) -> dict:
        return OrmHelper.toDict(self)

class ServicePydantic(BaseModel):
    email : Optional[str]
    phone : Optional[str]
    pin : Optional[str]

    class Config:
        orm_mode = True
