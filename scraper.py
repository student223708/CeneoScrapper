import requests
import json
from arpgarse import Raw
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/39562616#tab=reviews"
all_reviews = []

while(url):
response = requests.get(url)

page_dom = BeautifulSoup(response.text, 'html.parser')



reviews = page_dom.select("div.js_product-review")
for review in reviews:

    review_id = review["data-entry-id"]

    author = review.select_one("span.user-post__author-name").text.strip()

    recommendation = review.select_one("span.user-post__author-recommendation > em").text.strip()
    recommendation = True if recommendation == "Polecam" else False
    if recommendation =="Nie polecam" else None

    stars = review.select_one("span-user-post__score-count").text.strip()

    content = review.select_one("div.user-post__text").text.strip()

    publish_date = review.select_one("span.user-post__published > ")

    purchase_date = review.select_one("span.user-post__published > ")

    useful = review.select_one("button.vote-yes > span").text.strip()

    useless = review.select_one("button.vote-no > span").text.strip()

    pros = review.select("div.review-feature__title--positivies ~ div")
    pros = [item for item in pros]

    cons = review.select("div.review-feature__title--negatives ~ div")
    cons = [item for item in cons]


    single_review = {
        "review_id": review_id,
        "recommendation": author,
        "stars": recommendation,
        "content":content,
        "publish_date": publish_date,
        "purchase_date":purchase_date,
        "useful":useful,
        "useless": useless,
        "pros":pros,
        "cons":cons
    }
    all_reviews append.(single_review)

next_page = page_dom.select_one("a.pagination__text")
if next_page:
    url = "https://www.ceneo.pl"+next_page["href"]
else: url = None
review = page_dom.select_one("div.js_product-review")

with open ("./reviews/39562616.json", "w", endoding="UTF-8") as 
f:
    json.dump(all_reviews, f, indent=4, ensure_ascii=False)

    #39562616
    #95365253