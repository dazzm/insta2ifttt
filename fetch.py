import json
from flask import Flask, request
from _utils.insta import get_hashtag_posts
app = Flask(__name__)

@app.route('/')
@app.route('/<path:path>')
def catch_all(path):
    input = request.json
    post = get_hashtag_posts(input["tag"])
    return post
    
