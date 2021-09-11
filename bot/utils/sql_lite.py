import sqlite3

class Database:
    def __init__(self, path_to_db="data/main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()

        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id int NOT NULL,
        Name varchar(255) NOT NULL,
        groupi varchar(255),
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_user(self, id: int, name: str, groupi: str = None):
        sql = "INSERT INTO Users(id, Name, groupi) VALUES(?, ?, ?)"
        parameters = (id, name, groupi)
        self.execute(sql, parameters=parameters, commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_email(self, email, id):
        sql = "UPDATE Users set email=? WHERE id=?"
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_user(self):
        self.execute("DELETE FROM Users WHERE True")

    def update_group(self, groupi, id):
        sql = "UPDATE Users set groupi=? WHERE id=?"
        return self.execute(sql, parameters=(groupi, id), commit=True)

    def get_developer_info(self, id):
        try:
            sqlite_connection = sqlite3.connect(self.path_to_db)
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")

            sql_select_query = """SELECT * FROM Users WHERE id = ?"""
            cursor.execute(sql_select_query, (id,))
            records = cursor.fetchall()
            print("Вывод ID ", id)
            for row in records:
                print("ID:", row[0])
                print("Имя:", row[1])
                print("Группа:", row[2], end="\n\n")

            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")

    def get_group_info(self, **kwargs):
        sql = "SELECT groupi FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def get_id_group(self, **kwargs):
        sql = "SELECT id FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)


def logger(statement):
    print(f"Вот так вот: {statement}")
