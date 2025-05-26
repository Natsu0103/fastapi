from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Get the database URL from environment variables (ensure this is set in your .env file)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # Set default value if not found

# Create the SQLAlchemy engine for database connection
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a base class for declarative models
Base = declarative_base()

# Create a sessionmaker for working with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
