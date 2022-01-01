# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.doctor import Doctor  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDoctorController(BaseTestCase):
    """DoctorController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_doctor(self):
        """Test case for add_doctor

        Add a new doctor to the database
        """
        body = {
  "speciality" : "speciality",
  "password" : "password",
  "address" : "address",
  "phoneNumber" : "phoneNumber",
  "name" : "name",
  "dateOfBirth" : "2000-01-23",
  "id" : 0,
  "username" : "username"
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/doctor/',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_doctor(self):
        """Test case for delete_doctor

        Deletes a doctor
        """
        headers = { 
        }
        response = self.client.open(
            '/api/v1/doctor/{id}'.format(id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_edit_doctor(self):
        """Test case for edit_doctor

        Update an existing doctor
        """
        body = {
  "speciality" : "speciality",
  "password" : "password",
  "address" : "address",
  "phoneNumber" : "phoneNumber",
  "name" : "name",
  "dateOfBirth" : "2000-01-23",
  "id" : 0,
  "username" : "username"
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/doctor/{id}'.format(id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_doctor_by_name(self):
        """Test case for find_doctor_by_name

        Finds doctor by Name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/doctor/name/{name}'.format(name='name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_doctor_by_patient_name(self):
        """Test case for find_doctor_by_patient_name

        Finds doctors by  Patients Name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/doctor/patientName/{name}'.format(name='name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_doctors(self):
        """Test case for get_all_doctors

        Get all doctors
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/doctor/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
