from utils.db import create_sqlalchemy_connection_string
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from utils.db import db_envs


class DBConnectionHandler:
    def __init__(
        self,
        type=db_envs["type"],
        host=db_envs["host"],
        user=db_envs["user"],
        password=db_envs["password"],
        name=db_envs["name"],
        logs=db_envs["show_logs"],
    ) -> None:
        self.__connection_string = create_sqlalchemy_connection_string(
            type, host, user, password, name
        )
        self.__engine = self.__create_database_engine(logs)
        self.session = None

    def __create_database_engine(self, logs):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
