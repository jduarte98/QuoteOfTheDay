
from dbm.dumb import _Database
from DatabaseConn import DatabaseConn
import random
import numpy


#Database Connection
database = DatabaseConn()

print("QUOTE OF THE DAY - 2022")
database.cursor.execute("SELECT id FROM quotes;")
database.cursor.execute("SELECT author, message FROM quotes WHERE id='" + str(random.randint(1, numpy.asarray(database.cursor.fetchall()).size)) + "';")
retrived_quote = database.cursor.fetchall();

# [('Steve Jobs', '"Your time is limited, so don\'t waste it living someone else\'s life"')]

print(retrived_quote)

