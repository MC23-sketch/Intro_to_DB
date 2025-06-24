# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL Server
        conn = mysql.connector.connect(
            host="localhost",
            port=3308,
            user="root",
            password="Emcee24."
        )

        cursor = conn.cursor()

        # Attempt to create the database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed to create database: {err}")

        # Close connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Connection error: {err}")

if __name__ == "__main__":
    create_database()
