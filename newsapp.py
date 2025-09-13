import requests
import json

query = input("What topic are you interested in?: ")
response = requests.get(
    f"https://newsapi.org/v2/everything?q={query}&from=2025-07-02&sortBy=publishedAt&apiKey=7a51897558404703a638a2010fc8f030"
)

news = json.loads(response.text)

if news.get("status") != "ok" or "articles" not in news:
    print("Error fetching news:", news.get("message", "Unknown error"))
else:
    count = 0
    for article in news["articles"]:
        if count == 10:
            break
        print(article["title"])
        print(article["description"])
        print("-------------------------------------\n-------------------------------------\n")
        count += 1
