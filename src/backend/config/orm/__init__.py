from .settings import Address, NetworkConnection
from src.backend.config.api_settings import api

with api.app.app_context():
    api.db.create_all() #Creating the database