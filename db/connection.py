from dotenv import load_dotenv
from psycopg2 import pool
import os

load_dotenv()

class Connection:
    _DATABASE = os.getenv('name_db')
    _USER = os.getenv('user_db')
    _PASSWORD = os.getenv('password_db')
    _PORT = os.getenv('port_db')
    _HOST = os.getenv('host_db')
    _MIN_CON = os.getenv('min_con')
    _MAX_CON = os.getenv('max_con')
    _pool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None or cls._pool.closed:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      database = cls._DATABASE,
                                                      user = cls._USER,
                                                      password = cls._PASSWORD,
                                                      port = cls._PORT,
                                                      host = cls._HOST)
                return cls._pool
            except Exception as e:
                return None
        else:
            return cls._pool
    
    @classmethod
    def get_connection(cls):
        return cls.get_pool().getconn()
    
    @classmethod
    def free_connection(cls, connection):
        cls.get_pool().putconn(connection)

    @classmethod
    def close_connections(cls):
        cls.get_pool().closeall()