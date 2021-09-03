import os
import datetime
import pymysql

#Get username
username = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")

#Connect to the database

connection = pymysql.connect(host='localhost',
                            user=username,
                            password=password,
                            db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
      sql = "SELECT * FROM Genre;"
      cursor.execute("""CREATE TABLE IF NOT EXISTS
                    Friends(name char(20), age int, DOB datetime);""")

finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()