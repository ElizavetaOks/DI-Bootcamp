# Exercise 1 : Restaurant Menu Manager
# Description: Create a restaurant menu management system for a manager. The program should allow the manager to view the menu, add an item and delete an item.

# PART 1

import psycopg2
from psycopg2 import sql

import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    dbname = os.getenv('db_name'),
    user = os.getenv('db_user'),
    password = os.getenv('db_pass'),
    host = os.getenv('db_host'),
    port = os.getenv('liz_port')
)

cursor = conn.cursor()

# create_table = sql.SQL("""
#     CREATE TABLE Menu_Items (
#         item_id SERIAL PRIMARY KEY,
#         item_name VARCHAR(30) NOT NULL,
#         item_price SMALLINT DEFAULT 0
#     )
# """)

# cursor.execute(create_table)

import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql

class MenuItem:
    def __init__ (self, item_name, item_price):
        self.item_name = item_name,
        self.item_price = item_price

    def save(self):
    # Create save method
        load_dotenv()

        conn = psycopg2.connect(
            dbname = os.getenv('db_name'),
            user = os.getenv('db_user'),
            password = os.getenv('db_pass'),
            host = os.getenv('db_host'),
            port = os.getenv('liz_port')
        )

        cursor = conn.cursor()

        insert_query = sql.SQL("""
            INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)
        """)

        cursor.execute(insert_query, (self.item_name, self.item_price))
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        # Create delete method
        load_dotenv()

        conn = psycopg2.connect(
            dbname = os.getenv('db_name'),
            user = os.getenv('db_user'),
            password = os.getenv('db_pass'),
            host = os.getenv('db_host'),
            port = os.getenv('liz_port')
        )

        cursor = conn.cursor()

        delete_query = sql.SQL("""
            DELETE FROM Menu_Items WHERE item_name = %s
        """)

        cursor.execute(delete_query, (self.item_name,))
        conn.commit()
        cursor.close()
        conn.close()

    def update(self, new_name, new_price):
        # Create update method
        load_dotenv()

        conn = psycopg2.connect(
            dbname = os.getenv('db_name'),
            user = os.getenv('db_user'),
            password = os.getenv('db_pass'),
            host = os.getenv('db_host'),
            port = os.getenv('liz_port')
        )

        cursor = conn.cursor()

        update_query = sql.SQL("""
            UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s
        """)

        cursor.execute(update_query, (new_name, new_price, self.item_name))
        conn.commit()
        cursor.close()
        conn.close()


from menu_manager import MenuManager
    
item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuManager.get_by_name('Beef Stew')
items = MenuManager.all()

conn.commit()

cursor.close()
conn.close()

