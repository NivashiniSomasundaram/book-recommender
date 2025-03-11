import requests
import os

# Check if API Key is set in Render
API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")

if API_KEY:
    print("✅ DEBUG: API Key is set in Render (value hidden for security).")
else:
    print("❌ ERROR: API Key is NOT set in Render. Check environment settings.")

def get_book_link(book_title):
    """Fetches a book's link from Google Books API."""
    
    if not API_KEY:
        print("ERROR: API Key is missing! Make sure it's set in your environment variables.")
        return "API Key Missing!"

    url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}&key={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues

        data = response.json()
        if "items" in data:
            for item in data["items"]:
                info = item.get("volumeInfo", {})
                if "infoLink" in info:
                    return info["infoLink"]
        
        print("No book links found in API response.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching book link: {e}")

    return f"https://www.google.com/search?q={book_title.replace(' ', '+')}"

# Test the function when running the script
if __name__ == "__main__":
    test_title = "Harry Potter"
    print(f"Testing with: {test_title}")
    print(f"Book Link: {get_book_link(test_title)}")
