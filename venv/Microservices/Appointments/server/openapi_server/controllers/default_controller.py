import connexion
import six
from .. import main
from openapi_server.models.appointment import Appointment  # noqa: E501
from openapi_server import util


def add_appointment(body):  # noqa: E501
    """Add a new appointment to the database

    adds a new appointment to the database # noqa: E501

    :param body: Appointment object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Appointment.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            main.addAppointmentToDB(body)
            response = {"Appointment added successfully"}, 200
        except:
            response= {"Could not add appointment"},400
    return response


def delete_appointment(iddelete):  # noqa: E501
    """Deletes an Appointment

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """

    try:
        main.delete_appointment(iddelete)
        response={},200
    except KeyError:
        response={},404
    return response


def edit_appointment(iddelete, body):  # noqa: E501
    """Update an existing appointment

    updates an existing appointment in the database # noqa: E501

    :param id: id value that needs to be considered for filter
    :type id: int
    :param body: Appointment object that needs to be Modified in the databse
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Appointment.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            main.edit_appointment(iddelete,body)
            response={"Appointment edited Successfully"},200
        except KeyError:
            response={"Appointment ID not found"},400
    return response


def find_appointments_by_doctor_name(name):  # noqa: E501
    """Finds Appointments by doctor name

    returns Appointment by doctor name # noqa: E501

    :param name: name values that need to be considered for filter
    :type name: str

    :rtype: List[Appointment]
    """
    response=main.find_appointments_by_doctor_name(name)
    return response,200


def find_appointments_by_patient_name(name):  # noqa: E501
    """Finds Appointments by patient name

    returns Appointment by patient name # noqa: E501

    :param name: name values that need to be considered for filter
    :type name: str

    :rtype: List[Appointment]
    """
    response=main.find_appointments_by_patient_name(name)
    return response,200


def get_all_appointments():  # noqa: E501
    """Get all appointments

    returns all appointments # noqa: E501


    :rtype: List[Appointment]
    """
    response=main.getAllAppointmentsFromDB()
    return response,200
