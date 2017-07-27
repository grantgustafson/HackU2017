from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, BigInteger, Boolean, ForeignKey, DateTime, ForeignKeyConstraint, Float

Base = declarative_base()

class Book(Base):
    __tablename__ = 'book_data'
    __bind_key__ = 'nstebbins'
    #__table_args__ = {'schema': 'prism'}

    id = Column(Integer, primary_key=True)
    title = Column(String(1000))
    author = Column(String(1000))
    owner_id = Column(String(1000))
