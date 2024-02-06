"""

    Helper functions for data loading and manipulation.

    Author: Explore Data Science Academy.

"""
# Data handling dependencies
import pandas as pd
import numpy as np

def load_movie_titles(path_to_movies):
    """Load movie titles from database records.

    Parameters
    ----------
    path_to_movies : str
        Relative or absolute path to movie database stored
        in .csv format.

    Returns
    -------
    list[str]
        Movie titles.

    """
    df = pd.read_csv(path_to_movies)
    df = df.dropna()
    unique_movies = df[['movieId', 'title']].drop_duplicates()
    movie_list = unique_movies['title'].tolist()
    return movie_list
