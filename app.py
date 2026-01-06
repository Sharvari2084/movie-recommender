import pickle
import streamlit as st
import requests
import os
from dotenv import load_dotenv

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pickle.load(open("model/movie_list.pkl", "rb"))

@st.cache_resource
def compute_similarity(movies):
    cv = CountVectorizer(max_features=5000, stop_words="english")
    vectors = cv.fit_transform(movies["tags"]).toarray()
    similarity = cosine_similarity(vectors)
    return similarity






# ---------- Custom UI Styling ----------
st.markdown("""
<style>

/* Main title */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #7B61FF;
    margin-bottom: 10px;
}

/* Subtitle */
.sub-title {
    text-align: center;
    font-size: 18px;
    color: #CFCFFF;
    margin-bottom: 30px;
}

/* Section headers */
.section-title {
    font-size: 20px;
    font-weight: 600;
    color: #AFA8FF;
    margin-bottom: 10px;
}

/* Button styling */
div.stButton > button {
    background: linear-gradient(90deg, #7B61FF, #5F5CFF);
    color: white;
    border-radius: 12px;
    height: 3em;
    font-size: 18px;
    font-weight: 600;
    border: none;
    transition: 0.3s ease;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #5F5CFF, #7B61FF);
    transform: scale(1.03);
}

/* Movie card text */
.movie-title {
    text-align: center;
    font-weight: 600;
    font-size: 16px;
    color: #EDEDED;
    margin-top: 8px;
}

</style>
""", unsafe_allow_html=True)


# Load environment variables
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# ------------------ Fetch Poster ------------------
def fetch_poster(movie_id):
    if TMDB_API_KEY is None:
        return "https://via.placeholder.com/300x450?text=No+API+Key"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get('poster_path'):
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            return "https://via.placeholder.com/300x450?text=No+Poster"

    except requests.exceptions.RequestException:
        return "https://via.placeholder.com/300x450?text=Error"

# ------------------ Recommendation Logic ------------------
def recommend(movie):
    
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters
    

# ------------------ Streamlit UI ------------------
st.markdown(
    "<h1 style='text-align:center; color:#8F7CFF; font-weight:700;'>🎬 Movie Recommender System</h1>",
    unsafe_allow_html=True
)


st.markdown(
    "<p style='text-align: center; font-size:18px;'>Discover movies similar to your favorite ones 🍿</p>",
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)


movies = pickle.load(open("model/movie_list.pkl", "rb"))
similarity = compute_similarity(movies)

movie_list = movies["title"].values
selected_movie = st.selectbox(
    "🎥 Type or select a movie from the dropdown",
    movie_list
)


st.sidebar.markdown("## 🎬 About This App")
st.sidebar.write(
    "Discover movies you’ll love using intelligent similarity analysis that "
"matches films based on story, genre, and key features — not just popularity."

)


if st.button("Show Recommendations"):
    with st.spinner("Finding movies you’ll love... 🎥"):
        names, posters = recommend(selected_movie)


    st.divider()

    cols = st.columns(len(names))
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.image(poster, width=200)
            st.markdown(
                f"<div class='movie-title'>{name}</div>",
                unsafe_allow_html=True
            )
def apply_theme(theme):
    if theme == "dark":
        st.markdown("""
        <style>
        body {
            background-color: #0F0C29;
            color: #EDEDED;
        }
        </style>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <style>
        body {
            background-color: #F5F6FA;
            color: #111;
        }
        </style>
        """, unsafe_allow_html=True)
   
    


