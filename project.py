# Evan Taylor - Final Project
# IMDB Rating Checker
import os
from dotenv import load_dotenv

from omdbapi.movie_search import GetMovie


load_dotenv()

apiKey = os.getenv("OMDB_API_KEY")
movie = GetMovie(api_key=apiKey)


# This will prompt the user for a movie, potentially use system args to check mode?
def main():
    mode = input("Please enter what mode you would like to use. [ratings|compare] ")
    if mode == "ratings":
        movieTitle = input(
            "Please enter the title of the movie you would like to check the ratings for: "
        )
        movieRatings = getMovieRatingsData(movieTitle)
        print(movieRatings)
    elif mode == "compare":
        movieTitle1 = input(
            "Please enter the title of the first movie you would like to compare: "
        )
        movieTitle2 = input(
            "Please enter the title of the second movie you would like to compare: "
        )
        compareMovies(movieTitle1, movieTitle2)


def getMovieRatingsData(movieTitle):
    data = movie.get_movie(movieTitle)
    if data == "Movie not found!":
        sys.exit(
            "That movie was not found. Please ensure that you spelled the title correctly."
        )
    ratingsSources = data["ratings"]
    IMDBData = ratingsSources[0]
    RottenTomotoesData = ratingsSources[1]
    RottenTomatoesRating = RottenTomotoesData["Value"]
    IMDBRating = IMDBData["Value"]
    result = f"{movieTitle.title()} has an IMDB rating of {IMDBRating} and a Rotten Tomatoes rating of {RottenTomatoesRating}."
    return result


def compareMovies(movieTitle1, movieTitle2):
    movieRatings1 = getMovieRatingsData(movieTitle1)
    movieRatings2 = getMovieRatingsData(movieTitle2)
    print(movieRatings1)
    print(movieRatings2)
    if movieRatings1 > movieRatings2:
        result = f"{movieTitle1.title()} has a higher rating than {movieTitle2.title()}, with an IMDB rating of {IMDBRating1} and a Rotten Tomatoes rating of {RottenTomatoesRating1}."
    elif movieRatings1 < movieRatings2:
        result = f"{movieTitle2.title()} has a higher rating than {movieTitle1.title()}, with an IMDB rating of {IMDBRating2} and a Rotten Tomatoes rating of {RottenTomatoesRating2}."
        return result


main()

# Funtion to retrieve ratings from the API

# Fucntion to select a movie given two movies based on stats

# Function to
