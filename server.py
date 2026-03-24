from mcp.server.fastmcp import FastMCP
from services import search_movies, multi_search, trending_search, get_review_details, get_movie_reviews, get_tv_reviews

# Initialize MCP server
mcp = FastMCP("tmdb-server")

@mcp.tool()
async def tmdb_movie_reviews(movie_id: int, language: str = "en-US", page: int = 1) -> str:
    """
    Get the user reviews for a movie from TMDB.
    Args:
        movie_id: The TMDB movie ID (required).
        language: Language code (default: en-US).
        page: Page of results (default: 1).
    Returns:
        Formatted string with movie reviews.
    """
    try:
        results = get_movie_reviews(movie_id, language, page)
        reviews = results.get("results", [])
        if not reviews:
            return "No reviews found for this movie."
        return "\n---\n".join([
            f"Author: {review.get('author', 'N/A')}\n"
            f"Content: {review.get('content', 'N/A')}\n"
            f"Created At: {review.get('created_at', 'N/A')}\n"
            f"URL: {review.get('url', 'N/A')}\n"
            for review in reviews
        ])
    except Exception as e:
        return f"Error fetching movie reviews: {str(e)}"


@mcp.tool()
async def tmdb_tv_reviews(series_id: int, language: str = "en-US", page: int = 1) -> str:
    """
    Get the reviews that have been added to a TV show from TMDB.
    Args:
        series_id: The TMDB series ID (required).
        language: Language code (default: en-US).
        page: Page of results (default: 1).
    Returns:
        Formatted string with TV show reviews.
    """
    try:
        results = get_tv_reviews(series_id, language, page)
        reviews = results.get("results", [])
        if not reviews:
            return "No reviews found for this TV show."
        return "\n---\n".join([
            f"Author: {review.get('author', 'N/A')}\n"
            f"Content: {review.get('content', 'N/A')}\n"
            f"Created At: {review.get('created_at', 'N/A')}\n"
            f"URL: {review.get('url', 'N/A')}\n"
            for review in reviews
        ])
    except Exception as e:
        return f"Error fetching TV show reviews: {str(e)}"

@mcp.tool()
async def tmdb_search_movies(query: str, include_adult: bool = False, language: str = "en-US", page: int = 1, primary_release_year: str = None, region: str = None, year: str = None) -> str:
    """
    Search for movies using the TMDB API.
    Args:
        query: The text query to search for (required).
        include_adult: Whether to include adult content (default: False).
        language: Language code (default: en-US).
        page: Page of results (default: 1).
        primary_release_year: Filter by release year (optional).
        region: Filter by region (optional).
        year: Filter by year (optional).
    Returns:
        Formatted string with movie search results.
    """
    try:
        results = search_movies(query, include_adult, language, page, primary_release_year, region, year)
        movies = results.get("results", [])
        if not movies:
            return "No movies found matching the search criteria."
        return "\n---\n".join([
            f"Title: {movie.get('title', movie.get('original_title', 'N/A'))}\n"
            f"Release Date: {movie.get('release_date', 'N/A')}\n"
            f"Overview: {movie.get('overview', 'N/A')}\n"
            f"Vote Average: {movie.get('vote_average', 'N/A')}\n"
            for movie in movies
        ])
    except Exception as e:
        return f"Error searching for movies: {str(e)}"


@mcp.tool()
async def tmdb_multi_search(query: str, include_adult: bool = False, language: str = "en-US", page: int = 1) -> str:
    """
    Multi-search for movies, TV shows, and people using the TMDB API.
    Args:
        query: The text query to search for (required).
        include_adult: Whether to include adult content (default: False).
        language: Language code (default: en-US).
        page: Page of results (default: 1).
    Returns:
        Formatted string with multi-search results.
    """
    try:
        results = multi_search(query, include_adult, language, page)
        items = results.get("results", [])
        if not items:
            return "No results found matching the search criteria."
        return "\n---\n".join([
            f"Type: {item.get('media_type', 'N/A')}\n"
            f"Title/Name: {item.get('title', item.get('name', 'N/A'))}\n"
            f"Overview: {item.get('overview', 'N/A')}\n"
            for item in items
        ])
    except Exception as e:
        return f"Error performing multi-search: {str(e)}"


@mcp.tool()
async def tmdb_trending_search(time_window: str = "day", language: str = "en-US") -> str:
    """
    Get trending movies, TV shows, and people from TMDB.
    Args:
        time_window: 'day' or 'week' (default: 'day').
        language: Language code (default: en-US).
    Returns:
        Formatted string with trending results.
    """
    try:
        results = trending_search(time_window, language)
        items = results.get("results", [])
        if not items:
            return "No trending results found."
        return "\n---\n".join([
            f"Type: {item.get('media_type', 'N/A')}\n"
            f"Title/Name: {item.get('title', item.get('name', 'N/A'))}\n"
            f"Overview: {item.get('overview', 'N/A')}\n"
            for item in items
        ])
    except Exception as e:
        return f"Error fetching trending results: {str(e)}"

@mcp.tool()
async def tmdb_review_details(review_id: str) -> str:
    """
    Retrieve the details of a movie or TV show review from TMDB.
    Args:
        review_id: The TMDB review ID (required).
    Returns:
        Formatted string with review details.
    """
    try:
        review = get_review_details(review_id)
        return (
            f"Author: {review.get('author', 'N/A')}\n"
            f"Content: {review.get('content', 'N/A')}\n"
            f"Created At: {review.get('created_at', 'N/A')}\n"
            f"Media Title: {review.get('media_title', 'N/A')}\n"
            f"Media Type: {review.get('media_type', 'N/A')}\n"
            f"URL: {review.get('url', 'N/A')}\n"
        )
    except Exception as e:
        return f"Error fetching review details: {str(e)}"
