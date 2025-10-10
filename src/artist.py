class Artist:
    def __init__(self, name, genre, location, profile_pic=None, video=None, audio=None):
        self.name = name
        self.genre = genre
        self.location = location
        self.profile_pic = profile_pic
        self.video = video
        self.audio = audio
        self.portfolio = []

    def add_to_portfolio(self, piece):
        self.portfolio.append(piece)

    def display_profile(self):
        print(f"Name: {self.name}")
        print(f"Genre: {self.genre}")
        print(f"Location: {self.location}")
        print(f"Profile Picture: {self.profile_pic}")
        print(f"Video: {self.video}")
        print(f"Audio: {self.audio}")
        print("Portfolio:")
        if self.portfolio:
            for piece in self.portfolio:
                print(f"- {piece}")
        else:
            print("- No pieces in portfolio yet.")