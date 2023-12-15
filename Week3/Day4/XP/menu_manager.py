import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql

class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        load_dotenv()

        conn = psycopg2.connect(
            dbname = os.getenv('db_name'),
            user = os.getenv('db_user'),
            password = os.getenv('db_pass'),
            host = os.getenv('db_host'),
            port = os.getenv('liz_port')
        )

        cursor = conn.cursor()

        select_query = sql.SQL("""
            SELECT * FROM Menu_Items WHERE item_name = %s
        """)

        cursor.execute(select_query, (item_name,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        # Check if an item was found and return the result
        if result:
            return {"item_id": result[0], "item_name": result[1], "item_price": result[2]}
        else:
            return None
        

    @classmethod
    def all(cls):
        load_dotenv()

        conn = psycopg2.connect(
            dbname = os.getenv('db_name'),
            user = os.getenv('db_user'),
            password = os.getenv('db_pass'),
            host = os.getenv('db_host'),
            port = os.getenv('liz_port')
        )

        cursor = conn.cursor()

        select_all_query = sql.SQL("""
            SELECT * FROM Menu_Items
        """)

        cursor.execute(select_all_query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        items_list = [
            {"item_id": result[0], "item_name": result[1], "item_price": result[2]}
            for result in results
        ]
        return items_list

