from .json_receiver import JsonReceiver
from flask_restful.reqparse import RequestParser, Namespace
from typing import Callable

class SupplierJsonReceiver(JsonReceiver):

    FIELD: Callable[[str], str] = lambda field: f"{field} has been blocked"

    def __init__(self):
        self.create_args()
        self.set_arguments()

    def create_args(self) -> None:
        self.__args = RequestParser()
    
    def set_arguments(self) -> None:
        self.__args.add_argument("company-name", type = str, help = SupplierJsonReceiver.FIELD("company-name"))
        self.__args.add_argument("country", type = str, help = SupplierJsonReceiver.FIELD("country"))
        self.__args.add_argument("city", type = str, help = SupplierJsonReceiver.FIELD("city"))
        self.__args.add_argument("phone", type = str, help = SupplierJsonReceiver.FIELD("phone"))
        self.__args.add_argument("address", type = str, help = SupplierJsonReceiver.FIELD("address"))
        self.__args.add_argument("store-id", type = int, help = SupplierJsonReceiver.FIELD("store-id"))

    def get_args(self) -> Namespace:
        return self.__args.parse_args()