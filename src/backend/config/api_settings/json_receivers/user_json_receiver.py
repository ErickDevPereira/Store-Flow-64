from flask_restful import reqparse
from .json_receiver import JsonReceiver

class UserJsonReceiver(JsonReceiver):

    def __init__(self):
        self.__create_args()
        self.__set_arguments()

    def __create_args(self) -> None:
        self.__args: reqparse.RequestParser = reqparse.RequestParser()
    
    def get_args(self) -> reqparse.RequestParser:
        return self.__args

    def __set_arguments(self) -> None:
        self.__args.add_argument("first_name", type = str, help = "Something went wrong at first_name")
        self.__args.add_argument("last_name", type = str, help = "Something went wrong at lastt_name")
        self.__args.add_argument("password", type = str, help = "Something went wrong at password")
        self.__args.add_argument("email", type = str, help = "Something went wrong at password")
        self.__args.add_argument("birthdate", type = str, help = "Something went wrong at birthdate")