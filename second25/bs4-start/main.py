from bs4 import BeautifulSoup
import requests

#robots.txt

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

text = []
link = []
upvot = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

for article_tag in articles:
    article_link = article_tag.find('a')["href"]
    link.append(article_link)
    article_text = article_tag.getText()
    text.append(article_text)

for index, max_upvot in enumerate(upvot):
    if max_upvot == max(upvot):
        print(text[index])
        print(link[index])
        print(max_upvot)
        exit


""" with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'lxml')
#print(soup.title.name)
#print(soup.title.string)
#print(soup.prettify())
#print(soup.p)

all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

#for tag in all_anchor_tags:
    #print(tag.getText())
    #print(tag.get("href"))
    
heading = soup.find(name="h1", id="name")
#print(heading)

company_url = soup.select_one(selector="#name")
print(company_url)

heading = soup.select(".    ")
print(heading) """