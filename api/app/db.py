from sqlmodel import Session, SQLModel, create_engine

from app.config import settings

engine = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    echo=settings.ENVIRONMENT == "development",
    pool_pre_ping=True,  
    pool_size=5,  
    max_overflow=10,
)

def init_db() -> None:
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session