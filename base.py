from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


conn_string ='mysql+mysqldb://root:test123@localhost:3306/rsa_unified_db'
engine = create_engine(conn_string)
Session = sessionmaker(bind=engine)

Base = declarative_base()