import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

empireonline = response.text
soup = BeautifulSoup(empireonline, "html.parser")
best_movie = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

BMOAT = [movie.getText() for movie in best_movie]

with open("movies.txt", "w") as movie:
    for  best in BMOAT[::-1]:
        movie.write(f"{best}\n")
    
