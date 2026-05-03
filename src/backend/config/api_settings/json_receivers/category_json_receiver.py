from flask_restful.reqparse import RequestParser, Namespace
from .json_receiver import JsonReceiver

class CategoryJsonReceiver(JsonReceiver):

    def __init__(self):
        self.create_args()
        self.set_arguments()

    def create_args(self) -> None:
        self.__args: RequestParser = RequestParser()
    
    def set_arguments(self) -> None:
        self.__args.add_argument("store-id", type = int, help = "couldn't get the store_id")
        self.__args.add_argument("category-name", type = str, help = "Couldn't get the name of the category")
        self.__args.add_argument("description", type = str, help = "Couldn't get the description")
    
    def get_args(self) -> Namespace:
        return self.__args.parse_args()