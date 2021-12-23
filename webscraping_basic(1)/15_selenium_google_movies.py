import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=google+movies&rlz=1C1FKPE_enUS963US963&oq=google+movies&aqs=chrome..69i57j0i512l9.2800j0j15&sourceid=chrome&ie=UTF-8#wxpd=:true"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
movies = soup.find_all("div", attrs={"class":"RWuggc kCrYT"})
print(len(movies))
# print(movies)

# with open("movie.html", "w", encoding ="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify())

for movie in movies:
    title = movie.find("div", attrs={"class":"BNeawe s3v9rd AP7Wnd"}).get_text()
    print(title)