import pickle
import streamlit as st
import pandas as pd
import requests
import time
import gdown 

def download_pickle(file_id, output_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output_path, quiet=False)

# --- Download and load .pkl files ---
@st.cache_data
def load_data():
    # Replace with your actual Google Drive file IDs
    movies_file_id = "1pFoB4MTtUVNwjHmn0-sPc5kIdAb6ixDM"
    similarity_file_id = "1FMCAfDq2tsZjOokkBN4y_K2Wy6oIiLRG"

    download_pickle(movies_file_id, "movies.pkl")
    download_pickle(similarity_file_id, "similarity.pkl")

    with open("movies.pkl", "rb") as f:
        movies = pickle.load(f)

    with open("similarity.pkl", "rb") as f:
        similarity = pickle.load(f)

    return movies, similarity

# --- Fetch poster with error handling ---
def fetch_poster(movie_id, retries=3):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
            else:
                return "https://via.placeholder.com/300x450.png?text=No+Image"
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                time.sleep(1)
            else:
                print(f"[ERROR] Failed to fetch poster for movie_id {movie_id} - {e}")
                return "https://via.placeholder.com/300x450.png?text=Error"

# --- Recommend movies based on similarity ---
def recommend(movie):
    if movie not in movies['title'].values:
        st.error("Movie not found in dataset.")
        return [], []

    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:  # Top 5
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters

# --- Load data from Drive ---
movies, similarity = load_data()

# --- Page config and styling ---
st.set_page_config(page_title="Movie Recommender", layout="wide", initial_sidebar_state="collapsed")

# --- Custom CSS ---
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .stApp {
            background-color: #121212;
        }
        h1 {
            color: #00ffc3;
            text-align: center;
        }
        .css-1kyxreq, .css-1v0mbdj {
            background-color: #121212 !important;
        }
        .stSelectbox > div {
            background-color: #262730;
            color: white;
        }
        .stButton>button {
            background-color: #00ffc3;
            color: black;
            font-weight: bold;
            border-radius: 10px;
            height: 3em;
            width: 100%;
        }
        .stTextInput>div>div>input {
            background-color: #1e1e1e;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# --- UI Layout ---
st.markdown("## 🎬 Movie Recommender System")
st.markdown("##### Select a movie below and get top 5 similar recommendations")

with st.expander("🔍 Movie Selector", expanded=True):
    selected_movie = st.selectbox("Choose a movie you like", movies['title'].values)

st.markdown("---")

# --- Recommendation section ---
if st.button('🎯 Show Recommendation'):
    with st.spinner("Fetching recommendations..."):
        names, posters = recommend(selected_movie)
        st.markdown("### 🎥 Top 5 Recommended Movies")
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.image(posters[idx], use_container_width=True, caption=names[idx])
