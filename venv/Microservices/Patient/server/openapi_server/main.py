
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
    "private": [{"username":"abdelMotaleb"},{"username":"kay"}]
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


    medications_formatted = []
    for med in patient.medication:
        new_med = {
            "name": str(med.name),
            "method_of_use": str(med.method_of_use)
        }
        medications_formatted.append(new_med)

    pPatient = {
        "id": patient.id,
        "name": patient.name,
        "bloodType": patient.blood_type,
        "medication": medications_formatted,
        "username": patient.username,
        "password": patient.password,
        "address": patient.address,
        "phoneNumber": patient.phone_number,
        "dateOfBirth": str(patient.date_of_birth),
        "private": patient.private
    }

    try:

        patient_collection.insert_one(pPatient)
        return "Success: Patient Added Successfully", 201
    except pymongo.errors.PyMongoError as e:
        return "Error: Could Not Add Patient" , 400

def add_patient_medication(medication,username):

        patient_collection = mongo.db.Patients
        print("medication",medication)

        medicationlst=""


        medications_formatted = []
        for med in medication:
            new_med = {
                "name": str(med.name),
                "method_of_use": str(med.method_of_use)
            }
            medications_formatted.append(new_med)



        try:

            patient_collection.update_one({"username": username},{ "$push": {"medication": {"$each": medications_formatted}}})
            return "Success: Medication Added Successfully", 201
        except pymongo.errors.PyMongoError as e:


            return "Error: Could Not Add Medication" , 400


def add_doctor_access(doctor,username):

        patient_collection = mongo.db.Patients
        print("doctor",doctor)





        try:

            patient_collection.update_one({"username": username},{ "$push": {"private": doctor.doctorname}})
            return "Success: Doctor Access Added Successfully", 201
        except pymongo.errors.PyMongoError as e:


            return "Error: Could Not Add Medication" , 400


def delete_patient(id):
  patient_collection = mongo.db.Patients

  x=patient_collection.delete_one({"id": id})
  if(x.deleted_count==0):
        return "Error: Could Not Delete Patient, check Id", 404
  else:
        return  "Success: Patient Deleted Successfully", 200




def edit_patient(id, patient):
  patient_collection = mongo.db.Patients
  medicationlst = ""

  medications_formatted = []
  for med in patient.medication:
      new_med = {
          "name": str(med.name),
          "method_of_use": str(med.method_of_use)
      }
      medications_formatted.append(new_med)
  x = patient_collection.update_one({"id":id},{"$set":{
    "name": patient.name,
    "bloodType": patient.blood_type,
    "medication": medications_formatted,
    "username": patient.username,
    "password": patient.password,
    "address": patient.address,
    "phoneNumber": patient.phone_number,
    "dateOfBirth": str(patient.date_of_birth),
    "private": patient.private
}})
  if(x.modified_count==0):
      return "Error: Could Not Edit Patient, check Id", 404
  else:
      return "Success: Patient Edited Successfully", 200



def find_patient_by_username(name):
  patient_collection = mongo.db.Patients
  x=patient_collection.find_one({"username": name}, {'_id': False})
  if (x):
      return list(patient_collection.find({"username": name}, {'_id': False}))
  else:
      raise Exception
      #return list(x)




def find_patient_by_doctor_name(name):
  #FUTURE FEATURE CAN BE ADDED
  """modify db or code to find patient by Doctor name"""
  patient_collection = mongo.db.Patients

  return list(patient_collection.find({"Doctor": name}, {'_id': False}))


def get_all_patients():
  patient_collection = mongo.db.Patients

  return list(patient_collection.find({}, {'_id': False}))
