from flask_restful import abort
from .limitter import ORMReader, ORMWriter
from src.backend.config.api_settings import api

def process_rate_out(ip: str) -> None:
    authorization = ORMReader.is_authorized(ip)
    if authorization is not None:
        if not authorization:
            free = ORMReader.beyond_block_time(ip)
            if not free:
                abort(403, message = "Unauthorized access")
            else:
                ORMReader.toggle_authorization(ip)
    address = ORMWriter.load_request_log(network_ip=ip) #Loading the IP address and data about the request and getting the address
    signal = ORMReader.has_many_requests(network_ip=ip, max_frequency=20) #Checking if this IP exceeded the limit frequency
    if signal:
        address.blocked_status = 1 #Blocking the IP
        api.db.session.commit()
        abort(429, message = "Too many requests")