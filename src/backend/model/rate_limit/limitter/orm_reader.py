from src.backend.config.orm import NetworkConnection, Address, db
from flask_sqlalchemy.query import Query
from typing import Any, List, Dict
from datetime import datetime, timedelta

class ORMReader:

    ERROR = "ERROR: HTTP request wasn't indetified in sqlite"

    @staticmethod
    def __query_by_ip(network_ip: str) -> List[Dict[str, Any]] | None:
        ip_obj = Address.query.filter_by(network_ip = network_ip).first()
        if ip_obj is None:
            return None
        dataset = ip_obj.address_rl
        organized_dataset = list()
        if dataset is not None:
            for request in dataset:
                organized_dataset.append({
                    "datetime": request.event_date
                    })
            return organized_dataset
        return None
    
    @classmethod
    def has_many_requests(cls, network_ip: str, max_frequency: int) -> bool:
        count = 0
        dataset = cls.__query_by_ip(network_ip)
        if dataset is None:
            raise Exception(cls.ERROR)
        for request in dataset:
            if datetime.utcnow() - request["datetime"] < timedelta(seconds = 60):
                count += 1
        if count > max_frequency:
            return True
        return False

    @staticmethod
    def is_authorized(network_ip: str) -> bool | None:
        address = Address.query.filter_by(network_ip=network_ip).first()
        if address is None:
            return None #This IP is new
        if address.blocked_status == 1:
            return False
        return True
    
    @classmethod
    def beyond_block_time(cls, network_ip: str, max_blocking_minutes: int = 60) -> bool | None:
        dataset = cls.__query_by_ip(network_ip)
        if dataset is None:
            raise Exception(cls.ERROR)
        for request in dataset:
            if datetime.utcnow() - request['datetime'] > timedelta(minutes = max_blocking_minutes):
                return True #It is allowed to be free
        return False #Must be still blocked
    
    @classmethod
    def toggle_authorization(cls, network_ip: str) -> None:
        ip_obj = Address.query.filter_by(network_ip = network_ip).first()
        if ip_obj is None:
            raise Exception(cls.ERROR)
        ip_obj.blocked_status = 0 if ip_obj.blocked_status == 1 else 1
        db.session.commit()