import requests
from flask import Flask, render_template, request
import json

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
    return f"{base_url}/items/{id}"


db = {}
app = Flask("DayNine")

popular_articles = requests.get(popular).json()['hits']
new_articles = requests.get(new).json()['hits']


def find(request):
    query = request.args.get('order_by')
    if(query == 'new'):
        data = new_articles
        db = new_articles
        title = "New"
    elif(query == 'popular'):
        data = popular_articles
        db = popular_articles
        title = "Popular"
    else:
        data = popular_articles
        db = popular_articles
        title = "Popular"
    return render_template(
        "index.htm",
        hits=data,
        query=query
    )


@app.route("/")
def home():
    return find(request)


@app.route("/?order_by=new")
def new_board():
    return find(request)


@app.route("/?order_by=popular")
def popular_board():
    return find(request)


@app.route("/<id>")
def detail(id):
    detail_url = make_detail_url(id)
    request_detail = requests.get(detail_url).json()
    db = request_detail
    return render_template(
        "detail.htm",
        data=request_detail
    )


app.run(host="0.0.0.0", port="5000")
