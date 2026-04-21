from src.backend.config.db_settings import Database
from src.backend.config.api_settings import api
import src.backend.controller #Script that sets the resources
import src.backend.config.orm #Script that sets the ORM for rate limiting. SQLite was used here
#The data concerning the users and stores will be placed inside the MySQL, without ORM.

mysql_db: Database = Database()
mysql_db.start_db() #This method will initialize the MySQL database, creating it if it doesn't exist.
api.turn_on() #Will start the api server.