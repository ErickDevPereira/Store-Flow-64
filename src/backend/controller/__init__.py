from .store import Store
from .user import User
from src.backend.config.api_settings import api

api.set_rscs(Store, "/store")
api.set_rscs(User, "/user")