from typing import Tuple
from flask_restful import Resource, abort
from flask import request, make_response, Response
from src.backend.model.auth import UserAuthenticator
from src.backend.model.auth import jwt_sing
from src.backend.model.rate_limit import process_rate_out
from time import time
from flask_restful.reqparse import Namespace
from src.backend.config.api_settings import sing_login_json_receiver

class Login(Resource):

    def post(self) -> Response:
        self.__JSON: Namespace = sing_login_json_receiver.get_args()
        #process_rate_out(self.__JSON['ip'])
        self.__dataset: Tuple[str, ...] = (self.__JSON["email"], self.__JSON["password"], self.__JSON['ip'])
        #Avoiding None situations
        for data in self.__dataset:
            if data is None:
                abort(400, message = f"ERROR: All values must be filled")
        #The following code returns (True, user id) if that email and password are present in the database and they match, but returns (False, None) otherwise
        self.__login_status: Tuple[bool, int | None] = UserAuthenticator(self.__JSON["email"], self.__JSON["password"]).is_logged()
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