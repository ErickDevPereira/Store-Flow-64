from .entity import Remover, Loader, Getter
from mysql.connector.abstracts import MySQLConnectionAbstract
from typing import Any, List, Tuple, Dict

class SupplierBridge(Getter, Loader, Remover):

    def load(self,
            db_scnx: MySQLConnectionAbstract,
            cursor: Any,
            company_name: str,
            country: str,
            city: str,
            phone: str,
            address: str,
            store_id: int
        ) -> None:
        cursor.execute("INSERT INTO suppliers (company_name, country, city, phone, address, store_id) VALUES(%s, %s, %s, %s, %s, %s)",
                       (company_name, country, city, phone, address, store_id))
        db_scnx.commit()
    
    def rm(self,
           db_scnx: MySQLConnectionAbstract,
           cursor: Any,
           sup_id: int) -> None:
        cursor.execute("DELETE FROM suppliers WHERE supplier_id = %s", (sup_id,))
        db_scnx.commit()
    
    def get_entity(self,
                   cursor: Any,
                   sup_name: str,
                   store_id: int) -> Dict[str, str] | None:
        cursor.execute("""
                SELECT
                    supplier_id, company_name, country, city, phone, address
                FROM
                    suppliers
                WHERE
                    company_name = %s AND store_id = %s
            """, (sup_name, store_id))
        data: List[Tuple[int, str, str, str, str, str]] = cursor.fetchall()
        return {
            "sup-id" : data[0][0],
            "supplier-name" : data[0][1],
            "country" : data[0][2],
            "city" : data[0][3],
            "phone" : data[0][4],
            "address" : data[0][5]
        } if len(data) != 0 else None