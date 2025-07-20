from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Modellerimizi buraya import ediyoruz ki Alembic onları tanısın
