from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String,Date,ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///hospital_database.db')



Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    specialty = Column(String())

    
    appointments = relationship('Appointment', back_populates='doctor')

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    dob = Column(Date())
    gender = Column(String())

    
    appointments = relationship('Appointment', back_populates='patient')

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer(), primary_key=True)
    appointment_date = Column(Date())
    doctor_id = Column(Integer(), ForeignKey('doctors.id'))
    patient_id = Column(Integer(), ForeignKey('patients.id'))

    
    doctor = relationship('Doctor', back_populates='appointments')
    patient = relationship('Patient', back_populates='appointments')
