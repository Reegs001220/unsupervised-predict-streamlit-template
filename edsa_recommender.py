"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
# title_list = load_movie_titles('resources/data/movies.csv')
content_data = load_movie_titles('resources/data/content_data_clean.csv')
collab_data = load_movie_titles('resources/data/filtered_ratings_data.csv')
content_separated = pd.read_csv('resources/data/content_separated.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["About", "Movie Filter", "Current Trends", "Recommender System", "Algorithmic Analysis"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)

    if page_selection == "About":
        st.image('resources/imgs/CineMatch (1).png',use_column_width=True)
        st.write("# CineMatch: Connecting You to Your Next Favorite Movie 🎬")

        

            # Introduction
        st.write("#### Welcome to CineMatch, your personalized movie recommendation experience! Our mission is to help you discover"
                " the perfect movies tailored to your unique tastes. Powered by advanced algorithms, we strive to deliver"
                " accurate and enjoyable movie suggestions that match your preferences.")

        # Meet Our Team
        st.write("## Meet the Team")
        st.write("We're a passionate team of data scientists and movie enthusiasts committed to making your cinematic journey unforgettable."
                " Get to know the minds behind CineMatch:")
        st.write("- Reegan Rooke")
        st.write("- Precious Ratlhagane ")
        st.write("- Mudalo Ramadi ")
        st.write("- Mohau Khanye")
        st.write("- Harvey Ntelele")
        st.write("- Lucky Thamaga ")
        # Add more team members as needed

        # Navigation Guide
        st.write("## Navigation Guide")
        st.write("Explore the various features of CineMatch using the scroll down bar on the left to make the most out of your movie discovery:")
        st.write("- **Movie Filter:** Just want to explore the movies in our database? Customize your movie search by director, cast, year, genre, or title to receive any matching movies we have.")
        st.write("- **Current Trends:** Stay updated on popular movies, highest-rated films, and genre diversity by looking at our provided graphs.")
        st.write("- **Recommender System:** Receive personalized movie recommendations based on your 3 favorites found in the database.")
        st.write("- **Algorithmic Analysis:** Learn about the algorithms powering our recommendation system.")

        # Contact Us
        st.write("## Contact Us")
        st.write("Have questions or suggestions? Feel free to reach out to us at [cinematch@gmail.com]. We value your feedback"
                " and are here to enhance your CineMatch experience.")

        # Closing Statement
        st.write("Thank you for choosing CineMatch. Let the cinematic adventure begin!")

    if page_selection == "Recommender System":

        st.image('resources/imgs/CineMatch (1).png',use_column_width=True)
        # Header contents
        st.title('CineMatch: Movie Recommender Engine')
        st.write("**Ready to explore a curated list of movies recommended just for you? Choose your favorites, and let CineMatch do the rest! 🍿🎬**")
        
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        st.write('**Step 1:** Select the algorithm you want to use for your movie recommendations.')
        st.write('**Step 2:** Choose your three favorite movies via a type search or by selecting from the dropdowns.')
        st.write('**Step 3:** Click the **Recommend** button to generate your personalized movie list!')
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))
        

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            # User-based preferences
            st.write('### Enter Your Three Favorite Movies')
            movie_1 = st.selectbox('Fisrt Option',content_data)
            movie_2 = st.selectbox('Second Option',content_data)
            movie_3 = st.selectbox('Third Option',content_data)
            fav_movies = [movie_1,movie_2,movie_3]
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=5)
                    print(top_recommendations)
                    if top_recommendations:
                        st.title("We think you'll like:")
                    else:
                        st.title("Unfortunately there is not enough data on the selected movies to return recommendations")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except Exception as e:
                    print ("error:", e)
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            # User-based preferences
            st.write('### Enter Your Three Favorite Movies')
            movie_1 = st.selectbox('Fisrt Option',collab_data)
            movie_2 = st.selectbox('Second Option',collab_data)
            movie_3 = st.selectbox('Third Option',collab_data)
            fav_movies = [movie_1,movie_2,movie_3]
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(chosen_movies=fav_movies,
                                                           top_n=5)
                    if top_recommendations:
                        st.title("We think you'll like:")
                    else:
                        st.title("Unfortunately there is not enough data on the selected movies to return recommendations")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except Exception as e:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")
                    print(e)


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Algorithmic Analysis":

        st.image('resources/imgs/CineMatch (1).png',use_column_width=True)
        st.title("Algorithmic Analysis")
        st.write("## CineMatch Content-Based Filtering")
        st.image('resources/imgs/cont.png',use_column_width=True)
        st.write(" ##### **Our content-based filtering algorithm helps you discover movies based on the specific characteristics of films you already love. Here's a step-by-step breakdown of how it works:**")
        st.write(" #### **Step 1**: Selecting the Most Important Features")
        st.write("For our algorithm, each movie in the database has an Overview. This overview was developed by our data scientist and it contains key information about the movie including the Genres, Cast, Directors, and Keywords that briefly describes the plot of each movie. This is the info that the algorithm uses to determine which movies are best suited to your top 3 choices.")
        st.write(" #### **Step 2**: Vectorizing Movie Overviews")
        st.write("We use a technique called TF-IDF (Term Frequency-Inverse Document Frequency) to convert the movie overviews into numerical vectors. This helps us represent the content of each movie in a way that our algorithm can understand.")
        st.write(" #### **Step 3**: Calculating Similarity")
        st.write("Our algorithm uses cosine similarity to determine which movies are most similar to each other, based on the Overview feature. This helps us rank movies in order of how similar they are to your top 3 choices.")
        st.write(" #### **Step 4**: User Input and Recommendations")
        st.write("You tell us your three favorite movies, and we use them to find movies with similar content. The top five recommendations produced are the movies that had the highest similarity score to your top 3 choices.")
        st.write(" #### **Step 5**: Presenting Recommendations")
        st.write("We crunch the numbers and present you with a list of top 5 recommendations based on the content similarities.")
        st.write(" #### **Note**: ")
        st.write("- The algorithm analyzes the content of movies, such as titles, directors, genres, and plot keywords, to understand your preferences.")
        st.write("- If there's not enough data on your selected movies, we'll let you know.")

        st.write("## CineMatch CineMatch Collaborative-Based Filtering")
        st.image('resources/imgs/colab.png',use_column_width=True)
        st.write("##### **Our collaborative-based filtering algorithm leverages the preferences of users with similar tastes to offer personalized movie recommendations. Rather than looking at movie specific characteristics, this model recommends the top rated movies of other users that also enjoyed your movie selection. Here's a detailed look at how it works:**")
        st.write(" #### **Step 1**: User Ratings")
        st.write("Our algorithm uses the historical ratings data of our Top 100 users who have provided ratings for the most movies. This allows for an efficient yet informative recommendation system.")
        st.write(" #### **Step 2**: Identifying Similar Users")
        st.write("For the movies you've chosen as favorites, we identify users who have rated them highly (with a score of 4 or above). These users form a set of individuals with similar tastes.")
        st.write(" #### **Step 3**: Recommending Movies")
        st.write("Based on your preferences, we recommend movies based on the preferences of users similar to you. The collaborative model we use is based on Singular Value Decomposition (SVD). SVD is a powerful technique for matrix factorization, allowing us to uncover hidden patterns in user preferences. Our model has been trained on a dataset comprising the most active users, providing accurate predictions for personalized movie recommendations.The algorithm predicts ratings for the movies these users enjoyed, and then recommends the top five movies with the highest predicted ratings.")
        st.write(" #### **Step 4**: Presenting Recommendations")
        st.write("We crunch the numbers and present you with a list of top 5 recommendations based on the content similarities.")
        st.write(" #### **Note**: ")
        st.write("- The collaborative model is trained using the Singular Value Decomposition (SVD) technique.")
        st.write("- Recommendations are based on the ratings of users with similar tastes, providing movie suggestions that were highly rated by the users that also enjoyed your top three picks.")
        st.write("- This algorithm differs from the content-based filtering algorithm in that it is based on user preferences rather than movie characteristics.")
        st.write("- If there's not enough data on your selected movies, we'll let you know.")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
        
    if page_selection == "Movie Filter":

        st.image('resources/imgs/CineMatch (1).png',use_column_width=True)
        st.title("Looking for Something Specific?")
        st.image('resources/imgs/ideas.png',width=200)

        st.write("**Use our Movie Filter to find what you're looking for.**")
        st.write("Looking for a Comedy with Tom Hanks? We have you covered.") 
        st.write("This interactive filtering system will display all the movies in our database that match your specific search criteria.")

        columns = {'title': 'Title','genres': 'Genres','release_year' : 'Release Year','title_cast' : 'Cast', 'director': 'Director'}
        display_content_data = content_separated.drop('overview', axis=1).drop('movieId', axis=1).drop('plot_keywords', axis=1)
        display_content_data['release_year'] = display_content_data['release_year'].astype(str)
        display_content_data.rename(columns=columns, inplace=True)
        display_content_data.dropna()

        cols = st.columns(5)

        with cols[0]:
            title = st.text_input("Enter a title", "")
        with cols[1]:
            genre = st.text_input("Enter a genre", "")
        with cols[2]:
            release_year = st.text_input("Enter a release year", "")
        with cols[3]:
            cast = st.text_input("Enter a cast member", "")
        with cols[4]:
            director = st.text_input("Enter a director", "")

        title = title.split(" ") if title != '' else []
        title = [word.lower() for word in title]
        genre = genre.split(" ") if genre != '' else []
        genre = [word.lower() for word in genre]
        release_year = release_year.split(" ") if release_year != '' else []
        release_year = [word.lower() for word in release_year]
        cast = cast.split(" ") if cast != '' else []
        cast = [word.lower() for word in cast]
        director = director.split(" ") if director != '' else []
        director = [word.lower() for word in director]

        filtered_df = display_content_data[
            (display_content_data['Title'].apply(lambda x: isinstance(x, str) and all(string in x.lower() for string in title))) &
            (display_content_data['Genres'].apply(lambda x: isinstance(x, str) and all(string in x.lower() for string in genre))) &
            ((len(release_year) == 0) | (display_content_data['Release Year'].apply(lambda x: isinstance(x, str) and any(string in x.lower() for string in release_year)))) &
            (display_content_data['Cast'].apply(lambda x: isinstance(x, str) and all(string in x.lower() for string in cast))) &
            (display_content_data['Director'].apply(lambda x: isinstance(x, str) and all(string in x.lower() for string in director)))
        ]

        
        st.dataframe(filtered_df)

        st.image('resources/imgs/genres.png', width=1000)
    
    if page_selection == "Current Trends":

        st.image('resources/imgs/CineMatch (1).png',use_column_width=True)
        st.title("What's Trending?")
        st.write("Discover the most watched and rated movies in our database.")
        st.image('resources/imgs/popular.png',width = 1000)
        st.write("Explore the overall highest rated movies in our database.")
        st.image('resources/imgs/top_movies.png',width = 1000)
    # ----------------------------------------------------------------


if __name__ == '__main__':
    main()
