# fonts used: 'Maven Pro' or 'Maven Pro Black' for general, 'Jokerman' for title
import tkinter as tk
import requests
import json
from PIL import Image, ImageTk
import webbrowser
    
response = requests.get('https://api.jikan.moe/v4/random/manga?type=manhwa&status=complete&sfw=true')
data = response.json()
with open('sample.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

def load_json(filename):
    with open(filename, 'r') as file:    
        return json.load(file)

sample = load_json('sample.json')

# usage of wording: 'manga' to encompass all reading forms as MAL does
def get_random_manga(content_type):
    global sample
    api_url = f'https://api.jikan.moe/v4/random/manga?type={content_type}&status=complete'
    content_request = requests.get(api_url)
    sample = content_request.json() 
    print(sample)

def redirect_link(result_url):
    webbrowser.open(result_url)

root = tk.Tk()
root.geometry('1100x800') # wxh

search_var = tk.StringVar()

# widgets

title = tk.Label(root, text='MAL Lookup', font=('Jokerman', 32))
subtitle = tk.Label(root, text='Search a list of completed manhwa, anime, manga and etc.', font=('Maven Pro', 12))

anime_button = tk.Button(root, text='Anime', font=('Maven Pro Black', 18))
manga_button = tk.Button(root, text='Manga', font=('Maven Pro Black', 18))
manhwa_button = tk.Button(root, text='Manhwa', font=('Maven Pro Black', 18))
manhua_button = tk.Button(root, text='Manhua', font=('Maven Pro Black', 18))

result_title = tk.Label(root, text=sample['data']['titles'][0]['title'], font=('Maven Pro Black', 24))
result_img = ImageTk.PhotoImage(Image.open(requests.get(sample['data']['images']['jpg']['image_url'], stream=True).raw).resize((300,400), Image.Resampling.LANCZOS))
result_img_panel = tk.Label(root, image=result_img)
result_type = tk.Label(root, text=f'Type: {sample['data']['type']}', font=('Maven Pro', 18))
result_volumes = tk.Label(root, text=f'Volumes: {sample['data']['volumes']}', font=('Maven Pro', 18))
result_chapters = tk.Label(root, text=f'Chapters: {sample['data']['chapters']}', font=('Maven Pro', 18))
published_from = sample['data']['published'].get('from') or 'null'
published_to = sample['data']['published'].get('to') or 'null'
from_year = published_from[:4] if published_from != 'null' else 'null'
to_year = published_to[:4] if published_to != 'null' else 'null'
result_published = tk.Label(root, text=f'Published: {from_year} - {to_year}', font=('Maven Pro', 18))
result_genres = tk.Label(root, text=f'Genres: {', '.join([genre['name'] for genre in sample['data']['genres'][0:len(sample['data']['genres'])]])}', font=('Maven Pro', 18))
result_theme = tk.Label(root, text=f'Themes: {', '.join([theme['name'] for theme in sample['data']['themes'][0:len(sample['data']['themes'])]])}', font=('Maven Pro', 18))
result_score = tk.Label(root, text=f'Score: {sample['data']['score']} / 10.00', font=('Maven Pro', 18))
result_synopsis_title = tk.Label(root, text='Synopsis: ', font=('Maven Pro', 18))
content_synopsis = sample['data'].get('synopsis') or 'null'
content_synopsis = content_synopsis[:369] if content_synopsis != 'null' else 'null'
result_synopsis = tk.Label(root, text=f'{content_synopsis}', font=('Maven Pro', 12), wraplength=600)
read_more = tk.Label(root, text='read more...', font=('Maven Pro', 10), foreground='blue')

read_more.bind("<Button-1>", lambda event: redirect_link(sample['data']['url']))

# widget placement

title.place(x=400, y=10)
subtitle.place(x=325, y=80)

anime_button.place(x=250, y=120)
manga_button.place(x=400, y=120)
manhwa_button.place(x=550, y=120)
manhua_button.place(x=730, y=120)

result_title.place(x=150, y=200)
result_img_panel.place(x=150, y=275)
result_type.place(x=480, y=275)
result_volumes.place(x=480, y=325)
result_chapters.place(x=480, y=375)
result_published.place(x=480, y=425)
result_genres.place(x=480, y=475)
result_theme.place(x=480, y=525)
result_score.place(x=480, y=575)
result_synopsis_title.place(x=480, y=625)
result_synopsis.place(x=480, y=665)
read_more.place(x=1000, y=770)

root.mainloop()

