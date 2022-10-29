# Quote of The Day - 2022 #
# Author: João Duarte

# Imports
import mysql.connector
from decouple import config

# Class Definition
class DatabaseConn:
    # Establish the Database Connection
    database = mysql.connector.connect(
        host = config('DB_PTH'),
        user = config('DB_USR'),
        password = config('DB_PW')
    )   

    cursor = database.cursor() # Define a Cursor to execute on the database
    cursor.execute("USE " + config('DB_NM') + ";") # Define what database to use    