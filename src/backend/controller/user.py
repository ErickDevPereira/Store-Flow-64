from typing import Dict, Any, Tuple
from flask_restful import Resource, abort
from src.backend.config.api_settings import sing_user_json_receiver
from src.backend.config.db_settings.rsc import StrongConnection, Cursor
import os
from werkzeug.security import generate_password_hash
from mysql.connector.errors import DataError, IntegrityError
from src.backend.model.db import UserBridge
from flask import request, make_response, Response
from src.backend.model.auth import UserAuthenticator
from src.backend.model.auth import jwt_sing
from flask_restful.reqparse import Namespace
from src.backend.model.rate_limit import process_rate_out

class User(Resource):
    
    def get(self) -> Response:
        self.__email: str = request.args.get("email", type = str)
        self.__pw: str = request.args.get("password", type = str)
        self.__dataset: Tuple[str, ...] = (self.__email, self.__pw)
        #Avoiding None situations
        for data in self.__dataset:
            if data is None:
                abort(400, message = f"ERROR: All values must be filled")
        #The following code returns (True, user id) if that email and password are present in the database and they match, but returns (False, None) otherwise
        self.__login_status: Tuple[bool, int | None] = UserAuthenticator(self.__email, self.__pw).is_logged()
        #If the user isn't present or is present but the password doesn't match with that one inside the database, an abort will happen.
        if not self.__login_status[0]:
            abort(404, message = "This combination of email-password doesn't exist")
        #This part of the code will run if the credentials of that user are allowed
        self.__uid: int = self.__login_status[1] #Id of the user will be at the second position of the tuple
        #This uid will go to a JWT token, which will be sent to the cookies of the client-side browser, allowing authentication and user session.
        self.__jwt: str = jwt_sing.get_token(self.__uid) #Getting the cookie from the singleton
        self.__response: Response = make_response({"message": "authorized"}, 200)
        self.__response.set_cookie(
            key = "jwt",
            value = self.__jwt,
            max_age = 3600,
            secure = True,
            samesite = "none",
            httponly = True
        ) #Setting a cookie with the JWT
        return self.__response

    def post(self) -> Tuple[Dict[str, Any], int]:
        ip: str | None = request.args.get("ip", type = str)
        if ip is None:
            raise Exception("Problem while catching the IP of the user!")
        process_rate_out(ip)
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