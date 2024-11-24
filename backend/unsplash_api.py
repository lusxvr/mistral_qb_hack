import requests
from dotenv import load_dotenv
load_dotenv()
import os

def get_unsplash_image_url(query: str) -> str:
    """
    Fetches the URL of an image corresponding to the given natural language query from Unsplash.

    Args:
        query (str): The search query for the image.

    Returns:
        str: URL of the first valid image.
    """
    # Unsplash Search API endpoint
    endpoint = "https://api.unsplash.com/search/photos"
    
    # Parameters for the API request
    params = {
        "query": query,   # Search query
        "per_page": 1,    # Number of results to return
        "orientation": "landscape"  # Optional: Specify orientation (landscape/portrait/squarish)
    }
    
    # Headers for authorization
    headers = {
        "Authorization": f"Client-ID {os.getenv('UNSPLASH_ACCESS_KEY')}"
    }
    
    # Make the API request
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    
    # Parse the response JSON
    data = response.json()
    if "results" in data and len(data["results"]) > 0:
        return data["results"][0]["urls"]["regular"]  # Return the URL of the first image
    else:
        raise ValueError("No images found for the given query.")
