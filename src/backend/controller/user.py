from typing import Dict, Any, List, Tuple
from flask_restful import Resource
from src.backend.config import sing_user_json_receiver

class User(Resource):
    
    def get(self) -> Tuple[Dict[str, Any], int]:
        pass

    def post(self) -> Tuple[Dict[str, Any], int]:
        pass