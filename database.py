from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# sqlite
# DATABASE_URL = "sqlite:///./todoapp.db"
# :5432
DATABASE_URL = "postgresql://postgres:10872@localhost/todoapp"

engine = create_engine(url=DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()
