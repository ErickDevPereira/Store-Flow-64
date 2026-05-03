from .endpoint_entity import EndpointsEntity
from flask import Response, make_response
from flask_restful import Resource, abort
from flask_restful.reqparse import Namespace
from src.backend.model.auth import auth_jwt
from src.backend.config.db_settings.rsc import StrongConnection, Cursor
import os
from typing import Dict
from src.backend.model.db import CategoryBridge
from src.backend.config.api_settings import sing_category_json_receiver
from mysql.connector.errors import IntegrityError

class EndpointsCategories(Resource, EndpointsEntity):

    def get(self) -> Response:
        pass

    def post(self) -> Response:
        jwt, uid = auth_jwt()
        self.__JSON: Namespace = sing_category_json_receiver.get_args() #Getting the JSON from the frontend
        self.__store_id: int = self.__JSON["store-id"]
        self.__cat_name: str = self.__JSON["category-name"]
        self.__desc: str = self.__JSON["description"]
        for field in (self.__store_id, self.__cat_name, self.__desc):
            if field is None:
                abort(400, message = "You must fill all fields")
        self.__repeated_item: bool = False
        self.__server_error: bool = False
        with StrongConnection(os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("DB_NAME")) as scnx:
            with Cursor(scnx) as cursor:
                cb: CategoryBridge = CategoryBridge()
                try:
                    cb.load(db_scnx = scnx,
                            cursor = cursor,
                            cat_name = self.__cat_name,
                            description = self.__desc,
                            store_id = self.__store_id)
                except IntegrityError:
                    self.__repeated_item = True #Repeated name
                except Exception as err:
                    print(err)
                    self.__server_error = True #Unknowm error
        if self.__repeated_item:
            abort(403, message = "This name already exist")
        if self.__server_error:
            abort(500, message = "Server Error: something went wrong on the category table")
        self.__resp = make_response({"message": f"Category '{self.__cat_name}' created successfully"}, 201)
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