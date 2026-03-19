import datetime
from jwt import encode, decode
import os
from typing import Any, Dict

class JwtEngine:

    def __init__(self,
                key: str | None = os.getenv("JWT_KEY"),
                algorithm: str | None = os.getenv("JWT_ALGORITHM"),
                exp_time_minutes: str | None = os.getenv("JWT_EXP_TIME_MINUTES")):
        self.__key: str | None = key
        self.__alg: str | None = algorithm
        self.__exp: str | None = exp_time_minutes
        for cred in (self.__key, self.__alg, self.__exp):
            if cred is None:
                raise ValueError("ERROR: You must difine the JWT_KEY, JWT_ALGORITHM and JWT_EXP_TIME_MINUTES inside the jwt.env file")
    
    def __create_token(self, uid: int) -> str:
        return encode({
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes = int(self.__exp)),
            "uid": uid
            }, key = self.__key, algorithm = self.__alg)
    
    def get_token(self, uid: int) -> str:
        return self.__create_token(uid)
    
    def refresh_token(self, jwt_token: str, remaining_time_minutes: int = 15) -> str:
        self.__payload: Dict[str, Any] = decode(jwt_token, key = self.__key, algorithms = self.__alg)
        if datetime.datetime.utcfromtimestamp(self.__payload["exp"]) - datetime.datetime.utcnow() < datetime.timedelta(minutes = remaining_time_minutes):
            return self.get_token(self.__payload["uid"]) #Returns a new token for this user if the time is going out.
        return jwt_token #Returns the same token if it will last for a good time