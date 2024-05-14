from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'API KEY'

# Default route to serve index.html
@app.route("/")
def index():
    return render_template("index.html")

# API route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get message from request parameters
    message = request.form.get("message")

    completion=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user","content": message}]
    )
    print(completion.choices[0].message)