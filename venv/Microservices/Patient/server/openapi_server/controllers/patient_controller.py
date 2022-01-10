import connexion
import six
from .. import main
from openapi_server.models.patient import Patient  # noqa: E501
from openapi_server.models.medicine import Medicine  # noqa: E501
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


def add_patient(body):  # noqa: E501
    """Add a new patient to the database

    adds a new patient to the database # noqa: E501

    :param body: Patient object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Patient.from_dict(connexion.request.get_json())  # noqa: E501
        return main.add_patient(body)





def delete_patient(idm):  # noqa: E501
    """Deletes a patient

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
        id = auth.get("id",-1)
        authority = auth.get("Authority",-1)
        username = auth.get("username",-1)
        if (id == -1 or authority == -1 or username == -1):
            raise Exception
        if(id!=idm):
            return "Unauthorized: You cannot Delete Another Patients Profile", 401
        if (authority != 'Patient'):
            return "Unauthorized: Delete of a Patient Account By a Non Patient Personal Attempted", 401
        return main.delete_patient(idm)

    except:
        return  "Error: Bad Token", 400



def edit_patient(idm, body):  # noqa: E501
    """Update an existing patient

    updates an existing patient in the database # noqa: E501

    :param id: name values that need to be considered for filter
    :type id: int
    :param body: Patient object that needs to be added to the databse
    :type body: dict | bytes

    :rtype: None
    """
    auth = connexion.request.headers.get("Authorization").split()[-1]
    token1 = auth.replace("sAlTeD", "")
    auth = token1.replace("sPiCeD", "")
    auth = jwt.decode(auth, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    id = auth.get("id",-1)
    authority = auth.get("Authority",-1)
    username = auth.get("username",-1)

    if connexion.request.is_json:
        body = Patient.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            if (id == -1 or authority == -1 or username == -1):
                raise Exception
            if (id != idm):
                return "Unauthorized: You cannot Delete Another Patients Profile", 401
            if (authority != 'Patient'):
                return "Unauthorized: Delete of a Patient Account By a Non Patient Personal Attempted", 401
            return main.edit_patient(idm, body)

        except :

            return "Error: Bad Token", 400



def find_patient_by_username(name):  # noqa: E501
    """Finds patient by Name

    returns patient by name # noqa: E501

    :param name: name values that need to be considered for filter
    :type name: str

    :rtype: List[Patient]
    """
    try:
        auth = connexion.request.headers.get("Authorization").split()[-1]

    except:
        return "Error: Bad Token" , 400
    token1 = auth.replace("sAlTeD", "")
    auth = token1.replace("sPiCeD", "")

    auth = jwt.decode(auth, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    id = auth.get("id",-1)
    authority = auth.get("Authority",-1)
    usernameFromToken = auth.get("username",-1)
    if(authority=='Ultimate'):
        try:
            return main.find_patient_by_username(name),200
        except:
            return "",404
    if(usernameFromToken!=name and authority=="Patient"):
        return "Unauthorized: You Cannot View Another Patients Account "
    try:
        if (id == -1 or authority == -1 or usernameFromToken == -1):
            raise Exception
        if (authority == 'Doctor'):
            #Check if Patient Allowed this Dr to view Account
            try:
                patient = main.find_patient_by_username(name)
                print(patient)
                print("username",usernameFromToken)
                if usernameFromToken in str(patient):
                    return  patient , 200
                else:
                    return "Unauthorized: Patient did not Authorize you",401
            except:
                return "Error: Could Not Find Patient, check Patient Username", 404
        if (usernameFromToken == name and authority == "Patient"):
            try:
                return main.find_patient_by_username(name),200
            except Exception as e:
                print(e)
                return "Error: Could Not Find Patient, check Patient Username ",404
    except:
        return "Error: Bad Token" , 400


def add_patient_medication(name):  # noqa: E501
    """Adds patient Medication by Name

    # noqa: E501

    :param name: name values that need to be considered for filter
    :type name: str

    :rtype: List[Patient]
    """
    try:
        auth = connexion.request.headers.get("Authorization").split()[-1]

    except:
        return "Error: Bad Token" , 400
    token1 = auth.replace("sAlTeD", "")
    auth = token1.replace("sPiCeD", "")

    auth = jwt.decode(auth, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    id = auth.get("id",-1)
    authority = auth.get("Authority",-1)
    usernameFromToken = auth.get("username",-1)

    if(authority=="Patient"):
        return "Unauthorized: You Cannot Add Medication "
    try:
        if (id == -1 or authority == -1 or usernameFromToken == -1):
            raise Exception
        if (authority == 'Doctor'):
            #Check if Patient Allowed this Dr to view Account
            try:
                patient = main.find_patient_by_username(name)
                print(patient)
                print("username",usernameFromToken)
                if usernameFromToken in str(patient):
                    if connexion.request.is_json:
                        print(connexion.request.get_json())
                        body = [Medicine.from_dict(d) for d in connexion.request.get_json()]
                        return main.add_patient_medication(body,name)
                else:
                    return "Unauthorized: Patient did not Authorize you",401
            except Exception as e:
                print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
                return "Error: Could Not Find Patient, check Patient Username", 404

    except:
        return "Error: Bad Token" , 400




def find_patients_by_doctorsname(name):  # noqa: E501
    """Finds patients by Doctors Name

    returns patients by doctors name # noqa: E501

    :param name: name values that need to be considered for filter
    :type name: str

    :rtype: List[Patient]
    """
    ######FUTURE FEATURE CAN BE ADDED
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
        auth = connexion.request.headers.get("Authorization").split()[-1]

    except:
        return "Error: Bad Token" , 400
    token1 = auth.replace("sAlTeD", "")
    auth = token1.replace("sPiCeD", "")

    auth = jwt.decode(auth, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    id = auth.get("id",-1)
    authority = auth.get("Authority",-1)
    usernameFromToken = auth.get("username",-1)
    if(authority=='Ultimate'):
        try:
            return main.get_all_patients(), 200
        except:
            return "Empty: No Patients Available",404
    else:
        return "Unauthorized: You are Not Authorized to access all Patients!"

