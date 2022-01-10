# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.credentials import Credentials  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_auth_doctor(self):
        """Test case for auth_doctor

        Authorize a doctor
        """
        body = {
  "password" : "password",
  "username" : "username"
}
        headers = { 
            'Accept': 'text/plain',
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

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_auth_patient(self):
        """Test case for auth_patient

        Authorize a patient
        """
        body = {
  "password" : "password",
  "username" : "username"
}
        headers = { 
            'Accept': 'text/plain',
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


if __name__ == '__main__':
    unittest.main()
