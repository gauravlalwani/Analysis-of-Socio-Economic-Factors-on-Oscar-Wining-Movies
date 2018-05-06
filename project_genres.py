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
cursor = connection.cursor()

#SQL query to get the id of the movie that matches the movie name from the csv
sql_select_movie =  "SELECT id from movies WHERE name = %(movie_title)s"

#SQL query to get the id of the genre that matches the genre name from the csv
sql_select_genre =  "SELECT id from genres WHERE name = %(genre_name)s"

#SQL query to insert a new movie into the database
sql_insert_new_movie="""INSERT INTO movies(name)
                VALUE (%(movie_names)s)
"""
#SQL query to insert a new genre into the database
sql_insert_new_genre="""INSERT INTO genres(name)
                VALUE (%(genre_name)s)
"""

#SQL query to insert data into the movies_genres table
sql = """INSERT INTO movies_genres(genre_id,movie_id)
     VALUE (%(genre_id)s,%(movie_id)s)
     """
#Open the movies_imdb.csv to read the data
with open('movies_imdb.csv') as csvfile:

    myCSVReader = csv.DictReader(csvfile)

    for row in myCSVReader:
        #Removes extra white spaces from both sides
        row["movie_title"]=row["movie_title"].strip()

        #Algorithm to store the id of the movie if it exists or insert the new movie and get the newly created id
        cursor.execute(sql_select_movie, row)
        results = cursor.fetchall()
        if (len(results) == 0):
            cursor.execute(sql_insert_new_movie,row)
            movie_id = cursor.lastrowid
        else:
            movie_id = results[0]["id"]

        #Genres in the genre column are multiple names separated by | eg:- Comedy|Action|Adventure
        genres = row['genres'].split("|")

        #Once we split the genres we have a list for each movie and we need to traverse through each list
        for genre_str in genres:

            param_dict = { 'genre_name': genre_str}

            #Algorithm to store the id of the genre if it exists or insert the new movie and get the newly created id
            cursor.execute(sql_select_genre, param_dict)
            results = cursor.fetchall()
            if (len(results) == 0):
                cursor.execute(sql_insert_new_genre,param_dict)
                genre_id = cursor.lastrowid
            else:
                genre_id = results[0]["id"]

            param_dict1 = {'genre_id': genre_id,
                             'movie_id': movie_id
                             }

            cursor.execute(sql,param_dict1)
