# pymysql.cursors is the library that will talk to mysql
import pymysql
# csv helps us write out the csv files.
import csv
# convenience methods for debugging
import pprint

# First set up the connection to the server
# Open the connection to the database (must be one you can write to!)
connection = pymysql.connect(host="localhost",            # your host, usually localhost
                             user="gaurav_lalwani",             # your username
                             passwd="9987090417",   # your password
                             db="gaurav_lalwani_oscar_movies", # name of the db
                             autocommit=True,             # removes a step in queries
                             cursorclass=pymysql.cursors.DictCursor)

# as with opening a file we can use with to open the connection
# the cursor is the object through which we talk to the sql server.
with connection.cursor() as cursor:
    sql = """
        SELECT people.name, people.race, people.sexual_orientation, people.religion, popularity_ratings.actor_facebook_likes
        FROM people, movies, awards, popularity_ratings
        WHERE awards.category IN ("Best Actor", "Best Actress")
        AND people.id = awards.person_id
        AND awards.movie_id = movies.id
        AND movies.id = popularity_ratings.movie_id
        """
    sql2 = """
        SELECT people.name, people.race, people.sexual_orientation, people.religion, movies.name, movies.budget, movies.country, popularity_ratings.actor_facebook_likes, popularity_ratings.director_facebook_likes, popularity_ratings.movie_facebook_likes, popularity_ratings.imdb_rating, popularity_ratings.no_of_nominations, popularity_ratings.metacritic_rating, awards.category, awards.year, genres.name
        FROM people, movies, awards, popularity_ratings, genres, movies_genres
        WHERE people.id = awards.person_id
        AND awards.movie_id = movies.id
        AND movies.id = popularity_ratings.movie_id
        AND movies.id = movies_genres.movie_id
        AND genres.id = movies_genres.genre_id

        """
    cursor.execute(sql)
    results = cursor.fetchall()

    csv_column_order = list(results[0].keys())

    with open('table1.csv', 'w', newline='') as csvfile:
    # Note that here we ask for a DictWriter, which works with the Dicts
    # provided by the DictCursor.
        myCsvWriter = csv.DictWriter(csvfile, delimiter=',',
                                              quotechar='"',
                                              fieldnames = csv_column_order)

        # write the header row (it gets those from the fieldnames)
        myCsvWriter.writeheader()

        # and then each of the other results, row by row.
        for row in results:

            myCsvWriter.writerow(row)

    cursor.execute(sql2)
    results = cursor.fetchall()

    csv_column_order = list(results[0].keys())

    with open('table2.csv', 'w', newline='') as csvfile:
    # Note that here we ask for a DictWriter, which works with the Dicts
    # provided by the DictCursor.
        myCsvWriter = csv.DictWriter(csvfile, delimiter=',',
                                              quotechar='"',
                                              fieldnames = csv_column_order)

        # write the header row (it gets those from the fieldnames)
        myCsvWriter.writeheader()
        # and then each of the other results, row by row.
        for row in results:

            myCsvWriter.writerow(row)
