from flask_restful.reqparse import Namespace, RequestParser
from .json_receiver import JsonReceiver

class StoreJsonReceiver(JsonReceiver):

    def __init__(self):
        self.create_args()
        self.set_arguments()

    def create_args(self) -> None:
        self.__args: RequestParser = RequestParser()
    
    def get_args(self) -> Namespace:
        return self.__args.parse_args()

    def set_arguments(self) -> None:
        self.__args.add_argument("company_name", type = str, help = "Something went wrong at first_name")