import requests
import os

api_key = os.getenv("GOOGLE_BOOKS_API_KEY") 

def get_book_link(book_title):
    """
    Fetches a book's link from Google Books API.
    Falls back to a Google Search link if not found.
    """
    api_key = os.getenv("GOOGLE_BOOKS_API_KEY")
    url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}&key={api_key}"
    
    try:
        response = requests.get(url).json()
        print("API Response:", response)  # Debugging: Print full API response
        
        if "items" in response:
            for item in response["items"]:
                info = item.get("volumeInfo", {})
                if "infoLink" in info:
                    print(f"Found link for {book_title}: {info['infoLink']}")
                    return info["infoLink"]
    except Exception as e:
        print("Error fetching book link:", e)

    # If no link found, return a Google Search link
    search_link = f"https://www.google.com/search?q={book_title.replace(' ', '+')}"
    print(f"Falling back to Google Search link: {search_link}")
    return search_link


# Test the function
if __name__ == "__main__":
    book_title = "The Psychology of Money"
    print(f"Fetching link for: {book_title}")
    link = get_book_link(book_title)
    print(f"Book Link: {link}")
