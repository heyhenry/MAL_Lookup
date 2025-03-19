import requests
import json

j_url = "https://api.jikan.moe/v4/manga?type=manhwa&status=complete&limit=1&sfw=true&genres=17"
with open('sample.json', 'w') as outfile:
    json.dump(requests.get(j_url).json(), outfile, indent=4)