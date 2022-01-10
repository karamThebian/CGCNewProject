import connexion
import six

from openapi_server.models.credentials import Credentials  # noqa: E501
from openapi_server import util


def auth_doctor(body):  # noqa: E501
    """Authorize a doctor

    Authorizes a doctor from the databse # noqa: E501

    :param body: Doctor Credentials
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Credentials.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def auth_patient(body):  # noqa: E501
    """Authorize a patient

    Authorizes a patient from the databse # noqa: E501

    :param body: Patient Credentials
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Credentials.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
