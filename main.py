from flask import Flask, render_template, url_for, redirect, request
import openai
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/ttp")
def ttp():
    return render_template("ttp.html")

@app.route("/ptt")
def ptt():
    return render_template("ptt.html")

@app.route("/tips")
def tips():
    return render_template("tips.html")

@app.route("/community")
def community():
    return render_template("community.html")

@app.route("/get_gen_pres/<query>", methods=['GET','POST'])
# Set up OpenAI API credentials
def generated_text(query):
    print(query)
    openai.api_key = "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"
    prompt = '''Create a presentation  {} with slide number and its content in paragraph of 50 words with 12 slides,give slides ONLY in json format containing title and content
                '''.format(query)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.6,
        #frequency_penalty = 0,
        presence_penalty = 1,
    )
    presentation_text = response.choices[0].text
    return presentation_text.lower()

app.run(port=5000, debug=True, host="0.0.0.0")