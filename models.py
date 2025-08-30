from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL="sqlite:///company.db"


engine = create_engine(DATABASE_URL, echo=True)


Base = declarative_base()


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)



