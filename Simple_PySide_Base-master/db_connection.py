import sqlite3

def create_connection(database):
   conn = sqlite3.connect(database)
   cursor = conn.cursor()
   print("Connected to database")
   return conn, cursor

# # Usage example
# database_path = "/path/to/database.db"
# conn, cursor = create_connection(database_path)
