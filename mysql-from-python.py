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
      row = ("Bob", 21, "1990-02-06 23:04:56")
      cursor.execute("INSERT INTO Friends VALUES(%s, %s, %s);", row)
      connection.commit()

finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()