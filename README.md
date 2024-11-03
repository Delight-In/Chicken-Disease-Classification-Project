# Movie Recommendation System

## Overview
This Movie Recommendation System is designed to suggest movies to users based on a content-based tagging strategy. The system utilizes a combination of movie metadata and user-selected inputs to provide tailored recommendations. It features a user-friendly interface built with Streamlit and leverages The Movie Database (TMDb) API for fetching movie posters.

## Features
- **Content-Based Recommendations**: Suggests movies similar to the selected title based on content features.
- **Dynamic Movie Poster Fetching**: Retrieves and displays movie posters using the TMDb API.
- **Popular Movies Section**: Displays the top 10 popular movies to give users additional viewing options.

## Requirements
- Python 3.x
- Libraries: `pickle`, `streamlit`, `requests`, `pandas` (for data handling)
- An API key from TMDb (replace with your own key)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd Movie_Recommendation_System
   ```

2. **Install Required Libraries**:
   Make sure you have `streamlit` and `requests` installed. You can install them using pip:
   ```bash
   pip install streamlit requests pandas
   ```

3. **Data Files**:
   Place your preprocessed data files (`movie_list.pkl`, `similarity.pkl`, `popularity.pkl`) in the `Source/Preprocess/` directory.

4. **API Key**:
   Replace the API key in the `fetch_poster` function with your own TMDb API key:
   ```python
   url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API}language=en-US"
   ```

5. **Run the Application**:
   Launch the Streamlit app by running:
   ```bash
   streamlit run app.py
   ```

## Code Overview

### Main Functions

- **`fetch_poster(movie_id)`**:
  - Fetches the movie poster URL from TMDb based on the movie ID.
  
- **`recommend(movie)`**:
  - Recommends movies similar to the selected movie by computing distances from a precomputed similarity matrix.
  - Returns the names and poster URLs of recommended movies.

### User Interface
- **Movie Selection**: A dropdown menu allows users to select a movie from the dataset.
- **Recommendation Display**: Upon clicking the "Show Recommendation" button, the app displays the recommended movies along with their posters.
- **Popular Movies Section**: Displays the top 10 most popular movies, also with their posters.

## Usage
- Select a movie from the dropdown to get recommendations.
- Explore the "Top 10 Popular Movies" for additional options.
