from .json_receiver import JsonReceiver
from flask_restful.reqparse import RequestParser, Namespace

class LoginJsonReceiver(JsonReceiver):

    def __init__(self):
        self.create_args()
        self.set_arguments()

    def create_args(self) -> None:
        self.__args: RequestParser = RequestParser()
    
    def get_args(self) -> Namespace:
        return self.__args.parse_args()

    def set_arguments(self) -> None:
        self.__args.add_argument("ip", type = str, help = "Something went wrong at ip")
        self.__args.add_argument("email", type = str, help = "Something went wrong at email")
        self.__args.add_argument("password", type = str, help = "Something went wrong at password")