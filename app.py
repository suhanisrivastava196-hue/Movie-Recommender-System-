import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv

st.set_page_config(
    page_title="Movie Recommender System",
    layout="wide",
    initial_sidebar_state="collapsed"
)

movies_list = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

load_dotenv()
TMDB_TOKEN = os.getenv("TMDB_TOKEN")
headers = { 
    "accept": "application/json", 
    "Authorization": f"Bearer {TMDB_TOKEN}" 
}

SVG_PLACEHOLDER = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='500' height='750' viewBox='0 0 500 750'><rect width='500' height='750' fill='%231e293b'/><text x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-family='sans-serif' font-size='24' fill='%2364748b' font-weight='600'>No Poster</text></svg>"

def fetch_poster(movie_id):

    url = f"http://api.themoviedb.org/3/movie/{movie_id}"
    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            poster_path = data.get("poster_path")
            if poster_path:
                return "https://image.tmdb.org/t/p/w500" + poster_path
        return None
    except requests.exceptions.RequestException as e:
        print(f"TMDB API error for movie_id {movie_id}: {e}")
        return None

def recommend(movie):
    
    movie_index = movies_list[movies_list["title"] == movie].index[0]
    distances = similarity[movie_index]

    movie_indices = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    for i in movie_indices:
        idx = i[0]
        recommended_movies.append({
            "title": movies_list.iloc[idx].title,
            "movie_id": movies_list.iloc[idx].movie_id
        })

    return recommended_movies

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;800&display=swap');

.stApp {
    background: linear-gradient(135deg, #090d16 0%, #151030 100%) !important;
    font-family: 'Inter', sans-serif !important;
    color: #f1f5f9 !important;
}

.main-title {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    text-align: center !important;
    margin-bottom: 0.5rem !important;
    font-size: 3.5rem !important;
    letter-spacing: -0.03em !important;
    text-shadow: 0 4px 20px rgba(99, 102, 241, 0.15);
}

.sub-title {
    font-family: 'Inter', sans-serif !important;
    color: #94a3b8 !important;
    text-align: center !important;
    font-size: 1.1rem !important;
    margin-bottom: 3rem !important;
    font-weight: 400;
}

div[data-baseweb="select"] {
    background-color: #1e1b4b !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    transition: border-color 0.3s ease;
}

div[data-baseweb="select"]:hover {
    border-color: #a855f7 !important;
}

label[data-testid="stWidgetLabel"] {
    font-size: 1.05rem !important;
    font-weight: 600 !important;
    color: #e2e8f0 !important;
    font-family: 'Outfit', sans-serif !important;
    margin-bottom: 8px !important;
}

div.stButton > button {
    background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 32px !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    font-family: 'Outfit', sans-serif !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 20px rgba(99, 102, 241, 0.3) !important;
    width: 100% !important;
    margin-top: 15px !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #4f46e5 0%, #9333ea 100%) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(168, 85, 247, 0.5) !important;
}

div.stButton > button:active {
    transform: translateY(0px) !important;
}

.movie-card {
    background: rgba(255, 255, 255, 0.02);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 18px;
    padding: 12px;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex;
    flex-direction: column;
    align-items: center;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    margin-bottom: 2rem;
}

.movie-card:hover {
    transform: translateY(-8px) scale(1.03);
    border-color: rgba(168, 85, 247, 0.5);
    box-shadow: 0 16px 36px rgba(168, 85, 247, 0.3);
    background: rgba(255, 255, 255, 0.05);
}

.movie-poster {
    width: 100%;
    aspect-ratio: 2/3;
    border-radius: 14px;
    object-fit: cover;
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.4);
    transition: transform 0.4s ease;
}

.movie-card:hover .movie-poster {
    transform: scale(1.01);
}

.movie-title {
    margin-top: 14px;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 600;
    font-size: 1rem;
    color: #f8fafc;
    text-align: center;
    line-height: 1.4;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    height: 2.8rem;
    text-overflow: ellipsis;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Discover your next favorite movie based on TMDB 5000 dataset similarity</div>", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies_list["title"].values
)

if st.button("Get Recommendations"):
    recommendations = recommend(selected_movie_name)
    
    st.write(" ")  # Spacer
    
    cols = st.columns(5)
    
    for i, movie_data in enumerate(recommendations): 
        with cols[i]:
            title = movie_data["title"]
            poster_url = fetch_poster(movie_data["movie_id"])
            
            if not poster_url:
                poster_url = SVG_PLACEHOLDER
                
            st.markdown(f"""
            <div class="movie-card">
                <img src="{poster_url}" class="movie-poster" />
                <div class="movie-title" title="{title}">{title}</div>
            </div>
            """, unsafe_allow_html=True)