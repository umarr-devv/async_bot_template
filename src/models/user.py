from datetime import datetime

from sqlalchemy import (Date, Integer)
from sqlalchemy.orm import mapped_column, Mapped

from src.service.database import Base
from src.utils.funcs import current_utc_time


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    created_on: Mapped[datetime] = mapped_column(Date, default=current_utc_time)
    updated_on: Mapped[datetime] = mapped_column(Date, default=current_utc_time,
                                                 onupdate=current_utc_time)
