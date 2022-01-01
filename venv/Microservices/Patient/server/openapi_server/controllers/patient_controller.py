import connexion
import six
from .. import main
from openapi_server.models.patient import Patient  # noqa: E501
from openapi_server import util


def add_patient(body):  # noqa: E501
    """Add a new patient to the database

    adds a new patient to the database # noqa: E501

    :param body: Patient object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Patient.from_dict(connexion.request.get_json())  # noqa: E501
        #try:
        main.add_patient(body)
        response = "Patient added successfully", 200
        #except:
        #    response = "Could not add patient", 400

    return response


def delete_patient(idm):  # noqa: E501
    """Deletes a patient

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    try:
        main.delete_patient(idm)
        response = "Patient Deleted Successfully", 200
    except KeyError:
        response = {}, 404
    return response


def edit_patient(idm, body):  # noqa: E501
    """Update an existing patient

    updates an existing patient in the database # noqa: E501

    :param id: name values that need to be considered for filter
    :type id: int
    :param body: Patient object that needs to be added to the databse
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Patient.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            main.edit_patient(idm, body)
            response = "Patient edited Successfully", 200
        except KeyError:
            response = "Patient ID not found", 400
    return response


def find_patient_by_name(name):  # noqa: E501
    """Finds patient by Name

    returns patient by name # noqa: E501

    :param name: name values that need to be considered for filter
    :type name: str

    :rtype: List[Patient]
    """
    try:
        response = main.find_patient_by_name(name), 200
    except:
        response = "Patient not found", 400

    return response


def find_patients_by_doctorsname(name):  # noqa: E501
    """Finds patients by Doctors Name

    returns patients by doctors name # noqa: E501

    :param name: name values that need to be considered for filter
    :type name: str

    :rtype: List[Patient]
    """
    try:
        response = main.find_patient_by_doctor_name(name), 200
    except:
        response = "Patient not found", 400

    return response


def get_all_patients():  # noqa: E501
    """Get all patients

    returns all patient # noqa: E501


    :rtype: List[Patient]
    """
    try:
        response = main.get_all_patients(), 200
    except:
        response = "Error 400", 400

    return response
