from src.backend.config.db_settings import Database
from src.backend.config.api_settings import api
import src.backend.config.orm #Call the script that will initialize sqlite

mysql_db: Database = Database()
mysql_db.start_db() #This method will initialize the MySQL database, creating it if it doesn't exist.
api.turn_on() #Will start the api server.