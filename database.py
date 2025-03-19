from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# З'єднання з базою даних SQLite
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()