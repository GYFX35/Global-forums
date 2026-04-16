from flask import Flask, render_template, request, jsonify
from artist import Artist

app = Flask(__name__)

@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    data = request.json
    user_message = data.get('message', '').lower()

    # Simple AI logic
    if 'hello' in user_message or 'hi' in user_message:
        response = "Hello! I am your Arts & Talents assistant. How can I help you today?"
    elif 'artist' in user_message:
        response = "You can view featured artists on our homepage. We showcase painters, musicians, and more!"
    elif 'dance' in user_message:
        response = "We have a section dedicated to Traditional Dances like Samba and Kathakali. Check the navigation bar!"
    elif 'tourism' in user_message:
        response = "Discover cultural destinations like Kyoto and Machu Picchu in our Tourism section."
    elif 'startup' in user_message:
        response = "Are you an entrepreneur? Visit our Startups Hub to see featured ventures and resources."
    else:
        response = "That's interesting! Feel free to explore our platform to learn more about arts, culture, and innovation."

    return jsonify({'response': response})

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

if __name__ == '__main__':
    app.run(debug=True, port=5001)