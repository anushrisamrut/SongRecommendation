🎵 Conditional-Based Song Recommendation System
Welcome to the Conditional-Based Song Recommendation System project! This advanced machine learning project offers a unique approach to personalized music recommendations, focusing on genre-specific suggestions tailored to your tastes. Leveraging the power of clustering techniques and natural language processing, this system is designed to help users navigate the vast world of music with ease.

🌟 Project Overview
As the music industry continues to expand, so does the challenge of discovering the perfect tracks. Our recommendation system addresses this by offering genre-based suggestions that adapt to the user's specific preferences. The model is built using state-of-the-art techniques and is deployed via Streamlit for a seamless user experience.

🚀 Key Features
Data Collection via API Scraping: We’ve gathered an extensive dataset of songs, including key attributes like genre, acousticness, danceability, energy, and more, directly from streaming platforms using advanced API scraping methods.

🧩Sophisticated Clustering Techniques:
K-Means Clustering: Applied for basic genre clustering, achieving a silhouette score of 0.6405.
Hybrid Model (PCA + K-Means): Enhanced clustering by reducing dimensionality first, resulting in a silhouette score of 0.6406.
TF-IDF + Cosine Similarity + K-Means: Our most successful method, combining textual analysis with clustering, produced an impressive and best silhouette score of 🏆 0.9311.
Streamlit Deployment: The model is deployed through a user-friendly Streamlit interface, providing instant genre-based recommendations.

🎧 How It Works
Data Scraping & Preprocessing:

🎼We start by scraping detailed music data, including attributes such as Name, Artist, Genres, Acousticness, Danceability, Energy, Track URL, and Album Image URL.
The data is then cleaned and formatted to ensure consistency and readiness for model training.
Feature Engineering:

Text data is converted into numerical features using TF-IDF Vectorization, capturing the importance of terms within the dataset.
PCA (Principal Component Analysis) is employed to reduce the feature space, simplifying the data while retaining essential characteristics for clustering.
Clustering:

We utilize K-Means Clustering to group songs into clusters based on their attributes.
The final and most effective model combines TF-IDF Vectorization with Cosine Similarity and K-Means Clustering for superior genre-based clustering.
Recommendation Engine:

The system generates personalized song recommendations by identifying tracks within the same cluster as the input song.
The recommendations are not only genre-specific but also tailored to the user’s unique preferences.
Deployment:

The system is deployed via Streamlit, offering an interactive and visually appealing interface. Users can input their favorite genres or songs to receive instant, customized recommendations.
🎨 Visualization

Example of the deployed app, showcasing genre-based song recommendations.

🛠️ Installation & Usage
To get started with this project, follow these steps:

Clone the Repository:
bash
Copy code
git clone https://github.com/DivyaKopparthi71/songs-recommendation-system-Genres
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Run the Streamlit App:
bash
Copy code
streamlit run your_app.py
Explore: Input a genre or song to receive personalized recommendations.
🏆 Results & Performance
K-Means Clustering: Achieved a silhouette score of 0.6405.
PCA + K-Means Clustering: Improved to 0.6406.
TF-IDF + Cosine Similarity + K-Means: Delivered an outstanding silhouette score of 0.9311.
These results demonstrate the system's ability to effectively group and recommend songs based on genre-specific preferences, providing users with a tailored music experience.

📊 Deployment
The model is live and accessible through Streamlit. Check out the deployed version here:https://mygenres-gfbpwq9zekmxcfrpe5fsjr.streamlit.app/

🤝 Contributing
We welcome contributions from the community! Please feel free to fork the repository, create a branch, and submit a pull request. All types of contributions are appreciated.

📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

🎤 Acknowledgements
Thanks to the open-source community for providing valuable libraries like Scikit-learn, Pandas, and Streamlit.
Special thanks to Spotify and other platforms for their API services.
