from flask import Flask, request, render_template
import gtts
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    tts1 = gtts.gTTS(text, lang="en")
    tts1.save("templates/gttsspeech.mp3")
    return render_template('data.html')