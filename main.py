# fonts used: 'Maven Pro' or 'Maven Pro Black' for general, 'Jokerman' for title

import tkinter as tk

root = tk.Tk()
root.geometry('1100x600') # wxh

search_var = tk.StringVar()

# widgets

title = tk.Label(text='MAL Lookup', font=('Jokerman', 32))
subtitle = tk.Label(text='Search a list of completed manhwa, anime, manga and etc.', font=('Maven Pro', 12))

anime_button = tk.Button(text='Anime', font=('Maven Pro Black', 18))
manga_button = tk.Button(text='Manga', font=('Maven Pro Black', 18))
manhwa_button = tk.Button(text='Manhwa', font=('Maven Pro Black', 18))
manhua_button = tk.Button(text='Manhua', font=('Maven Pro Black', 18))




# widget placement

title.place(x=400, y=10)
subtitle.place(x=325, y=80)

anime_button.place(x=250, y=120)
manga_button.place(x=400, y=120)
manhwa_button.place(x=550, y=120)
manhua_button.place(x=730, y=120)

root.mainloop()

