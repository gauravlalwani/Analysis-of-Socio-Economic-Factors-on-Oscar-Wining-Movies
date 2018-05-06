import pymysql
import csv
import pprint

# Open the connection to the database
connection = pymysql.connect(host="localhost",
                             user="gaurav_lalwani",
                             passwd="9987090417",
                             db="gaurav_lalwani_oscar_movies",
                             autocommit=True,
                             cursorclass=pymysql.cursors.DictCursor)

# # We get a cursor from the connection to talk to the server
cursor = connection.cursor() # now we can use cursor.execute() to talk to the server

#SQL query to get the id of the person that matches the name from the csv
sql_select_person = "SELECT id from people WHERE name = %(person)s"

#SQL query to get the id of the movie that matches the movie name from the csv
sql_select_movie =  "SELECT id from movies WHERE name = %(movie)s"

#SQL query to insert a new movie into the database
sql_insert_new_movie="""INSERT INTO movies(name)
                VALUE (%(movie)s)
"""

#SQL query to insert data in the awards table
sql = """INSERT INTO awards(year,category,person_id,movie_id)
     VALUE (%(year_of_award)s,%(award)s,%(person_id)s,%(movie_id)s)
     """

#Open the people.csv to read the data
with open('people.csv') as csvfile:

    myCSVReader = csv.DictReader(csvfile)

    for row in myCSVReader:
        cursor.execute(sql_select_person, row)
        results = cursor.fetchone()
        person_id = results['id']

        #Algorithm to store the id of the movie if it exists or insert the new movie and get the newly created id
        cursor.execute(sql_select_movie, row)
        results = cursor.fetchall()
        if (len(results) == 0):
            cursor.execute(sql_insert_new_movie,row)
            movie_id = cursor.lastrowid
        else:
            movie_id = results[0]["id"]

        param_dict = {'person_id': person_id,
                      'movie_id': movie_id,
                      'year_of_award': row['year_of_award'],
                      'award' : row['award'],
                      }

        cursor.execute(sql, param_dict)
