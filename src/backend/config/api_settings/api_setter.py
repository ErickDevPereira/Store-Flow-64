from flask_restful import Api, Resource
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

class ApiSetter:
    
    def __init__(self):
        self.__create_app()
        self.__create_api()
        self.__set_orm()
    
    def __create_app(self) -> None:
        self.__app: Flask = Flask(__name__)
        CORS(self.__app, supports_credentials = True) #Allows communication of cookies between Python (backend) and JS (frontend)
    
    def __create_api(self) -> None:
        self.__api: Api = Api(self.__app)
    
    def set_rscs(self, class_rsc: Resource, route: str) -> None:
        self.__api.add_resource(class_rsc, route)

    def __set_orm(self) -> None:
        self.__app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ratelimit.db" #Set the database as sqlite
        self.__app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Avoids anoying warnings
        self.__db: SQLAlchemy = SQLAlchemy(self.__app) #sqlalchemy instance
    
    def turn_on(self) -> None:
        self.__app.run(debug = True)

    @property
    def app(self) -> Api:
        return self.__app
    
    @property
    def db(self) -> SQLAlchemy:
        return self.__db