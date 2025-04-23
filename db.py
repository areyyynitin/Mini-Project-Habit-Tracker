import mysql.connector

config = {
    'user': 'root',
    'password': 'your password',
    'host': 'localhost',
    'database': 'habit_tracker'
}

def connect_db():
    return mysql.connector.connect(**config)

# Test the connection
try:
    cnx = connect_db()
    print("Connected to database successfully!")
except mysql.connector.Error as err:
    print("Error connecting to database: {}".format(err))