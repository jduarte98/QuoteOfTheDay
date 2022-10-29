import os
from decouple import config
import mysql.connector

#Database Connection
database = mysql.connector.connect(
  host="localhost",
  user=config('DB_USR'),
  password=config('DB_PW')
)
database_status = 'Could Not Connect'
if database.is_connected():
    database_status = 'Connected'

print("QUOTE OF THE DAY - 2022")
print("Database Status: " + database_status + ';')

# Fetch all the ID's from the quotes table
cursor = database.cursor()
cursor.execute("USE " + config('DB_NM') + ";")
cursor.execute("SELECT id FROM quotes;")
ids = cursor.fetchall()

for x in ids:
    print(x)