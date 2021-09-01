import os
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
      sql = "SELECT * FROM Artist;"
      cursor.execute(sql)
      result = cursor.fetchall()
      print(result)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()