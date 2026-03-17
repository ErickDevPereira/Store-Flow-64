from typing import Any, Tuple, List, Dict
from entity import Remover, Loader, Getter
from mysql.connector import MySQLConnectionAbstract

class UserBridge(Getter, Loader, Remover):
    
    def get(self, cursor: Any, uid: int) -> Dict[str, Any]:
        cursor.execute("""
                        SELECT
                            uid, first_name, last_name, wzg_password, email, birthdate
                        FROM
                            users
                        WHERE
                            uid = %s
                        """, (uid,))
        dirty_dataset: List[Tuple[Any]] = cursor.fetchall()
        dataset: Dict[str, Any] = {}
        if len(dirty_dataset) > 0: #Has data in it
            dataset.update({
                "uid": dirty_dataset[0][0],
                "first_name": dirty_dataset[0][1],
                "last_name": dirty_dataset[0][2],
                "wzg_password": dirty_dataset[0][3],
                "email": dirty_dataset[0][4],
                "birthdate": dirty_dataset[0][5]
            })
        return dataset

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
        cursor.execute("DELETE FROM users WHERE uid = %s", (uid,))
        cnx.commit()

    def user_is_present(self, cursor: Any, email: str) -> Tuple[bool, None] | Tuple[bool, int]:
        cursor.execute(
                    """
                        SELECT
                            uid
                        FROM
                            users
                        WHERE
                            email = %s 
                    """, (email,))
        self.__user: List[Tuple[str]] = cursor.fetchall()
        if not len(self.__user) == 0: #The list is empty so there is no user with such email
            return False, None
        return True, self.__user[0][0] #If we got here, the user is present, so we return his/her id.