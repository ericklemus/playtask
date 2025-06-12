import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Replace with your own PostgreSQL instance
DATABASE_URL = os.environ.get(
    "DATABASE_URL", "postgresql://postgres:postgres@db:5432/mydb"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
