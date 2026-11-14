
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import URL


# SQL Server configuration
DB_SERVER = "172.31.3.168"
DB_PORT = 1433
DB_NAME = "FastApi"

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]

ODBC_DRIVER = "ODBC Driver 18 for SQL Server"


# SQL Server Authentication connection
connection_url = URL.create(
    "mssql+pyodbc",
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_SERVER,
    port=DB_PORT,
    database=DB_NAME,
    query={
        "driver": ODBC_DRIVER,
        "Encrypt": "yes",
        "TrustServerCertificate": "yes"
    }
)


# Create database engine
engine = create_engine(
    connection_url,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10
)


# Database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base model
Base = declarative_base()


# Database dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
