"""

    Content-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `content_model` !!

    You must however change its contents (i.e. add your own content-based
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline content-based
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize

# Importing data
movies = pd.read_csv('resources/data/movies.csv', sep = ',')
ratings = pd.read_csv('resources/data/ratings.csv')
content_data = pd.read_csv('resources/data/content_data_clean.csv')
movies.dropna(inplace=True)

# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  
def content_model(movie_list, top_n=5):
    """Performs Content filtering based upon a list of movies supplied
       by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.
    top_n : type
        Number of top recommendations to return to the user.

    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.

    """
     # Vectorizing the input movies
    tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
    vectors = tfidf.fit_transform(content_data["cleaned_overview"]).toarray()
    vectors = normalize(vectors)

    # Calculating cosine similarity
    similarity = cosine_similarity(vectors)

    # Getting the indices of the input movies
    indices = content_data[content_data['title'].isin(movie_list)].index.tolist()

    # Calculating average similarity for input movies
    avg_similarity = similarity[indices].mean(axis=0)

    # Getting the indices of the top similar movies
    top_indices = avg_similarity.argsort()[-top_n*2:][::-1]

    # Filtering out movies that are the same as the input movies
    top_indices = [idx for idx in top_indices if idx not in indices][:top_n]

    # Getting the titles and genres of the top similar movies
    recommended_movies = content_data.iloc[top_indices][['title', 'genres']]

    # Getting the cosine similarity scores for the recommended movies
    cosine_similarity_scores = avg_similarity[top_indices]

    # Adding the cosine similarity scores to the DataFrame
    recommended_movies['cosine_similarity'] = cosine_similarity_scores

    return recommended_movies['title'].tolist()

