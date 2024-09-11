from datetime import datetime

from sqlalchemy import (BigInteger, Column, Date, Integer, Sequence)

from src.service.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('id'))
    user_id = Column(BigInteger, primary_key=True)
    created_on = Column(Date, default=datetime.now)
    update_on = Column(Date, default=datetime.now, onupdate=datetime.now)
