from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")
article = soup.find_all(name="a", class_="StoryLink")
article_text = []
article_link = []
for articl in article:
    text = articl.getText()
    article_text.append(text)
    link = articl.get("href")
    article_link.append(link)

article_upvotes = [score.getText().split()[0] for score in soup.find_all(name="span", class_="score")]

highest_vote = max(article_upvotes)
highest_index = article_upvotes.index(highest_vote)

highest_vote_article = article_text[highest_index]
highest_vote_link = article_link[highest_index]

print(highest_vote_article)

