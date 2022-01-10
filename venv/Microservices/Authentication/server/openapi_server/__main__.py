#!/usr/bin/env python3

import connexion

from openapi_server import encoder
from  .extensions import mongo
from .main import main as main1

def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Cloud Gate Consulting Hospital Management System'},
                pythonic_params=True)



    app.app.register_blueprint(main1)
    app.run()


if __name__ == '__main__':
    main()
