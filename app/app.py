from flask import Flask, render_template,request
from vagalume import lyrics

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        artist = request.form.get("artist")
        music = request.form.get("music")
        if artist and music:
            result = lyrics.find(artist,music)
            song = (result.song.lyric)

        else: 
            song = "Preencha os campos corretamente.."
    return render_template('index.html', music=music, song=song)

if __name__ == '__main__':
    app.run(debug=True)