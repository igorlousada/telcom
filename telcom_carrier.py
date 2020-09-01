import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://postgres:r3@Tk`4h1{OPC%3(@localhost:5432/postgres',echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()



class Did(Base):
    __tablename__ = 'Did'

    id = Column(Integer, primary_key=True)
    value = Column(String)
    monthyPrice = Column(Float)
    setupPricee = Column(Float)
    currency =  Column (String)

Base.metadata.create_all(engine)

did1 = Did(value='+55 61 98232-7140',monthyPrice='0.03',setupPricee='3.4',currency='U$S')
session.add(did1)
session.commit()
print(did1.id)

    

    

