from database_connection import GetDBConnection
from schema import LoginInput


def verify_user_login(login_input: LoginInput):
    user_name = login_input.user_name
    password = login_input.password
    fetch_user_query = f"SELECT user_name, user_password FROM app_db.users WHERE user_name = '{user_name}'"
    try:
        with GetDBConnection().connect() as _mysql_connection:
            _mysql_cursor = _mysql_connection.cursor()
            _mysql_cursor.execute(fetch_user_query)
            _record = _mysql_cursor.fetchone()
            if _record and _record[1] == password:
                return True
    except Exception as e:
        print(f"Error in establishing connection to mysql : {e}")
    return False
