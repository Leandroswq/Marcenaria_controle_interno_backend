from db import create_sqlalchemy_connection_string


def test_create_sqlalchemy_connection_string():
    # Test SQLite connection string
    sqlite_connection_string = create_sqlalchemy_connection_string(
        "sqlite", "test.db", "", "", ""
    )
    assert sqlite_connection_string == "sqlite:///test.db"

    # Test MySQL connection string
    mysql_connection_string = create_sqlalchemy_connection_string(
        "mysql",
        "db_name",
        "localhost",
        "user",
        "password",
    )
    assert (
        mysql_connection_string
        == "mysql+pymysql://user:password@localhost/db_name"
    )
