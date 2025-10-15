from flask import Flask, render_template
from artist import Artist

app = Flask(__name__)

@app.route('/')
def index():
    # Create a sample artist with media
    sample_artist = Artist(
        "John Doe",
        "Painter",
        "New York",
        profile_pic='images/profile.jpg',
        video='videos/performance.mp4',
        audio='audio/song.mp3'
    )
    sample_artist.add_to_portfolio("Starry Night Rework")
    sample_artist.add_to_portfolio("Abstract Cityscape")
    return render_template('index.html', artist=sample_artist)

@app.route('/dance')
def dance():
    return render_template('dance.html')

@app.route('/tourism')
def tourism():
    return render_template('tourism.html')

@app.route('/animal_husbandry')
def animal_husbandry():
    return render_template('animal_husbandry.html')

@app.route('/startups')
def startups():
    return render_template('startups.html')

@app.route('/diplomacy')
def diplomacy():
    return render_template('diplomacy.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)