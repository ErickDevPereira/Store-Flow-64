from src.backend.config.orm import NetworkConnection, Address
from src.backend.config.api_settings import api
from datetime import datetime
from sqlalchemy.exc import IntegrityError

class ORMWriter:

    @staticmethod
    def load_request_log(network_ip: str, logged_in: int = 0, log_date: str = datetime.utcnow()) -> None:
        try:
            ip_obj: Address = Address(network_ip = network_ip, blocked_status = 0)
            api.db.session.add(ip_obj)
            api.db.session.commit()
        except IntegrityError:
            api.db.session.rollback() #That ip is already present so we pass this piece of code
        address = Address.query.filter_by(network_ip = network_ip).first()
        http_request: NetworkConnection = NetworkConnection(address_id = address.address_id, logged_in = logged_in, event_date = log_date)
        api.db.session.add(http_request) #Adding a new log
        api.db.session.commit() #Comitting the creation
        return address