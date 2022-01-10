import connexion
import six
from .. import main
from openapi_server.models.appointment import Appointment  # noqa: E501
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

def add_appointment(body):  # noqa: E501
    """Add a new appointment to the database

    adds a new appointment to the database # noqa: E501

    :param body: Appointment object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Appointment.from_dict(connexion.request.get_json())  # noqa: E501
        auth = connexion.request.headers.get("Authorization").split()[-1]
        token1 = auth.replace("sAlTeD", "")
        auth = token1.replace("sPiCeD", "")
        auth = jwt.decode(auth, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        id = auth.get("id")
        authority = auth.get("Authority")
        username = auth.get("username")
        if (authority != 'Doctor'):
            return "Unauthorized: Appointments can only be added by Doctors ", 401
        if (username == body.doctor):
            #try:
                return main.addAppointmentToDB(body)
                # return "Appointment added successfully", 200
            #except:
                # return "Could not add appointment", 400

        else:
            return "Unauthorized: You cannot Add an appointment for Another Drs Profile", 401



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
