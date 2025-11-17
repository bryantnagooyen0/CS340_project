# ########################################
# ########## SETUP

from flask import Flask, render_template, request, redirect
import database.db_connector as db

PORT = 64217

app = Flask(__name__)

# ########################################
# ########## ROUTE HANDLERS

# READ ROUTES
@app.route("/", methods=["GET"])
def home():
    try:
        return render_template("home.j2")

    except Exception as e:
        print(f"Error rendering page: {e}")
        return "An error occurred while rendering the page.", 500



    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()


@app.route("/developers", methods=["GET"])
def developers():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        # In query1, we use a JOIN clause to display the names of the homeworlds,
        #       instead of just ID values
        query1 = "SELECT developer_id AS 'Developer ID', \
                developer_name AS 'Developer Name' \
                FROM Developers;"
        
        developers = db.query(dbConnection, query1).fetchall()
        

        # Render the bsg-people.j2 file, and also send the renderer
        # a couple objects that contains bsg_people and bsg_homeworld information
        return render_template(
            "Developers.j2", developers=developers
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()


@app.route("/genres", methods=["GET"])
def genres():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        # In query1, we use a JOIN clause to display the names of the homeworlds,
        #       instead of just ID values
        query1 = "SELECT genre_id AS 'Genre ID', \
                genre_name AS 'Genre Name' \
                FROM Genres;"
        
        genres = db.query(dbConnection, query1).fetchall()
        

        # Render the bsg-people.j2 file, and also send the renderer
        # a couple objects that contains bsg_people and bsg_homeworld information
        return render_template(
            "Genres.j2", genres=genres
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()


@app.route("/games", methods=["GET"])
def games():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        
        query1 = (
            "SELECT g.game_id AS 'Game ID', "
            "g.game_title AS 'Title', "
            "gen.genre_name AS 'Genre', "
            "d.developer_name AS 'Developer', "
            "g.sales_count AS 'Sales', "
            "g.release_date AS 'Release Date' "
            "FROM Games g "
            "LEFT JOIN Genres gen ON g.genre_id = gen.genre_id "
            "LEFT JOIN Developers d ON g.developer_id = d.developer_id;"
        )

        query2 = "SELECT * FROM Developers;"
        query3 = "SELECT * FROM Genres;"

        games = db.query(dbConnection, query1).fetchall()
        genres = db.query(dbConnection, query3).fetchall()
        developers = db.query(dbConnection, query2).fetchall()
        

        # Render the bsg-people.j2 file, and also send the renderer
        # a couple objects that contains bsg_people and bsg_homeworld information
        return render_template(
            "Games.j2", games=games, genres=genres, developers=developers
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()


@app.route("/reviewers", methods=["GET"])
def reviewers():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        # In query1, we use a JOIN clause to display the names of the homeworlds,
        #       instead of just ID values
        query1 = "SELECT reviewer_id AS 'Reviewer ID', reviewer_company AS 'Reviewer Company' FROM Reviewers;"

        reviewers = db.query(dbConnection, query1).fetchall()
        

        # Render the bsg-people.j2 file, and also send the renderer
        # a couple objects that contains bsg_people and bsg_homeworld information
        return render_template(
            "Reviewers.j2", reviewers=reviewers
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/reviews", methods=["GET"])
def reviews():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        # In query1, we use a JOIN clause to display the names of the homeworlds,
        #       instead of just ID values
        query1 = (
            "SELECT r.review_id AS 'Review ID', "
            "g.game_title AS 'Game Title', "
            "rev.reviewer_company AS 'Reviewer Company', "
            "r.rating AS 'Rating', "
            "r.comment AS 'Comment', "
            "r.review_date AS 'Review Date' "
            "FROM Reviews r "
            "LEFT JOIN Reviewers rev ON r.reviewer_id = rev.reviewer_id "
            "LEFT JOIN Games g ON r.game_id = g.game_id;"
        )

        query2 = "SELECT * FROM Reviewers;"
        query3 = "SELECT * FROM Games;"
        
        reviews = db.query(dbConnection, query1).fetchall()
        

        # Render the bsg-people.j2 file, and also send the renderer
        # a couple objects that contains bsg_people and bsg_homeworld information
        return render_template(
            "Reviews.j2", reviews=reviews
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()


# ########################################
# ########## LISTENER

if __name__ == "__main__":
    app.run(
        port=PORT, debug=True
    )  # debug is an optional parameter. Behaves like nodemon in Node.