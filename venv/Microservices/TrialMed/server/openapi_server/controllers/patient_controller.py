import connexion
import six

from openapi_server.models.doctorauth import Doctorauth  # noqa: E501
from openapi_server.models.medicine import Medicine  # noqa: E501
from openapi_server.models.patient import Patient  # noqa: E501
from openapi_server import util


def add_doctor_access(name, body):  # noqa: E501
    """Authorize a new doctor to the patient database

    adds a new Doctor to the Patient database # noqa: E501

    :param name: name values that need to be considered for filter
    :type name: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Doctorauth.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_patient(body):  # noqa: E501
    """Add a new patient to the database

    adds a new patient to the database # noqa: E501

    :param body: Patient object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Patient.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_patient_medication(name, body):  # noqa: E501
    """Add a new medication to the patient database

    adds a new Medication to the Patient database # noqa: E501

    :param name: name values that need to be considered for filter
    :type name: str
    :param body: Medication object that needs to be added to the database
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Medicine.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def delete_patient(idm):  # noqa: E501
    """Deletes a patient

     # noqa: E501

    :param idm: 
    :type idm: int

    :rtype: None
    """
    return 'do some magic!'


def edit_patient(idm, body):  # noqa: E501
    """Update an existing patient

    updates an existing patient in the database # noqa: E501

    :param idm: name values that need to be considered for filter
    :type idm: int
    :param body: Patient object that needs to be added to the databse
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Patient.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_patient_by_username(name):  # noqa: E501
    """Finds patient by Name

    returns patient by username # noqa: E501

    :param name: name values that need to be considered for filter
    :type name: str

    :rtype: List[Patient]
    """
    return 'do some magic!'


def find_patients_by_doctorsname(name):  # noqa: E501
    """Finds patients by Doctors Name

    returns patients by doctors name # noqa: E501

    :param name: name values that need to be considered for filter
    :type name: str

    :rtype: List[Patient]
    """
    return 'do some magic!'


def get_all_patients():  # noqa: E501
    """Get all patients

    returns all patient # noqa: E501


    :rtype: List[Patient]
    """
    return 'do some magic!'
