# Streamlit is an open-source Python framework that lets you build interactive web applications for data science, machine learning, and data visualization using only Python code—without needing HTML, CSS, or JavaScript.

import streamlit as st
import pickle
import pandas as pd
import requests
import urllib3

# Disable warning logs for insecure requests (verify=False)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()
#footer


# No horizontal header navigation needed


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@300;400;500;700;800&display=swap');

/* Top Horizontal Header Layout */
.logo-text {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 34px !important;
    letter-spacing: 2px;
    background: linear-gradient(45deg, #ff4b4b, #ff8a8a);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 !important;
    padding: 0 !important;
    font-weight: 400;
}

/* Sidebar Styling Override (Hide Sidebar Panel) */
[data-testid="stSidebar"] {
    display: none !important;
}

/* Remove unwanted default Streamlit header spacing */
[data-testid="block-container"] {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
}

div[class*="stAppHeader"] {
    display: none !important;
}

/* Radio group navigation styles removed */

/* Glass card container styling */
.glass-card {
    background: rgba(255, 255, 255, 0.03) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 20px !important;
    box-shadow: 0 10px 35px 0 rgba(0, 0, 0, 0.4) !important;
    color: white !important;
}

/* Custom form inputs styling */
div[data-testid="stForm"] {
    background: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 20px !important;
    padding: 30px !important;
    box-shadow: 0 10px 35px 0 rgba(0, 0, 0, 0.4) !important;
}

div[data-testid="stForm"] input, div[data-testid="stForm"] textarea {
    background-color: rgba(255, 255, 255, 0.04) !important;
    color: white !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 8px !important;
    font-family: 'Outfit', sans-serif !important;
    padding: 12px !important;
    transition: all 0.3s ease !important;
}

div[data-testid="stForm"] input:focus, div[data-testid="stForm"] textarea:focus {
    border-color: #ff4b4b !important;
    box-shadow: 0 0 10px rgba(255, 75, 75, 0.4) !important;
    background-color: rgba(255, 255, 255, 0.07) !important;
}

div[data-testid="stForm"] button {
    background: linear-gradient(135deg, #ff4b4b 0%, #d62f2f 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    height: 48px !important;
    width: 100% !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    font-family: 'Outfit', sans-serif !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    box-shadow: 0 4px 15px rgba(255, 75, 75, 0.25) !important;
    cursor: pointer !important;
    margin-top: 10px;
}

div[data-testid="stForm"] button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(255, 75, 75, 0.45) !important;
    background: linear-gradient(135deg, #ff6b6b 0%, #ff4b4b 100%) !important;
}

/* Button & UI elements styling */
.stButton>button {
    background: linear-gradient(135deg, #ff4b4b 0%, #d62f2f 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    height: 50px !important;
    width: 180px !important;
    font-size: 18px !important;
    font-weight: 600 !important;
    font-family: 'Outfit', sans-serif !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3) !important;
}

.stButton>button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(255, 75, 75, 0.5) !important;
    background: linear-gradient(135deg, #ff6b6b 0%, #ff4b4b 100%) !important;
}

.stButton>button:active {
    transform: translateY(1px) !important;
}

.stSelectbox {
    font-family: 'Outfit', sans-serif;
}

/* Movie Poster Hover Effects */
[data-testid="stImage"] img {
    border-radius: 14px !important;
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease, filter 0.4s ease !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5) !important;
}

[data-testid="stImage"] img:hover {
    transform: scale(1.07) !important;
    box-shadow: 0 15px 30px rgba(255, 75, 75, 0.5) !important;
    filter: brightness(1.08) !important;
}
</style>
""", unsafe_allow_html=True)

#background
st.markdown("""
<style>
.stApp{
background-image:url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba");
background-size:cover;
}
</style>
""", unsafe_allow_html=True)


#def fetch_poster(movie_id):
#    response = requests.get('https://api.tmdb.org/3/movie/{}?api_key=b6481393eb186a1e7c69e1af4562ad7b'.format(movie_id))
#    data = response.json()
#    #print(data)
#    return "https://image.tmdb.org/t/p/w500/" +  data["poster_path"]

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    url = f"https://api.tmdb.org/3/movie/{int(movie_id)}?api_key=b6481393eb186a1e7c69e1af4562ad7b&language=en-US"

    for attempt in range(3):
        try:
            response = requests.get(url, verify=False, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data.get("poster_path"):
                return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
            else:
                # If TMDB itself doesn't have a poster, we return the placeholder and cache it (since it's a permanent state on TMDB)
                return "https://placehold.co/500x750?text=No+Poster"

        except Exception as e:
            if attempt == 2:
                # Raise exception on final attempt so Streamlit cache doesn't cache the failure
                raise e
            import time
            time.sleep(0.5)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list= sorted(list(enumerate(distances)), reverse=True, key=lambda x : x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters =[]
    for i in movie_list:

        #movie_id = i[0]
        movie_id = int(movies.iloc[i[0]].movie_id)
        print(movie_id)
        #movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from the api
        recommended_movies.append(movies.iloc[i[0]].title)
        
        # Safely call fetch_poster and handle errors here to fallback without caching the error
        try:
            poster_url = fetch_poster(movie_id)
        except Exception as e:
            print(f"Error fetching poster for {movie_id}: {e}")
            poster_url = "https://placehold.co/500x750?text=No+Poster"
            
        recommended_movies_posters.append(poster_url)

    return recommended_movies, recommended_movies_posters


# A .pkl (pickle) file stores data in binary format, not plain text.
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
movies.reset_index(drop=True, inplace=True)

#similarity = pickle.load(open('similarity.pkl', 'rb'))
import os
import pickle
import gdown

url = "https://drive.google.com/file/d/1sBde_poOSeRmSMPwffo4zFM_Ti-BVXjc/view?usp=sharing"
OUTPUT = "similarity.pkl"

if not os.path.exists(OUTPUT):
    gdown.download(url, OUTPUT, quiet=False)

similarity = pickle.load(open(OUTPUT, "rb"))
print(type(similarity))
print(similarity.shape)

movies_list = movies['title'].values

st.markdown(
    """
    <h1 style="
        text-align: center; 
        color: white; 
        font-family: 'Outfit', sans-serif; 
        font-weight: 800; 
        font-size: 38px; 
        letter-spacing: -1px;
        background: linear-gradient(135deg, #ffffff 40%, #ff4b4b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 10px;
        margin-bottom: 30px;
        text-shadow: 0 4px 15px rgba(0, 0, 0, 0.6);
    ">
        Movie Recommendation System
    </h1>
    """,
    unsafe_allow_html=True
)

Selected_movie_name = st.selectbox(
    "Choose Your Favorite Movie",
    movies_list,
    index=None,
    placeholder="Search a movie..."
)

# This creates a button on your web app.
# st.write() prints or displays data on the Streamlit webpage.
if st.button("Recommend"):

    if Selected_movie_name is None:
        st.warning("⚠ Please select a movie first.")
        st.stop()

    with st.spinner("Finding similar movies..."):
        names, posters = recommend(Selected_movie_name)
    st.success("Recommendations Ready! 🍿")
    

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.markdown(f"<p style='text-align: center; color: white; font-weight: bold; font-size: 16px; margin-top: 5px;'>{names[i]}</p>", unsafe_allow_html=True)

st.markdown(
"""
<div style='text-align:center; margin-top: 150px; margin-bottom: 30px; font-family: "Outfit", sans-serif; color: #ffffff; line-height: 1.8;'>
    Made with ❤️ by <b>Mehul Agrawal</b>
    <br>
    <span style="color: #ffffff; font-size: 14px; font-weight: 500; letter-spacing: 0.5px;">Python | Streamlit | Machine Learning | TMDB API</span>
</div>
""",
unsafe_allow_html=True
)
