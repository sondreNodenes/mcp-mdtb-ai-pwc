# TMDB Movie Search Service
import os
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

# Movie Reviews Service
def get_movie_reviews(movie_id: int, language: str = "en-US", page: int = 1) -> dict:
    """
    Get the user reviews for a movie from TMDB.
    Args:
        movie_id: The TMDB movie ID (required).
        language: ISO 639-1 value to display translated data (default: en-US).
        page: Page of results to return (default: 1).
    Returns:
        Dictionary containing TMDB movie reviews results (keys: id, page, results, total_pages, total_results).
    """
    api_key = os.getenv("TMDB_API_KEY")
    if not api_key:
        raise RuntimeError("TMDB_API_KEY not set in environment variables.")

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews"
    params = {
        "language": language,
        "page": page,
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "accept": "application/json",
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

# TV Series Reviews Service
def get_tv_reviews(series_id: int, language: str = "en-US", page: int = 1) -> dict:
    """
    Get the reviews that have been added to a TV show from TMDB.
    Args:
        series_id: The TMDB series ID (required).
        language: ISO 639-1 value to display translated data (default: en-US).
        page: Page of results to return (default: 1).
    Returns:
        Dictionary containing TMDB TV reviews results (keys: id, page, results, total_pages, total_results).
    """
    api_key = os.getenv("TMDB_API_KEY")
    if not api_key:
        raise RuntimeError("TMDB_API_KEY not set in environment variables.")

    url = f"https://api.themoviedb.org/3/tv/{series_id}/reviews"
    params = {"language": language, "page": page}
    headers = {"Authorization": f"Bearer {api_key}", "accept": "application/json"}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

# Review Details Service
def get_review_details(review_id: str) -> dict:
    """
    Retrieve the details of a movie or TV show review from TMDB.
    Args:
        review_id: The TMDB review ID (required).
    Returns:
        Dictionary containing TMDB review details.
    """
    api_key = os.getenv("TMDB_API_KEY")
    if not api_key:
        raise RuntimeError("TMDB_API_KEY not set in environment variables.")

    url = f"https://api.themoviedb.org/3/review/{review_id}"
    headers = {"Authorization": f"Bearer {api_key}", "accept": "application/json"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

# Trending Search Service
def trending_search(time_window: str = "day", language: str = "en-US") -> dict:
    """
    Get trending movies, TV shows, and people from TMDB.
    Args:
        time_window: Either 'day' or 'week' (default: 'day').
        language: ISO 639-1 value to display translated data (default: en-US).
    Returns:
        Dictionary containing TMDB trending results (keys: page, results, total_pages, total_results).
    """
    api_key = os.getenv("TMDB_API_KEY")
    if not api_key:
        raise RuntimeError("TMDB_API_KEY not set in environment variables.")

    url = f"https://api.themoviedb.org/3/trending/all/{time_window}"
    params = {"language": language}
    headers = {"Authorization": f"Bearer {api_key}", "accept": "application/json"}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

# Multi Search Service
def multi_search(query: str, include_adult: bool = False, language: str = "en-US", page: int = 1) -> dict:
    """
    Search for movies, TV shows, and people using the TMDB multi search API.
    Args:
        query: The text query to search for (required).
        include_adult: Whether to include adult (pornography) content in the results (default: False).
        language: ISO 639-1 value to display translated data (default: en-US).
        page: Page of results to return (default: 1).
    Returns:
        Dictionary containing TMDB multi search results (keys: page, results, total_pages, total_results).
    """
    # TODO: implementer denne service'en

def search_movies(query: str, include_adult: bool = False, language: str = "en-US", page: int = 1, primary_release_year: str = None, region: str = None, year: str = None) -> dict:
    """
    Search for movies using the TMDB API.
    Args:
        query: The text query to search for (required).
        include_adult: Whether to include adult (pornography) content in the results (default: False).
        language: ISO 639-1 value to display translated data (default: en-US).
        page: Page of results to return (default: 1).
        primary_release_year: Filter the results to only the year provided (optional).
        region: Specify a ISO 3166-1 code to filter release dates (optional).
        year: Filter the results to only those with a matching release year (optional).
    Returns:
        Dictionary containing TMDB search results (keys: page, results, total_pages, total_results).
    """
    # TODO: implementer denne service'en



# Optionally, you can add more TMDB endpoints here as needed.


# if __name__ == "__main__":
#     # Example usage
#     try:
#         # results = search_movies("Inception", include_adult=False, language="en-US", page=1)
#         # print(results)
#         # Example multi search
#         # multi_results = multi_search("Inception", include_adult=False, language="en-US", page=1)
#         # print(multi_results)
#         # Example trending search
#         # trending_results = trending_search(time_window="day", language="en-US")
#         # print(trending_results)
#         recommendations_results = get_review_details("640b2aeecaaca20079decdcc")
#         print(recommendations_results)
#     except Exception as e:
#         print(f"Error searching for movies: {str(e)}")