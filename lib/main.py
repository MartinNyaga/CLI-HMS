import click
from models import session, Doctor, Patient, Appointment
from datetime import datetime, date  

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Doctor name', help='Name of the doctor')
@click.option('--specialty', prompt='Doctor specialty', help='Specialty of the doctor')
def add_doctor(name, specialty):
    """Add a new doctor to the database."""
    doctor = Doctor(name=name, specialty=specialty)
    session.add(doctor)
    session.commit()
    click.echo(f'Doctor {name} added to the database.')

@cli.command()
@click.option('--name', prompt='Patient name', help='Name of the patient')
@click.option('--dob', prompt='Date of birth (YYYY-MM-DD)', help='Date of birth of the patient')
@click.option('--gender', prompt='Gender', help='Gender of the patient')
def add_patient(name, dob, gender):
    """Add a new patient to the database."""
    
   
    dob_date = datetime.strptime(dob, '%Y-%m-%d').date()

    
    patient = Patient(name=name, dob=dob_date, gender=gender)
    session.add(patient)
    session.commit()
    click.echo(f'Patient {name} added to the database.')

@cli.command()
@click.option('--doctor-id', type=int, prompt='Doctor ID', help='ID of the doctor')
@click.option('--patient-id', type=int, prompt='Patient ID', help='ID of the patient')
@click.option('--appointment-date', prompt='Appointment date (YYYY-MM-DD)', help='Date of the appointment')
def add_appointment(doctor_id, patient_id, appointment_date):
    """Add a new appointment to the database."""
    
   
    appointment_date = datetime.strptime(appointment_date, '%Y-%m-%d').date()

    
    appointment = Appointment(doctor_id=doctor_id, patient_id=patient_id, appointment_date=appointment_date)
    session.add(appointment)
    session.commit()
    click.echo('Appointment added to the database.')

if __name__ == '__main__':
    cli()
