from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:Ahmad5351157@localhost:5432/productdb"
engine = create_engine(db_url)

session = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()