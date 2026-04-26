from flask_restful import Resource
from flask import Response, request,abort, make_response
from src.backend.config.db_settings.rsc import StrongConnection, Cursor
from src.backend.model.auth import auth_jwt
import os
from src.backend.model.db.complex_queries import ComplexQueries
from datetime import datetime
from typing import Dict

class Bridge(Resource):

    def get(self) -> Response:
        jwt, uid = auth_jwt()
        self.__store_id: int | None = request.args.get("store-id", type = int)
        if self.__store_id is None:
            abort(500, message = "ERROR: The id of the store was not found")
        with StrongConnection(os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("DB_NAME")) as scnx:
            with Cursor(scnx) as cursor:
                self.__dataset: Dict[str, int | str | datetime] = ComplexQueries().get_store_datasize(cursor, self.__store_id)
        self.__resp: Response = make_response({"data": self.__dataset}, 200)
        self.__resp.set_cookie(
            "jwt",
            value = jwt,
            max_age = 3600,
            httponly = True,
            secure = True,
            samesite = "none"
            )
        return self.__resp