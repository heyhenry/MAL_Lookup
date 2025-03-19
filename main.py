import requests
import json

api_url = f"https://api.jikan.moe/v4/manga?type=manhwa&status=complete"
my_request = requests.get(api_url)
data = my_request.json()
for manhwa in data["data"]:
    title = manhwa.get("title", "N/A")
    chapters = manhwa.get("chapters", "Unknown")
    description = manhwa.get("synopsis", "No description available")

    print(f"Title: {title}")
    print(f"Chapters: {chapters}")
    print(f"Description: {description}")
    print("-"*40)