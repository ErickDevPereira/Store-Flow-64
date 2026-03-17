from src.backend.controller.user import User
from flask_restful import Api, reqparse
from flask import Flask
from flask_cors import CORS

class ApiSetter:

    def __init__(self):
        self.__create_app()
        self.__create_api()
        self.__set_rscs()
    
    def __create_app(self) -> None:
        self.__app: Flask = Flask(__name__)
        CORS(self.__app, set_credentials = True) #Allows communication of cookies between Python (backend) and JS (frontend)
    
    def __create_api(self) -> None:
        self.__api: Api = Api(self.__app)
    
    def __set_rscs(self) -> None:
        self.__api.add_resource(User, "/user")
    
    def turn_on(self) -> None:
        self.__app.run(debug = True)