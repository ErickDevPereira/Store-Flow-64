from src.backend.config.db_settings import Database
from src.backend.config.api_settings import ApiSetter

if __name__ == "__main__":
    db: Database = Database()
    db.start_db() #This method will initialize the database, creating it if it doesn't exist.
    api: ApiSetter = ApiSetter()
    api.turn_on() #Will start the api server.