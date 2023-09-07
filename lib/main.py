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

@cli.command()
def list_doctors():
    """List all doctors."""
    doctors = session.query(Doctor).all()
    if doctors:
        click.echo("List of Doctors:")
        for doctor in doctors:
            click.echo(f"{doctor.id}: {doctor.name} ({doctor.specialty})")
    else:
        click.echo("No doctors found.")

@cli.command()
def list_patients():
    """List all patients."""
    patients = session.query(Patient).all()
    if patients:
        click.echo("List of Patients:")
        for patient in patients:
            click.echo(f"{patient.id}: {patient.name} (DOB: {patient.dob}, Gender: {patient.gender})")
    else:
        click.echo("No patients found.")

@cli.command()
def list_appointments():
    """List all appointments."""
    appointments = session.query(Appointment).all()
    if appointments:
        click.echo("List of Appointments:")
        for appointment in appointments:
            click.echo(f"Appointment ID: {appointment.id}")
            click.echo(f"Doctor: {appointment.doctor.name}")
            click.echo(f"Patient: {appointment.patient.name}")
            click.echo(f"Date: {appointment.appointment_date}")
            click.echo()
    else:
        click.echo("No appointments found.")

@cli.command()
@click.option('--id', type=int, prompt='Doctor ID', help='ID of the doctor to update')
@click.option('--name', prompt='New name', help='New name for the doctor')
@click.option('--specialty', prompt='New specialty', help='New specialty for the doctor')
def update_doctor(id, name, specialty):
    """Update a doctor's information."""
    doctor = session.query(Doctor).filter(Doctor.id == id).first()
    if doctor:
        doctor.name = name
        doctor.specialty = specialty
        session.commit()
        click.echo(f'Doctor {id} updated successfully.')
    else:
        click.echo(f'Doctor with ID {id} not found.')

@cli.command()
@click.option('--id', type=int, prompt='Patient ID', help='ID of the patient to update')
@click.option('--name', prompt='New name', help='New name for the patient')
@click.option('--dob', prompt='New date of birth (YYYY-MM-DD)', help='New date of birth for the patient')
@click.option('--gender', prompt='New gender', help='New gender for the patient')
def update_patient(id, name, dob, gender):
    """Update a patient's information."""
    patient = session.query(Patient).filter(Patient.id == id).first()
    if patient:
        patient.name = name
        
        dob_date = datetime.strptime(dob, '%Y-%m-%d').date()
        patient.dob = dob_date
        
        patient.gender = gender
        session.commit()
        click.echo(f'Patient {id} updated successfully.')
    else:
        click.echo(f'Patient with ID {id} not found.')

@cli.command()
@click.option('--id', type=int, prompt='Appointment ID', help='ID of the appointment to update')
@click.option('--doctor-id', type=int, prompt='New Doctor ID', help='New doctor ID for the appointment')
@click.option('--patient-id', type=int, prompt='New Patient ID', help='New patient ID for the appointment')
@click.option('--appointment-date', prompt='New Appointment date (YYYY-MM-DD)', help='New appointment date')
def update_appointment(id, doctor_id, patient_id, appointment_date):
    """Update an appointment's information."""
    appointment = session.query(Appointment).filter(Appointment.id == id).first()
    if appointment:
        appointment.doctor_id = doctor_id
        appointment.patient_id = patient_id
        
        appointment_date = datetime.strptime(appointment_date, '%Y-%m-%d').date()
        appointment.appointment_date = appointment_date
        
        session.commit()
        click.echo(f'Appointment {id} updated successfully.')
    else:
        click.echo(f'Appointment with ID {id} not found.')

@cli.command()
@click.option('--id', type=int, prompt='Doctor ID', help='ID of the doctor to delete')
def delete_doctor(id):
    """Delete a doctor from the database."""
    doctor = session.query(Doctor).filter(Doctor.id == id).first()
    if doctor:
        session.delete(doctor)
        session.commit()
        click.echo(f'Doctor {id} deleted successfully.')
    else:
        click.echo(f'Doctor with ID {id} not found.')

@cli.command()
@click.option('--id', type=int, prompt='Patient ID', help='ID of the patient to delete')
def delete_patient(id):
    """Delete a patient from the database."""
    patient = session.query(Patient).filter(Patient.id == id).first()
    if patient:
        session.delete(patient)
        session.commit()
        click.echo(f'Patient {id} deleted successfully.')
    else:
        click.echo(f'Patient with ID {id} not found.')

@cli.command()
@click.option('--id', type=int, prompt='Appointment ID', help='ID of the appointment to delete')
def delete_appointment(id):
    """Delete an appointment from the database."""
    appointment = session.query(Appointment).filter(Appointment.id == id).first()
    if appointment:
        session.delete(appointment)
        session.commit()
        click.echo(f'Appointment {id} deleted successfully.')
    else:
        click.echo(f'Appointment with ID {id} not found.')


if __name__ == '__main__':
    cli()
