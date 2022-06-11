import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_text = response.text

soup = BeautifulSoup(website_text, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movie_title = [movie.getText() for movie in movies]

movie_list = movie_title[::-1]

with open("movies.txt", mode="w") as file:
    for name in movie_list:
        file.write(f"{name}\n")







