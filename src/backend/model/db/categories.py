from .entity import Remover, Loader, Getter
from mysql.connector.abstracts import MySQLConnectionAbstract
from typing import Any, List, Tuple

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

    def get_entity(
            cursor: Any,
            cat_name: str,
            store_id: int) -> List[Tuple[str, int]] | None:
        cursor.execute("""
                        SELECT
                            category_name, description
                        FROM
                            categories
                        WHERE
                            category_name = %s AND store_id = %s""",
                        (cat_name, store_id))
        data: List[Tuple[str, int]] = cursor.fetchall()
        return {
            "category-name" : data[0][0],
            "desc" : data[0][1]
        } if len(data) != 0 else None