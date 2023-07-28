import os
from dotenv import load_dotenv

load_dotenv()

db_envs = {
    "type": os.getenv("DB_TYPE"),
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "name": os.getenv("DB_NAME"),
    "show_logs": True if os.getenv("DB_SHOW_LOGS") == "True" else False,
}


def create_sqlalchemy_connection_string(
    type=db_envs["type"],
    host=db_envs["host"],
    user=db_envs["user"],
    password=db_envs["password"],
    name=db_envs["name"],
):
    if type == "sqlite":
        # Gera a string de conexão para o SQLite
        connection_string = f"sqlite:///{name}"
    else:
        # Gera a string de conexão para o MySQL
        connection_string = f"mysql+pymysql://{user}:{password}@{host}/{name}"
    return connection_string
