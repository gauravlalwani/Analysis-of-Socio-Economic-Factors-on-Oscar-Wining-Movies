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

#Open the movies_imdb.csv to read the data
with open('movies_imdb.csv') as csvfile:
    myCSVReader = csv.DictReader(csvfile)

    #SQL query to insert a new movie into our database
    sql = """INSERT INTO movies(name,budget,country)
            VALUE (%(movie_title)s,%(budget)s,%(country)s)
            """
    #SQL query to find the id of the movie that matches the name from the csv
    sql_select_movie =  "SELECT id from movies WHERE name = %(movie_title)s"

    #SQL query to check the name of the movie in the table to avoid duplicates
    sql_select_movie_name = "SELECT name from movies WHERE name = %(movie_title)s"


    #SQL query to insert the data into popularity_ratings table
    sql_insert = """INSERT INTO popularity_ratings(imdb_rating,movie_facebook_likes,director_facebook_likes,actor_facebook_likes,movie_id)
         VALUE (%(imdb_score)s,%(movie_facebook_likes)s,%(director_facebook_likes)s,%(actor_1_facebook_likes)s,%(movie_id)s)
         """
    for row in myCSVReader:

        #Removes extra white spaces from both sides
        row["movie_title"]=row["movie_title"].strip()
        #row["movie_title"]=row["movie_title"][:-2]
        cursor.execute(sql_select_movie, row)
        results = cursor.fetchall()

        #Checking for duplicates
        if (len(results) == 0):
            cursor.execute(sql,row)

        cursor.execute(sql_select_movie, row)
        results = cursor.fetchone()
        movie_id = results['id']

        param_dict = {
                      'movie_id': movie_id,
                      'imdb_score': row['imdb_score'],
                      'movie_facebook_likes' : row['movie_facebook_likes'],
                      'director_facebook_likes' : row['director_facebook_likes'],
                      'actor_1_facebook_likes' : row['actor_1_facebook_likes']
                      }

        cursor.execute(sql_insert, param_dict)
