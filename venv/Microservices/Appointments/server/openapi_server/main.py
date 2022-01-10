
from flask import Blueprint
from pymongo import collection
from .extensions import mongo
from datetime import datetime

main=Blueprint('main',__name__)


@main.route('/')
def index():

 


  return '<h1>DB started!</h1>'


def addAppointmentToDB(appointment):
  appointment_collection=mongo.db.Appointments
  pipeline = [
    {
        '$match': {
            '$and': [
                {
                    'date': {
                        '$eq': appointment.date
                    }
                }, {
                    '$or': [
                        {
                            'doctor': appointment.doctor
                        }, {
                            'patientName': appointment.patient_name
                        }
                    ]
                }
            ]
        }
    }, {
        '$count': 'count'
    }
]

  allappsquantity = appointment_collection.aggregate(pipeline)

  allappsquantity = list(allappsquantity)

  if allappsquantity:
    print(allappsquantity)
    print(type(allappsquantity))

    allappsquantity = allappsquantity[0]
    print(allappsquantity.get("count"))

    if allappsquantity.get("count"):
      return "Conflict Error: You Cannot add an appointment due to Conflict", 409

  # allappsquantity=appointment_collection.find(
  #   {
  #     "$and":
  #      [
  #        {
  #          "date": {
  #            "$eq":appointment.date
  #          }
  #        },
  #        {
  #          "$or":
  #            [
  #              {
  #                "doctor":
  #                  appointment.doctor
  #              },
  #              {
  #                "patientName":
  #                  appointment.patient_name
  #              }
  #            ]
  #        }
  #      ]
  #     },
  #     {
  #       "date": 1,
  #       '_id': False
  #     }
  #   ).count()
  #allapps=list(appointment_collection.find({"$and": [{"date": {"$eq": appointment.date}}, {"$or": [{"doctor": appointment.doctor}, {"patientName": appointment.patient_name}]}]}, {"date": 1, '_id': False}))
  #print(allapps)
  #if (allappsquantity>0):
  #  return "Conflict Error: You Cannot add an appointment due to Conflict", 409

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
  return "Success: Patient Added Successfully" , 200
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