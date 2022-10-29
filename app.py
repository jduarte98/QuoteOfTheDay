# Quote of the Day - 2022 #
# Author: João Duarte

# Imports
from DatabaseConn import DatabaseConn
import random
import numpy


#Ddatbase Definition from the DatabaseConn Class
database = DatabaseConn()

# "Title"
print()
print("QUOTE OF THE DAY - 2022") 
print("by João duarte")
print()

# Data Fetch
# First the program executes a query to fetch all IDs. That way we can get all the IDs to a tuple that latter on we will use
# to know how many quotes there is in the database. After that a query is executed, where we fetch from a quote author and message. 
# This query will return the quote with the ID that is automaticly generated from 1 to the Size of the ID's tuple that we abtoined 
# in the first query. Ultimatelly we fecth the data restrained by the queries described above.
database.cursor.execute("SELECT id FROM quotes;")
database.cursor.execute("SELECT author, message FROM quotes WHERE id='" + str(random.randint(1, numpy.asarray(database.cursor.fetchall()).size)) + "';")
retrived_quote = database.cursor.fetchall();

# Print Retrieved Quote
print("Quote of The Day:")
print(retrived_quote)
print()

# PS: this program doesn't have any Exception Handling or Error Handling Mechanisms by choice (since the purpose of 
# the program was just to return back to Python programming and remember its basic commands). Implementing those
# would be a good next step ;)