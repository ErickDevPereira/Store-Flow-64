from src.backend.config.db_settings.rsc import Cursor, WeakConnection, StrongConnection
from typing import Dict, List, Any, Tuple
import os
from datetime import datetime

class ComplexQueries:

    @staticmethod
    def get_store_datasize(db_cursor: Any, store_id: int) -> Dict[str, int | str | datetime]:
        db_cursor.execute("""
                SELECT
                    store_id,
                    company_name,
                    registration_date,
                    (SELECT
                        COUNT(ct.category_id)
                    FROM
                        stores AS st LEFT JOIN categories AS ct ON ct.store_id = st.store_id
                    GROUP BY
                        st.store_id
                    HAVING 
                        st.store_id = %s) AS category_qtt,
                    (SELECT
                        COUNT(cust.customer_id)
                    FROM
                        stores AS st LEFT JOIN customers AS cust ON cust.store_id = st.store_id
                    GROUP BY
                        st.store_id
                    HAVING 
                        st.store_id = %s) AS customer_qtt,
                    (SELECT
                        COUNT(emp.employee_id)
                    FROM
                        stores AS st LEFT JOIN employees AS emp ON emp.store_id = st.store_id
                    GROUP BY
                        st.store_id
                    HAVING 
                        st.store_id = %s) AS employees_qtt,
                    (SELECT
                        COUNT(pr.product_id)
                    FROM
                        stores AS st LEFT JOIN products AS pr ON pr.store_id = st.store_id
                    GROUP BY
                        st.store_id
                    HAVING 
                        st.store_id = %s) AS product_qtt,
                    (SELECT
                        COUNT(sup.supplier_id)
                    FROM
                        stores AS st LEFT JOIN suppliers AS sup ON sup.store_id = st.store_id
                    GROUP BY
                        st.store_id
                    HAVING 
                        st.store_id = %s) AS supplier_qtt
                FROM
                    stores
                WHERE
                    store_id = %s
            """, (store_id,) * 6)
        dirty_data: List[Tuple[int, str, str, int, int, int, int, int]] = db_cursor.fetchall()
        cleaned_data: Dict[str, int | str | datetime] = {
            "store_id" : dirty_data[0][0],
            "company_name": dirty_data[0][1],
            "reg_date": str(dirty_data[0][2]),
            "category_qtt": dirty_data[0][3],
            "customer_qtt": dirty_data[0][4],
            "employees_qtt": dirty_data[0][5],
            "product_qtt": dirty_data[0][6],
            "supplier_qtt": dirty_data[0][7]
        }
        return cleaned_data