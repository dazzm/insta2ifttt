import json
from datetime import datetime
from flask import Flask, request
import requests
from _utils.insta import get_user_posts
app = Flask(__name__)

@app.route('/')
@app.route('/<path:path>')
def catch_all(path):
    input = request.json
    users = input["users"]
    index = datetime.now().time().hour % len(users)
    user = users[index]
    post = get_user_posts(user)[0]
    caption = '%s by <a href=instagram.com/p/%s> %s </a>' % (post.caption, post.shortcode, post.profile)
    r = requests.post(input["callback_url"], data={ 'value1': post.url, 'value2': caption })
    return r.text
    