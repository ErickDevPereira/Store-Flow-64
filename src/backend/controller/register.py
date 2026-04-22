from typing import Dict, Any, Tuple
from flask_restful import Resource, abort
from src.backend.config.api_settings import sing_user_json_receiver
from src.backend.config.db_settings.rsc import StrongConnection, Cursor
import os
from werkzeug.security import generate_password_hash
from mysql.connector.errors import DataError, IntegrityError
from src.backend.model.db import UserBridge
from flask_restful.reqparse import Namespace

class Register(Resource):

    def post(self) -> Tuple[Dict[str, Any], int]:
        self.__JSON: Namespace = sing_user_json_receiver.get_args()
        for field in (
            self.__JSON["first_name"],
            self.__JSON["last_name"],
            self.__JSON["email"],
            self.__JSON["password"],
            self.__JSON["birthdate"]
            ):
            if field is None:
                abort(400, message = f"You've forgotten to fill the field {field}")
        #Inserting the user inside the database
        with StrongConnection(os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("DB_NAME")) as scnx:
            with Cursor(scnx) as cursor:
                try:
                    UserBridge().load(
                        cursor = cursor,
                        cnx = scnx,
                        first_name = self.__JSON["first_name"],
                        last_name = self.__JSON["last_name"],
                        wzg_pw = generate_password_hash(self.__JSON["password"]),
                        email = self.__JSON["email"],
                        bdate = self.__JSON["birthdate"]
                        )
                #DataError will raise when the format or size of the input data doesn't accomplish the type for the column.
                #IntegrityError will raise when a constraint has been broken by the input data, like a CHECK, FK or UNIQUE constraint.
                except IntegrityError as err:
                    abort(403, message = f"FORBIDDEN ERROR: {err}")
                except DataError as err:
                    abort(500, message = f"INTERNAL SERVER ERROR: {err}")
        #Response when everything went fine.
        return {"message": "User created successfully"}, 201