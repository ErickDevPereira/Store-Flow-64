from src.backend.config.db_settings.rsc import StrongConnection, Cursor
from ..db import UserBridge
from werkzeug.security import check_password_hash
import os
from typing import Tuple, Dict, Any

class UserAuthenticator:

    def __init__(self, email: str, password: str):
        self.__email: str = email
        self.__password: str = password
    
    def is_logged(self) -> Tuple[bool, None | int]:
        self.__bridge: UserBridge = UserBridge()
        with StrongConnection(os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("DB_NAME")) as scnx:
            with Cursor(scnx) as cursor:
                #Returns (True, uid) if the user is present, (False, None) otherwise
                self.__tuple_presence: Tuple[bool, None | int] = self.__self.__bridge.user_is_present(cursor, self.__email)
                #Getting the boolean value that says if the user with this email exists or not.
                self.__present = self.__tuple_presence[0]
            if self.__present:
                with Cursor(scnx) as cursor:
                    self.__dataset: Dict[str, Any] = self.__bridge.get(cursor, self.__tuple_presence[1])
        if self.__present:
            if check_password_hash(self.__dataset["wzg_password"], self.__password):
                return True, self.__tuple_presence[1] #The user was logged successfully, so we return True, id
        return False, None