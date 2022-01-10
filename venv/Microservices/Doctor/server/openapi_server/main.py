
from flask import Blueprint
from pymongo import collection
from .extensions import mongo

main=Blueprint('main',__name__)


@main.route('/')
def index():
  post1= {
  "id": 1,
  "name": "abed motaleb",
  "speciality": "Neuro Surgeon",
  "username": "abed",
  "password": "abed123",
  "address": "beirut",
  "phoneNumber": "961-81-61-55-42",
  "dateOfBirth": "1962-07-02"
 }
  post2={
  "id": 2,
  "name": "kaytho",
  "speciality": "Heart Surgeon",
  "username": "kay",
  "password": "kay123",
  "address": "hamra",
  "phoneNumber": "961-81-00-00-00",
  "dateOfBirth": "2008-10-12"
 }

  doctor_collection=mongo.db.Doctors
  doctor_collection.insert_many([post1,post2])
 


  return '<h1>DB started!</h1>'


















def add_doctor(doctor):
  doctor_collection = mongo.db.Doctors
  count = doctor_collection.find().count()
  doctor.id = count + 1
  pDoctor = {
    "id": doctor.id,
    "name": doctor.name,
    "speciality": doctor.speciality,
    "username": doctor.username,
    "password": doctor.password,
    "address": doctor.address,
    "phoneNumber": doctor.phone_number,
    "dateOfBirth": str(doctor.date_of_birth)
  }
  doctor_collection.insert_one(pDoctor)


def delete_doctor(id):
  doctor_collection = mongo.db.Doctors
  doctor_collection.delete_one({"id": id})


def edit_doctor(id, doctor):
  doctor_collection = mongo.db.Doctors
  doctor_collection.update_one({"id":id},{"$set":{"name": doctor.name,
    "speciality": doctor.speciality,
    "username": doctor.username,
    "password": doctor.password,
    "address": doctor.address,
    "phoneNumber": doctor.phone_number,
    "dateOfBirth": str(doctor.date_of_birth)}})


def find_doctor_by_username(name):
  doctor_collection = mongo.db.Doctors

  return list(doctor_collection.find({"username": name}, {'_id': False}))

"""
modify db or code to find doctor by patient name"""

def find_doctor_by_patient_name(name):
  doctor_collection = mongo.db.Doctors

  return list(doctor_collection.findOne({"patientName": name}, {'_id': False}))


def get_all_doctors():
  doctor_collection = mongo.db.Doctors

  return list(doctor_collection.find({}, {'_id': False}))
