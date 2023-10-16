from flask_login import UserMixin
from __init__ import db
from datetime import datetime, date


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), nullable=False)


class Appointment(db.Model):
    appointmentid = db.Column(db.Integer, primary_key=True)
    patientName = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(10), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    # appointmentDate = db.Column(db.Datetime, default = datetime)
    description = db.Column(db.String(500), nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=False)


class Patient(db.Model):

    patientid = db.Column(db.Integer, primary_key=True)
    patientName = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.Enum('male', 'female', 'other', name='varchar'))
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    mobile = db.Column(db.String(10), nullable=False)
    # assignedDoctorName = db.Column(db.String(100), nullable=False)
    # admitDate = db.column(db.Datetime)


class Doctor(db.Model):
    doctorid = db.Column(db.Integer, primary_key=True)
    doctorName = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(100), nullable=False)


# class Room(db.Model):
#     roomNo = db.Column(db.Integer, primary_key=True)
#     roomType = db.Column(db.String, nullable=False)
#     available = db.Column(db.Integer, nullable=False)


# class Medicines(db.Model):
#     code = db.Column(db.Integer, primary_key=True)
#     medicineName = db.Column(db.String, nullable=False)
#     brand = db.Column(db.String, nullable=False)
