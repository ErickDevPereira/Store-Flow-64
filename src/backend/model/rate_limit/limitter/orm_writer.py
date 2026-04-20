from src.backend.config.orm import db, NetworkConnection, Address
from datetime import datetime
from sqlalchemy.exc import IntegrityError

class ORMWriter:

    @staticmethod
    def load_request_log(network_ip: str, logged_in: int = 0, log_date: str = datetime.utcnow()) -> None:
        try:
            ip_obj: Address = Address(network_ip = network_ip, blocked_status = 0)
            db.session.add(ip_obj)
            db.session.commit()
        except IntegrityError:
            pass #That ip is already present so we pass this piece of code
        address = Address.query.filter_by(network_ip = network_ip).first()
        http_request: NetworkConnection = NetworkConnection(address_id = address.address_id, logged_in = logged_in, event_date = log_date)
        db.session.add(http_request) #Adding a new log
        db.session.commit() #Comitting the creation
        return address