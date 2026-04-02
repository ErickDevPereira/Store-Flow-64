from .entity import *
from mysql.connector.abstracts import MySQLConnectionAbstract
from typing import Any, Tuple, List, Dict
import datetime

class StoreBridge(Getter, Loader, Remover):

    def load(self,
            cnx: MySQLConnectionAbstract,
            cursor: Any,
            company_name: str,
            uid: int) -> None:
        cursor.execute("INSERT INTO stores (company_name, uid, registration_date) VALUES (%s, %s, %s)",
                       (company_name, uid, str(datetime.datetime.now().date())))
        cnx.commit()

    def rm(self, cnx: MySQLConnectionAbstract, cursor: Any, store_id: int) -> None:
        cursor.execute("DELETE FROM stores WHERE store_id = %s", (store_id,))
        cnx.commit()
    
    def get_entity(self, cursor: Any, uid: int) -> List[Dict[int, Any]]:
        cursor.execute(
            """ SELECT
                    company_name, store_id, registration_date
                FROM
                    stores
                WHERE
                    uid = %s
                ORDER BY
                    store_id ASC""", (uid,)
                    )
        self.__dataset: List[Tuple[Any,...]] = cursor.fetchall()
        self.__organized_dataset = []
        for data in self.__dataset:
            self.__organized_dataset.append({"store_id": data[1], "company_name": data[0], "registration_date": str(data[2])})
        return self.__organized_dataset #The dataset is sorted by store_id in ascending mode, which allows us to use binary search in order to get the store that we need as fastest as possible.