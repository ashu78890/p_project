from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL,echo=True)  #echo true it will print all sql querirs that sql alchemy runs4
sessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base =declarative_base()