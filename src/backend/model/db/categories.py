from .entity import Remover, Loader, Getter
from mysql.connector.abstracts import MySQLConnectionAbstract
from typing import Any, List, Tuple, Dict

class CategoryBridge(Getter, Loader, Remover):

    def rm(self,
            db_scnx: MySQLConnectionAbstract,
            cursor: Any,
            cat_id: int) -> None:
        cursor.execute("DELETE FROM categories WHERE category_id = %s", (cat_id,))
        db_scnx.commit()

    def load(self,
            db_scnx: MySQLConnectionAbstract,
            cursor: Any,
            cat_name: str,
            description: str,
            store_id: int) -> None:
        cursor.execute("INSERT INTO categories (category_name, description, store_id) VALUES (%s, %s, %s)",
                       (cat_name, description, store_id))
        db_scnx.commit()

    def get_entity(self,
            cursor: Any,
            cat_name: str,
            store_id: int) -> Dict[int, str, str] | None:
        cursor.execute("""
                        SELECT
                            category_id, category_name, description
                        FROM
                            categories
                        WHERE
                            category_name = %s AND store_id = %s""",
                        (cat_name, store_id))
        data: List[Tuple[str, int]] = cursor.fetchall()
        return {
            "category-id" : data[0][0],
            "category-name" : data[0][1],
            "desc" : data[0][2]
        } if len(data) != 0 else None