# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.appointment import Appointment  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_appointment(self):
        """Test case for add_appointment

        Add a new appointment to the database
        """
        body = {
  "doctor" : "doctor",
  "date" : "2000-01-23T04:56:07.000+00:00",
  "patientName" : "patientName",
  "issue" : "issue",
  "id" : 0,
  "clinic" : "clinic"
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/appointment/',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_appointment(self):
        """Test case for delete_appointment

        Deletes an Appointment
        """
        headers = { 
        }
        response = self.client.open(
            '/api/v1/appointment/{id}'.format(id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_edit_appointment(self):
        """Test case for edit_appointment

        Update an existing appointment
        """
        body = {
  "doctor" : "doctor",
  "date" : "2000-01-23T04:56:07.000+00:00",
  "patientName" : "patientName",
  "issue" : "issue",
  "id" : 0,
  "clinic" : "clinic"
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/appointment/{id}'.format(id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_appointments_by_doctor_name(self):
        """Test case for find_appointments_by_doctor_name

        Finds Appointments by doctor name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/appointment/doctor/{name}'.format(name='name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_appointments_by_patient_name(self):
        """Test case for find_appointments_by_patient_name

        Finds Appointments by patient name
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/appointment/patient/{name}'.format(name='name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_appointments(self):
        """Test case for get_all_appointments

        Get all appointments
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/appointment/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
