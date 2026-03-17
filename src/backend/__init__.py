from dotenv import load_dotenv

#Loading the environment variables relative to MySQL (important for connections to the database)
load_dotenv("src/backend/config/env/db.env")
load_dotenv("src/backend/config/env/jwt.env")