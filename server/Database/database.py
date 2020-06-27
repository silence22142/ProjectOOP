import sqlite3


class Database:
    def __init__(self, name=None):
        self.conn = None
        self.cursor = None

        if name:
            self.open(name)

    def open(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Error connecting to database")

    def close(self):
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def get(self, table, column_1, column_2, id):
        query = "SELECT {0} FROM {1} WHERE {2} = {3}".format(column_1, table, column_2, id)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows[0][0]

    def get_all(self, table):
        query = "SELECT * FROM {0}".format(table)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def write(self, table, columns, data):
        query = "INSERT INTO {0} ({1}) VALUES ({2});".format(table, columns, data)
        self.cursor.execute(query)
        self.conn.commit()

    def update(self, table, column_1, data_1, column_2, data_2):
        query = "UPDATE {0} SET {1} = {2} WHERE {3} = {4}".format(table, column_1, data_1, column_2, data_2)
        self.cursor.execute(query)
        self.conn.commit()

    def delete(self, table, column, data):
        query = "DELETE FROM {0} WHERE {1} = {2}".format(table, column, data)
        self.cursor.execute(query)
        self.conn.commit()

    def query(self, sql):
        self.cursor.execute(sql)
