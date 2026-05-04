from .endpoint_entity import EndpointsEntity
from flask import Response, make_response
from flask_restful import Resource, abort
from src.backend.model.auth import auth_jwt
from src.backend.config.db_settings.rsc import StrongConnection, Cursor
import os
from src.backend.config.api_settings.json_singletons import sing_sup_json_receiver
from flask_restful.reqparse import Namespace
from typing import List
from src.backend.model.db import SupplierBridge
from mysql.connector.errors import IntegrityError

class EndpointsSuppliers(Resource, EndpointsEntity):

    def get(self) -> Response:
        pass

    def post(self) -> Response:
        jwt, uid = auth_jwt()
        self.__JSON: Namespace = sing_sup_json_receiver().get_args()
        self.__store_id: int | None = self.__JSON["store-id"]
        self.__cname: str | None = self.__JSON["company-name"]
        self.__city: str | None = self.__JSON["city"]
        self.__phone: str | None = self.__JSON["phone"]
        self.__address: str | None = self.__JSON["address"]
        self.__country: str | None = self.__JSON["country"]
        for field in (self.__store_id,
                    self.__cname,
                    self.__city,
                    self.__phone,
                    self.__address,
                    self.__country):
            if field is None:
                abort(400, message = "You must fill all fields")
        self.__repeated_name: bool = False
        self.__server_trouble: bool = False
        with StrongConnection(os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("DB_NAME")) as scnx:
            with Cursor() as cursor:
                try:
                    SupplierBridge().load(
                        db_scnx = scnx,
                        cursor = cursor,
                        company_name = self.__cname,
                        country = self.__country,
                        city = self.__city,
                        phone = self.__phone,
                        address = self.__address,
                        store_id = self.__store_id
                    )
                except IntegrityError:
                    self.__repeated_name = True
                except Exception as err:
                    print(err)
                    self.__server_trouble = True
        if self.__repeated_name:
            abort(403, message = f"'f{self.__cname}' has been used before. You must implement a new name")
        if self.__server_trouble:
            abort(500, message = "Internal Server Error at suppliers table")
        self.__resp: Response = make_response(201, {
            "message" : f"'{self.__cname}' was created successfully"
        })
        self.__resp.set_cookie(
            "jwt",
            value = jwt,
            max_age = 3600,
            httponly = True,
            secure = True,
            samesite = "none"
        )
        return self.__resp
        

    def delete(self) -> Response:
        pass

    def patch(self) -> Response:
        pass