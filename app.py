
from dbm.dumb import _Database
from DatabaseConn import DatabaseConn

#Database Connection
database = DatabaseConn()

print("QUOTE OF THE DAY - 2022")
# Fetch all the ID's from the quotes table
database.cursor.execute("SELECT id FROM quotes;")
ids = database.cursor.fetchall()

for x in ids:
    print(x)