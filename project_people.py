import pymysql
import csv


# Open the connection to the database
connection = pymysql.connect(host="localhost",
                             user="gaurav_lalwani",
                             passwd="9987090417",
                             db="gaurav_lalwani_oscar_movies",
                             autocommit=True,
                             cursorclass=pymysql.cursors.DictCursor)

# # We get a cursor from the connection to talk to the server
cursor = connection.cursor() # now we can use cursor.execute() to talk to the server

#Open the people.csv to read the data
with open('people.csv') as csvfile:
    myCSVReader = csv.DictReader(csvfile)

    # Placeholders are same as in our csv file
    sql = """INSERT INTO people(name,sexual_orientation,race,religion)
          VALUE (%(person)s,%(sexual_orientation)s,%(race_ethnicity)s,%(religion)s)"""

    for row in myCSVReader:
        cursor.execute(sql,row)
