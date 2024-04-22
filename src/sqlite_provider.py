import sqlite3


class SQLiteProvider(object):

    @staticmethod
    def read(target, column_names=None, table="content"):
        with sqlite3.connect(target) as conn:
            cursor = conn.cursor()
            cols = "*" if column_names is None else ",".join(column_names)
            cursor.execute(f"SELECT {cols} FROM {table}")
            for row in cursor:
                yield row

    @staticmethod
    def get_columns(target, table="content"):
        with sqlite3.connect(target) as conn:
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({table})")
            return [row[1] for row in cursor.fetchall()]
