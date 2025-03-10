import requests
import os

def get_book_link(book_title):
    """Fetches a book's link from Google Books API."""
    
    API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")  # Get API key from Render environment
    print(f"Using API Key: {API_KEY}")  # DEBUG: Check if API key is retrieved

    if not API_KEY:
        print("ERROR: API Key is missing!")
        return "API Key Missing!"

    url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}&key={API_KEY}"
    
    try:
        response = requests.get(url).json()
        if "items" in response:
            for item in response["items"]:
                info = item.get("volumeInfo", {})
                if "infoLink" in info:
                    return info["infoLink"]
    except Exception as e:
        print(f"Error fetching book link: {e}")

    return f"https://www.google.com/search?q={book_title.replace(' ', '+')}"
