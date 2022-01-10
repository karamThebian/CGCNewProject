import connexion
import six
from .. import main
from openapi_server.models.doctor import Doctor  # noqa: E501
from openapi_server import util
from jose import JWTError, jwt
from werkzeug.exceptions import Unauthorized
JWT_SECRET = 'thisismysecretkey'

JWT_ALGORITHM = 'HS256'

def decode_token(token):
    token1= token.replace("sAlTeD","")
    token1=token1.replace("sPiCeD","")
    try:
         return jwt.decode(token1, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        # return "Unauthorized:" + e, 401
        raise Unauthorized from e

def add_doctor(body):  # noqa: E501
    """Add a new doctor to the database

    adds a new doctor to the database # noqa: E501

    :param body: Doctor object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Doctor.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            main.add_doctor(body)
            response= "Doctor added successfully",200
        except :
            response= "Could not add doctor", 400
    return response


def delete_doctor(idm):  # noqa: E501
    """Deletes a doctor

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """

    try:
        auth = connexion.request.headers.get("Authorization").split()[-1]
        token1 = auth.replace("sAlTeD", "")
        auth = token1.replace("sPiCeD", "")
        auth = jwt.decode(auth, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        id = auth.get("id")
        authority=auth.get("Authority")
        username=auth.get("username")
        if(authority!='Doctor'):
            return "Unauthorized: Delete of a Dr Account By a Non Doctor Personal Attempted",401
        if (id == idm):
            main.delete_doctor(idm)
            response = "Doctor Deleted Successfully", 200
        else:
            return "Unauthorized: You cannot Delete Another Drs Profile", 401

    except KeyError:
        response = {}, 404
    return response


def edit_doctor(idm, body):  # noqa: E501
    """Update an existing doctor

    updates an existing doctor in the database # noqa: E501

    :param id: name values that need to be considered for filter
    :type id: int
    :param body: Doctor object that needs to be added to the databse
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Doctor.from_dict(connexion.request.get_json())  # noqa: E501
        auth=connexion.request.headers.get("Authorization").split()[-1]
        token1 = auth.replace("sAlTeD", "")
        auth = token1.replace("sPiCeD", "")
        auth= jwt.decode(auth, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        id=auth.get("id")
        print("auth",auth)
        try:
            if(id==idm):
                main.edit_doctor(idm, body)
                response = "Doctor edited Successfully", 200
            else:
                return "Unauthorized: You cannot Edit Another Drs Profile", 401
        except KeyError:
            response = "Doctor ID not found", 400
    return response


def find_doctor_by_username(name):  # noqa: E501
    """Finds doctor by Name

    returns doctor by name # noqa: E501

    :param name: name values that need to be considered for filter
    :type name: str

    :rtype: List[Doctor]
    """
    try:
        response=main.find_doctor_by_username(name),200
    except:
        response= "Doctor not found",400

    return response


def find_doctor_by_patient_name(name):  # noqa: E501
    """Finds doctors by  Patients Name

    returns doctors by Patients name # noqa: E501

    :param name: name values that need to be considered for filter
    :type name: str

    :rtype: List[Doctor]
    """
    try:
        response = main.find_doctor_by_patient_name(name), 200
    except:
        response = "Doctor not found", 400

    return response


def get_all_doctors():  # noqa: E501
    """Get all doctors

    returns all doctor # noqa: E501


    :rtype: List[Doctor]
    """
    try:
        response = main.get_all_doctors(), 200
    except:
        response = "Error 400", 400

    return response

