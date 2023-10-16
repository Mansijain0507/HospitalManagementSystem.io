from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from __init__ import create_app, db
from models import Appointment, Patient, Doctor
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/admin')
@login_required
def admin():
    id = current_user.id
    if id == 1:
        return render_template('admin.html')
    else:
        flash("Sorry you must be admin to access the admin page ")
        return redirect(url_for('main.profile'))


@main.route('/patient', methods=['GET', 'POST'])
def patient():
    if request.method == 'POST':
        patientName = request.form.get('patientName')
        gender = request.form.get('gender')
        age = request.form.get('age')
        address = request.form.get('address')
        mobile = request.form.get('mobile')
        patients = Patient(patientName=patientName, gender=gender,
                           age=age, address=address, mobile=mobile)
        db.session.add(patients)
        db.session.commit()
    allpatient = Patient.query.all()
    print(allpatient)
    return render_template('patient.html', allpatient=allpatient)


@main.route('/doctor', methods=['GET', 'POST'])
def doctor():
    if request.method == 'POST':
        doctorName = request.form.get('doctorName')
        mobile = request.form.get('mobile')
        department = request.form.get('department')
        doctors = Doctor(doctorName=doctorName,
                         mobile=mobile, department=department)
        db.session.add(doctors)
        db.session.commit()
    alldoctor = Doctor.query.all()
    print(alldoctor)
    return render_template('doctor.html', alldoctor=alldoctor)


@main.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':

        patientName = request.form.get('patientName')
        mobile = request.form.get('mobile')
        department = request.form.get('department')
        description = request.form.get('description')
        appointments = Appointment(
            patientName=patientName, mobile=mobile, department=department, description=description)
        db.session.add(appointments)
        db.session.commit()

    allappointment = Appointment.query.all()
    print(allappointment)
    return render_template('appointment.html', allappointment=allappointment)


app = create_app()
if __name__ == '__main__':

    with app.app_context():
        db.create_all()
        app.run(debug=True, port=8000)
