from flask_restful.reqparse import RequestParser, Namespace
from .json_receiver import JsonReceiver

class UserJsonReceiver(JsonReceiver):

    def __init__(self):
        self.create_args()
        self.set_arguments()

    def create_args(self) -> None:
        self.__args: RequestParser = RequestParser()
    
    def get_args(self) -> Namespace:
        return self.__args.parse_args()

    def set_arguments(self) -> None:
        self.__args.add_argument("first_name", type = str, help = "Something went wrong at first_name")
        self.__args.add_argument("last_name", type = str, help = "Something went wrong at lastt_name")
        self.__args.add_argument("password", type = str, help = "Something went wrong at password")
        self.__args.add_argument("email", type = str, help = "Something went wrong at password")
        self.__args.add_argument("birthdate", type = str, help = "Something went wrong at birthdate")