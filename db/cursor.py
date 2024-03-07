from db.connection import Connection

class Cursor():
    def __init__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        self._connection = Connection.get_connection()
        self._cursor = self._connection.cursor()
        return self._cursor
    
    def __exit__(self, exc_type, exc_value, trace):
        if exc_value:
            print(f'Type: {exc_type}, Value: {exc_value}, Details: {trace}')
            self._connection.rollback()
        else:
            self._connection.commit()
        self._cursor.close()
        Connection.free_connection(self._connection)