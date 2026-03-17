from typing import Dict, Any, List, Tuple
from flask_restful import Resource, reqparse, abort
from src.backend.config import sing_user_json_receiver
from src.backend.config.db_settings.rsc import WeakConnection, StrongConnection, Cursor
import os
from werkzeug.security import generate_password_hash
from mysql.connector.errors import DataError, IntegrityError
from src.backend.model.db import UserBridge

class User(Resource):
    
    def get(self) -> Tuple[Dict[str, Any], int]:
        pass

    def post(self) -> Tuple[Dict[str, Any], int]:
        self.__JSON: reqparse.RequestParser = sing_user_json_receiver.get_args()
        for field in (
            self.__JSON["first_name"],
            self.__JSON["last_name"],
            self.__JSON["email"],
            self.__JSON["password"],
            self.__JSON["birthdate"]
            ):
            if field is None:
                abort(400, message = f"You've forgotten to fill the field {field}")
        with StrongConnection(os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("DB_NAME")) as scnx:
            with Cursor(scnx) as cursor:
                try:
                    UserBridge().load(
                        cursor = cursor,
                        first_name = self.__JSON["first_name"],
                        last_name = self.__JSON["last_name"],
                        wzg_pw = generate_password_hash(self.__JSON["password"]),
                        email = self.__JSON["email"],
                        bdate = self.__JSON["birthdate"]
                        )
                except (DataError, IntegrityError) as err:
                    abort(400, message = f"ERROR: {err}")
        
        return {"message": "User created successfully"}, 201