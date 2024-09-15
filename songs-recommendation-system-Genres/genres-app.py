import streamlit as st
import pandas as pd
import pickle
import ast

# Load the pickle file
with open('Genres_Recommendation.pkl', 'rb') as file:
    data = pickle.load(file)

# Extract DataFrame and labels
genre_clean = data['genre_clean']
labels_cosine = data['labels_cosine']

# Add cluster labels to the DataFrame
genre_clean['cluster'] = labels_cosine

# Convert track_url strings to dictionaries if necessary
def convert_to_dict(url_str):
    try:
        return ast.literal_eval(url_str)
    except (ValueError, SyntaxError):
        return {}

genre_clean['track_url'] = genre_clean['track_url'].apply(convert_to_dict)

# Function to recommend songs
def recommend_songs(song_name, data, num_recommendations):
    song_name = song_name.lower().strip()
    data['Name'] = data['Name'].str.lower().str.strip()
    if song_name in data['Name'].values:
        cluster = data.loc[data['Name'] == song_name, 'cluster'].values[0]
        recommendations = data[(data['cluster'] == cluster) & (data['Name'] != song_name)]
        if len(recommendations) > num_recommendations:
            recommendations = recommendations.sample(num_recommendations)
        return recommendations[['Name', 'Artist', 'genres', 'album_image_url', 'track_url']]
    return pd.DataFrame()  # Return an empty DataFrame if the song is not found

# Streamlit app layout
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #1f4037, #99f2c8);
        color: white;
    }
    .title {
        color: white;
        font-size: 40px;
        text-align: center;
        margin-bottom: 20px;
    }
    .recommendation {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    .recommendation img {
        max-width: 100px;
        margin-right: 15px;
    }
    .recommendation-details {
        font-size: 16px;
    }
    .recommendation-details a {
        color: #1db954;
        text-decoration: none;
    }
    .recommendation-details a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Song Recommendation System</div>', unsafe_allow_html=True)

# Dropdown for song selection
song_names = genre_clean['Name'].unique()
selected_song = st.selectbox("Select a song for recommendation:",options=song_names, key='select_song')

# Button to get recommendations
if st.button('Get Recommendations', key='recommend'):
    recommendations = recommend_songs(selected_song, genre_clean, 10)
    if not recommendations.empty:
        for _, row in recommendations.iterrows():
            track_url = row['track_url']
            url = track_url.get('spotify', '')
            st.markdown(f'<div class="recommendation">'
                        f'<img src="{row["album_image_url"]}" alt="Album Image">'
                        f'<div class="recommendation-details">'
                        f'<strong>{row["Name"]}</strong><br>'
                        f'Artist: {row["Artist"]}<br>'
                        f'Genre: {row["genres"]}<br>'
                        f'<a href="{url}" target="_blank">Play on Spotify</a>'
                        f'</div></div>',
                        unsafe_allow_html=True)
    else:
        st.write("No recommendations available.")
