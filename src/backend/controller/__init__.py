from .store import Store
from .register import Register
from .login import Login
from src.backend.config.api_settings import api

api.set_rscs(Store, "/store")
api.set_rscs(Register, "/register")
api.set_rscs(Login, "/login")