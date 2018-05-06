import pymysql
import csv

# Open the connection to the database (must be one you can write to!)
connection = pymysql.connect(host="localhost",
                             user="gaurav_lalwani",
                             passwd="9987090417",
                             db="gaurav_lalwani_oscar_movies",
                             autocommit=True,
                             cursorclass=pymysql.cursors.DictCursor)

# # We get a cursor from the connection to talk to the server
cursor = connection.cursor() # now we can use cursor.execute() to talk to the server

#SQL query to get the id of the person that matches the person name from the csv
sql_select_person = "SELECT id from people WHERE name = %(person)s"

#SQL query to find the id of the movie that matches the name from the csv
sql_select_movie =  "SELECT id from movies WHERE name = %(name)s"

#SQL query to insert a new movie into our database
sql_insert_new_movie="""INSERT INTO movies(name)
                VALUE (%(name)s)
"""

#SQL query to update the data in the popularity ratings table
sql_update = """UPDATE popularity_ratings SET metacritic_rating = %(metacritic)s,
no_of_nominations= %(nominations)s,
movie_id = %(movie_id)s
WHERE movie_id = %(movie_id)s
"""

#Open the actor_waterloo.csv to read the data
with open('actor_waterloo.csv') as csvfile:

    myCSVReader = csv.DictReader(csvfile)

    for row in myCSVReader:
        #Removes extra white spaces from both sides
        row["name"]=row["name"].strip()

        #Algorithm to store the id of the movie if it exists or insert the new movie and get the newly created id
        cursor.execute(sql_select_movie, row)
        results = cursor.fetchall()
        if (len(results) == 0):
            cursor.execute(sql_insert_new_movie,row)
            movie_id = cursor.lastrowid
        else:
            movie_id = results[0]["id"]

        param_dict = {
                      'movie_id': movie_id,
                      'nominations': row['nominations'],
                      'metacritic' : row['metacritic']}

        cursor.execute(sql_update, param_dict)

#Open the actress_waterloo.csv to read the data
with open('actress_waterloo.csv') as csvfile:

    myCSVReader = csv.DictReader(csvfile)

    for row in myCSVReader:
        #Removes extra white spaces from both sides
        row["name"]=row["name"].strip()
        #Algorithm to store the id of the movie if it exists or insert the new movie and get the newly created id
        cursor.execute(sql_select_movie, row)
        results = cursor.fetchall()
        if (len(results) == 0):
            cursor.execute(sql_insert_new_movie,row)
            movie_id = cursor.lastrowid
        else:
            movie_id = results[0]["id"]

        param_dict = {
                      'movie_id': movie_id,
                      'nominations': row['nominations'],
                      'metacritic' : row['metacritic']}

        cursor.execute(sql_update, param_dict)

#Open the director_waterloo.csv to read the data
with open('director_waterloo.csv') as csvfile:

    myCSVReader = csv.DictReader(csvfile)

    for row in myCSVReader:
        #Removes extra white spaces from both sides
        row["name"]=row["name"].strip()
        #Algorithm to store the id of the movie if it exists or insert the new movie and get the newly created id
        cursor.execute(sql_select_movie, row)
        results = cursor.fetchall()
        if (len(results) == 0):
            cursor.execute(sql_insert_new_movie,row)
            movie_id = cursor.lastrowid
        else:
            movie_id = results[0]["id"]

        param_dict = {
                      'movie_id': movie_id,
                      'nominations': row['nominations'],
                      'metacritic' : row['metacritic']}

        cursor.execute(sql_update, param_dict)
