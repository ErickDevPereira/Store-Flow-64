from .jwt_singleton import jwt_sing
from typing import Callable
from flask import request
from flask_restful import abort
from typing import Dict, Any, Tuple
from jwt import decode, InvalidSignatureError, ExpiredSignatureError
import os

def auth_jwt() -> Tuple[str, int] | None:
    jwt: str = request.cookies.get("jwt")
    if jwt is None:
        abort(401, message = "The cookie can't be accessed!")
    try:
        payload: Dict[str, Any] = decode(jwt, key = os.getenv('JWT_KEY'), algorithms = os.getenv('JWT_ALGORITHM'))
    except InvalidSignatureError as err:
        abort(500, message = str(err))
    except ExpiredSignatureError:
        abort(401, message = "JWT expired - Unauthorized access")
    except Exception as err:
        abort(500, message = str(err))
    else:
        uid: int = payload['uid']
        new_jwt: str = jwt_sing.refresh_token(jwt) #If it is about to expire, a new token will be generated with same data, lasting 1 hour, otherwise, the same token is returned.
        return new_jwt, uid