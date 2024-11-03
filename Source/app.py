import pickle
import streamlit as st
import requests
from constant import API

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API}language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        return full_path
    return None

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:  # Get 5 recommendations
        movie_id = movies.iloc[i[0]].id
        poster = fetch_poster(movie_id)
        if poster:
            recommended_movie_posters.append(poster)
            recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Load data
st.header('Movie Recommender System')
movies = pickle.load(open('G:/Movie_Recommendation_System/Source/Preprocess/movie_list.pkl', 'rb'))
similarity = pickle.load(open('G:/Movie_Recommendation_System/Source/Preprocess/similarity.pkl', 'rb'))

# Movie selection for recommendations
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Button to show recommendations
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    st.subheader('Recommended Movies')
    cols = st.columns(3)  # Create 3 columns for recommendations
    
    for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
        with col:
            st.text(name)
            st.image(poster)

# Load popular movies
popular_movies = pickle.load(open('G:/Movie_Recommendation_System/Source/Preprocess/popularity.pkl', 'rb'))

# Display top 10 popular movies
st.subheader('Top 10 Popular Movies')
top_popular_movies = popular_movies.sort_values(by='popularity', ascending=False).head(10)

# Create 3 columns for popular movies
cols = st.columns(3)  # Create 3 columns for popular movies
for index, row in top_popular_movies.iterrows():
    poster = fetch_poster(row['id'])
    if poster:
        with cols[index % 3]:  # Use modulo to distribute movies into columns
            st.text(row['title'])
            st.image(poster)

