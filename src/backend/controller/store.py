from flask_restful import Resource, abort, reqparse
from flask_restful.reqparse import Namespace
from src.backend.config.api_settings import sing_store_json_receiver
from src.backend.model.db import StoreBridge
from mysql.connector.errors import DataError, IntegrityError
from src.backend.config.db_settings.rsc import StrongConnection, Cursor
import os
from flask import make_response, Response
from src.backend.model.auth import auth_jwt
from typing import Dict, Any

class Store(Resource):

    def post(self):
        jwt, uid = auth_jwt() #Authenticating the cookies and jwt
        self.__JSON: Namespace = sing_store_json_receiver.get_args()
        if self.__JSON["company_name"] is None:
            abort(400, message = "you msut give the 'company_name'")
        self.__sb: StoreBridge = StoreBridge()
        with StrongConnection(os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("DB_NAME")) as scnx:
            with Cursor(scnx) as cursor:
                try:
                    self.__sb.load(
                                cnx = scnx,
                                cursor = cursor,
                                company_name = self.__JSON["company_name"],
                                uid = uid
                    )
                except DataError:
                    abort(403, message = "The name of the company is too large")
                except IntegrityError:
                    abort(400, message = "The field must be filled")
        self.__resp: Response = make_response({"message": "Store accepted"}, 201)
        self.__resp.set_cookie(
            key = "jwt",
            value = jwt,
            max_age = 3600,
            httponly = True,
            secure = True,
            samesite = "none"
        )
        return self.__resp
