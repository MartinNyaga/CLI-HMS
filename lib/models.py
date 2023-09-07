from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///hospital_database.db')

Base = declarative_base()

