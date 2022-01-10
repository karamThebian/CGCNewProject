
from flask import Blueprint
import pymongo
from pymongo import  MongoClient
from .extensions import mongo
from .settings import MONGO_URI
import  requests
import time
from jose import JWTError, jwt
import rsa
from .encryption import rsaEncrypt , rsaDecrypt
import binascii
publicKey, privateKey = rsa.newkeys(256)

JWT_SECRET = 'thisismysecretkey'
JWT_LIFETIME_SECONDS = 3600
JWT_ALGORITHM = 'HS256'

main=Blueprint('main',__name__)


@main.route('/')
def index():
   client= MongoClient(MONGO_URI)
   db= client.Doctors
   collection=db.Doctors

   post1 = {
       "id": 1,
       "name": "karam Thebian",
       "address": "beirut",
       "phoneNumber": "81615542"
   }
   post2 = {
       "id": 2,
       "name": "Abdel Motaleb",
       "address": "hamra",
       "phoneNumber": "81111111"
   }
   post3 = {
       "id": 3,
       "name": "Client 3",
       "address": "tripoli",
       "phoneNumber": "81222222"
   }

   collection.insert_many([post1, post2, post3])

   return '<h1>DB started!</h1>'

def _current_timestamp() -> int:
    return int(time.time())

def auth_doctor(body):
    URL = "http://192.168.8.111:5001/api/v1/doctor/username/"+body.username
    r = requests.get(url=URL)
    data=r.json()
    try:
        data= dict(data[0])
    except:
         return "Unauthorized: Incorrect Username", 401
    if(data.get('password') != body.password):
        return "Unauthorized: Incorrect Password",401
    else:
        timestamp = _current_timestamp()
        payload = {
            "iat": int(timestamp),
            "exp": int(timestamp + JWT_LIFETIME_SECONDS),
            "id":data.get('id') ,
            "username": data.get('username'),
            "Authority": "Doctor"

        }
        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM).split(".")

        token[1]="sAlTeD"+token[1]+"sAlTeD"

        modtoken=".".join(token)


        #token="hello world!"
        #token=token.encode('utf8')
        #print("token",token)
        #enctoken=rsaEncrypt(token)
        #dectoken=rsaDecrypt(enctoken)
        #print(enctoken)
        #enctoken=enctoken.decode('utf8')
        #print("enctoken", enctoken)
        #print("dectoken",dectoken)
        return "Token: sPiCeD"+modtoken+"sPiCeD",200



def auth_patient(body):
    URL = "http://192.168.8.111:5002/api/v1/patient/username/" + body.username
    timestamp = _current_timestamp()
    payload = {
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "id": None,
        "username": None,
        "Authority": "Ultimate"

    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM).split(".")

    token[1] = "sAlTeD" + token[1] + "sAlTeD"

    modtoken = ".".join(token)
    HEADER = {'Authorization': 'Bearer ' + modtoken}
    print(HEADER)
    r = requests.get(url=URL,headers=HEADER )
    print(r)
    data = r.json()
    try:
        data = dict(data[0])
    except:
        return "Unauthorized: Incorrect Username", 401
    if (data.get('password') != body.password):
        return "Unauthorized: Incorrect Password", 401
    else:
        timestamp = _current_timestamp()
        payload = {
            "iat": int(timestamp),
            "exp": int(timestamp + JWT_LIFETIME_SECONDS),
            "id": data.get('id'),
            "username": data.get('username'),
            "Authority": "Patient"

        }
        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM).split(".")

        token[1] = "sAlTeD" + token[1] + "sAlTeD"

        modtoken = ".".join(token)

        # token="hello world!"
        # token=token.encode('utf8')
        # print("token",token)
        # enctoken=rsaEncrypt(token)
        # dectoken=rsaDecrypt(enctoken)
        # print(enctoken)
        # enctoken=enctoken.decode('utf8')
        # print("enctoken", enctoken)
        # print("dectoken",dectoken)
        return "Token: sPiCeD" + modtoken + "sPiCeD", 200



