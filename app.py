from flask import Flask, render_template, url_for, request
import gtts
app = Flask(__name__)

 

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")



@app.route('/result',methods=['POST', 'GET'])
def result():
    text = request.form['speech']
    tts1 = gtts.gTTS(text, lang="en")
    tts1.save("templates/gttsspeech.mp3")
    return render_template('index.html', name = text)
    




if __name__ == "__main__":
    app.run(debug=True)