from flask import Flask, request, Response, url_for
import os
from dotenv import load_dotenv
import requests

load_dotenv()

GH_TOKEN = os.environ["GITHUB_TOKEN"]
GH_USERNAME = os.environ["GITHUB_USERNAME"]

app = Flask(__name__)


@app.route('/')
def create_webhook():
    repo = 'webhooks-flask-github'
    headers = {
        "accept": "application/vnd.github+json",
        "authorization": f"Bearer {GH_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    params = {
        "name": "web",
        "config": {
            "url": url_for("respond")
        },
        "events": ["push"]
    }

    api_url = "https://api.github.com/"

    create_url = f"{api_url}repos/{GH_USERNAME}/{repo}/hooks"

    response = requests.post(url=create_url, headers=headers, params=params)
    print(response.json)

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json) # Handle webhook request here
    return Response(status=200)

if __name__ == "__main__":
    app.run(debug=True, port=5009)