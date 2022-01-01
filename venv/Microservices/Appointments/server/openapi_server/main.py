
from flask import Blueprint
from pymongo import collection
from .extensions import mongo

main=Blueprint('main',__name__)


@main.route('/')
def index():
  post1= {
    "id":1,
    "name": "karam Thebian",
    "address": "beirut",
    "phoneNumber": "81615542"
  }
  post2={
    "id":2,
    "name": "Abdel Motaleb",
    "address": "hamra",
    "phoneNumber": "81111111"
  }
  post3={
    "id":3,
    "name": "Client 3",
    "address": "tripoli",
    "phoneNumber": "81222222"
  }
  client_collection=mongo.db.Appointments
  client_collection.insert_many([post1,post2,post3])
 


  return '<h1>DB started!</h1>'


def addAppointmentToDB(appointment):
  appointment_collection=mongo.db.Appointments
  count=appointment_collection.find().count()
  appointment.id=count+1
  pAppointment={
    "id": appointment.id,
    "patientName": appointment.patient_name,
    "issue": appointment.issue,
    "doctor": appointment.doctor,
    "clinic": appointment.clinic,
    "date": appointment.date
}
  
  appointment_collection.insert_one(pAppointment)

def getAllAppointmentsFromDB():
  appointment_collection=mongo.db.Appointments
  
  return list(appointment_collection.find({}, {'_id': False}))


def delete_appointment(id):
  appointment_collection = mongo.db.Appointments
  appointment_collection.delete_one({"id":id})



def edit_appointment(id, appointment):
  appointment_collection = mongo.db.Appointments
  appointment_collection.update_one({"id":id},{"$set":{"patientName": appointment.patient_name,
    "issue": appointment.issue,
    "doctor": appointment.doctor,
    "clinic": appointment.clinic,
    "date": appointment.date}})



def find_appointments_by_doctor_name(name):
  appointment_collection = mongo.db.Appointments

  return list(appointment_collection.find({"doctor":name}, {'_id': False}))



def find_appointments_by_patient_name(name):
  appointment_collection = mongo.db.Appointments

  return list(appointment_collection.find({"patientName":name}, {'_id': False}))