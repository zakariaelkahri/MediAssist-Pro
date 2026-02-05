from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Import all models here so they are registered with Base
from app.models.user import User  # noqa
from app.models.query import Query  # noqa