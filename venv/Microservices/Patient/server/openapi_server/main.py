
from flask import Blueprint
from pymongo import collection
from .extensions import mongo
import json

main=Blueprint('main',__name__)


@main.route('/')
def index():
  post1= {
    "id": 1,
    "name": "patient1",
    "bloodType": "fugiat",
    "medication": [
        {
            "name": "deserunt anim sunt commodo",
            "methodOfUse": "et commodo voluptate"
        },
        {
            "name": "ullamco non ea Lorem",
            "methodOfUse": "minim qui consequat"
        }
    ],
    "username": "patient1",
    "password": "patient1123",
    "address": "aliqua aliquip",
    "phoneNumber": "aute ex laborum velit anim",
    "dateOfBirth": "2013-12-17",
    "private": True
}
  post2={
    "id": 2,
    "name": "patient2",
    "bloodType": "fugiat",
    "medication": [
        {
            "name": "Panadol",
            "methodOfUse": "Twice Per Day"
        },
        {
            "name": "Augmentin",
            "methodOfUse": "Once A Day"
        }
    ],
    "username": "patient2",
    "password": "patient2123",
    "address": "aliqua aliquip",
    "phoneNumber": "aute ex laborum velit anim",
    "dateOfBirth": "2013-12-17",
    "private": True
}

  patient_collection=mongo.db.Patients
  patient_collection.insert_many([post1,post2])
 


  return '<h1>DB started!</h1>'


















def add_patient(patient):
  patient_collection = mongo.db.Patients
  count = patient_collection.find().count()
  patient.id = count + 1
  medicationlst=""

  for item in patient.medication:
      name=item.name
      method= item.method_of_use
      medicationlst+='{"name: "'+name+', "method: "'+method+ '}'
  pPatient = {
    "id": patient.id,
    "name": patient.name,
    "bloodType": patient.blood_type,
    "medication": [{
            "name": patient.medication[0].name,
            "methodOfUse": patient.medication[0].method_of_use
        },
        {
            "name": patient.medication[1].name,
            "methodOfUse": patient.medication[1].method_of_use
        }],
    "username": patient.username,
    "password": patient.password,
    "address": patient.address,
    "phoneNumber": patient.phone_number,
    "dateOfBirth": str(patient.date_of_birth),
    "private": patient.private
}
  patient_collection.insert_one(pPatient)




def delete_patient(id):
  patient_collection = mongo.db.Patients
  patient_collection.delete_one({"id": id})


def edit_patient(id, patient):
  patient_collection = mongo.db.Patients
  patient_collection.update_one({"id":id},{"$set":{
    "name": patient.name,
    "bloodType": patient.blood_type,
    "medication": patient.medication,
    "username": patient.username,
    "password": patient.password,
    "address": patient.address,
    "phoneNumber": patient.phone_number,
    "dateOfBirth": patient.date_of_birth,
    "private": patient.private
}})


def find_patient_by_name(name):
  patient_collection = mongo.db.Patients

  return list(patient_collection.find({"name": name}, {'_id': False}))

"""
modify db or code to find patient by Doctor name"""

def find_patient_by_doctor_name(name):
  patient_collection = mongo.db.Patients

  return list(patient_collection.find({"Doctor": name}, {'_id': False}))


def get_all_patients():
  patient_collection = mongo.db.Patients

  return list(patient_collection.find({}, {'_id': False}))
