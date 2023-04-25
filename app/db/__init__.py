from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# connect to database using env variable
# engine manages connection to db 
# session generates temporary connections for performing create, read, update, and delete(CRUD operations)
# Base is a class variable helps us map the models to MySQL tables 
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()