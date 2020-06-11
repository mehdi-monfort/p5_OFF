import mysql.connector
from mysql.connector import errorcode
from config import DB_CONFIG
from SQL.table import TABLES

def database():
    """delete database"""
    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor(buffered=True)

    try:
        cursor.execute("DROP DATABASE IF EXISTS {}".format(DB_CONFIG["database"]))
        print("database is deleted")
    except mysql.connector.Error as err:
        print("Failed delete database: {}".format(err))
        exit(1)

    def create_database(cursor):
        """create database"""
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8mb4'".format(
                    DB_CONFIG["database"]
                )
            )
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    try:
        cursor.execute("USE {}".format(DB_CONFIG["database"]))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_CONFIG["database"]))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(DB_CONFIG["database"]))
            cnx.database = DB_CONFIG["database"]
        else:
            print(err)
            exit(1)

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.close()
