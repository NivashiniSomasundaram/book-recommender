import requests
import os

# Check if API Key is set in Render
API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")

if API_KEY:
    print(f"✅ DEBUG: API Key is set in Render: {API_KEY[:5]}****** (partially hidden)")
else:
    print("❌ ERROR: API Key is NOT set in Render. Check environment settings.")

def get_book_link(book_title):
    """Fetches a book's link from Google Books API."""
    
    if not API_KEY:
        print("❌ ERROR: API Key is missing! Make sure it's set in your environment variables.")
        return "API Key Missing!"

    url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}&key={API_KEY}"
    
    try:
        print(f"🔍 Fetching book link for: {book_title}")
        response = requests.get(url)
        print(f"📡 API Response Status: {response.status_code}")

        response.raise_for_status()  # Raise an error for HTTP issues

        data = response.json()
        if "items" in data and data["items"]:
            for item in data["items"]:
                info = item.get("volumeInfo", {})
                if "infoLink" in info:
                    print(f"✅ Found Book Link: {info['infoLink']}")
                    return info["infoLink"]
        
        print("⚠️ No book links found in API response.")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ ERROR: API Request Failed: {e}")
        return f"API Request Failed: {e}"

    return f"https://www.google.com/search?q={book_title.replace(' ', '+')}"

# Test the function when running the script
if __name__ == "__main__":
    test_title = "Harry Potter"
    print(f"📝 Testing with: {test_title}")
    print(f"🔗 Book Link: {get_book_link(test_title)}")
