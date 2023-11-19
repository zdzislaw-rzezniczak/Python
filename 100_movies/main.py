import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


#<h3 class="title">

response = requests.get(URL)
empire_online_page = response.text

soup = BeautifulSoup(empire_online_page, "html.parser")

article_titles = []
title = soup.find(name="h3", class_="title")


for movie_title in soup.find_all(name="h3", class_="title"):
    article_titles.append(movie_title.getText())


article_titles.reverse()


with open("100 movies.txt", mode="w", encoding="utf-8") as file:
    for movie in article_titles:
        file.write(f"{movie}\n")


