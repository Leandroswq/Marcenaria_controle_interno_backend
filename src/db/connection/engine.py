import os
import sqlalchemy
from dotenv import load_dotenv

load_dotenv()

db_type = os.getenv("DB_TYPE")
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_show_logs = True if os.getenv("DB_SHOW_LOGS") == "True" else False

connection_string = ""

if db_type == "sqlite":
    # Gera a string de conexão para o SQLite
    connection_string = f"sqlite:///{db_name}"
else:
    # Gera a string de conexão para o MySQL
    connection_string = (
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
    )


engine = sqlalchemy.create_engine(connection_string, echo=db_show_logs)
