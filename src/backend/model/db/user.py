from typing import Any, Tuple, List
from entity import Remover, Loader, Getter
from mysql.connector import MySQLConnectionAbstract

class UserBridge(Getter, Loader, Remover):
    
    def get(self): pass #Will be implemented in the future

    def load(self,
            cnx: MySQLConnectionAbstract,
            cursor: Any,
            first_name: str,
            last_name: str,
            wzg_pw: str,
            email: str,
            bdate: str) -> None:
        cursor.execute("""
                    INSERT INTO users (first_name, last_name, wzg_password, email, birthdate) VALUES
                    (%s, %s, %s, %s, %s)""", (first_name, last_name, wzg_pw, email, bdate))
        cnx.commit()
    
    def rm(self, cnx: MySQLConnectionAbstract, cursor: Any, uid: int) -> None:
        cursor.execute("DELETE FROM users WHERE uid = %s", uid)
        cnx.commit()

