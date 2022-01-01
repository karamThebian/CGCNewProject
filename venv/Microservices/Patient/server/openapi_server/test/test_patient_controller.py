# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.patient import Patient  # noqa: E501
from openapi_server.test import BaseTestCase


class TestPatientController(BaseTestCase):
    """PatientController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_patient(self):
        """Test case for add_patient

        Add a new patient to the database
        """
        body = {
  "password" : "password",
  "private" : true,
  "address" : "address",
  "phoneNumber" : "phoneNumber",
  "name" : "name",
  "medication" : [ {
    "name" : "name",
    "methodOfUse" : "methodOfUse"
  }, {
    "name" : "name",
    "methodOfUse" : "methodOfUse"
  } ],
  "dateOfBirth" : "2000-01-23",
  "id" : 0,
  "bloodType" : "bloodType",
  "username" : "username"
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/patient/',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_patient(self):
        """Test case for delete_patient

        Deletes a patient
        """
        headers = { 
        }
        response = self.client.open(
            '/api/v1/patient/{id}'.format(id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_edit_patient(self):
        """Test case for edit_patient

        Update an existing patient
        """
        body = {
  "password" : "password",
  "private" : true,
  "address" : "address",
  "phoneNumber" : "phoneNumber",
  "name" : "name",
  "medication" : [ {
    "name" : "name",
    "methodOfUse" : "methodOfUse"
  }, {
    "name" : "name",
    "methodOfUse" : "methodOfUse"
  } ],
  "dateOfBirth" : "2000-01-23",
  "id" : 0,
  "bloodType" : "bloodType",
  "username" : "username"
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/patient/{id}'.format(id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_patient_by_name(self):
        """Test case for find_patient_by_name

        Finds patient by Name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/patient/name/{name}'.format(name='name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_patients_by_doctorsname(self):
        """Test case for find_patients_by_doctorsname

        Finds patients by Doctors Name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/patient/doctorsname/{name}'.format(name='name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_patients(self):
        """Test case for get_all_patients

        Get all patients
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/patient/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
