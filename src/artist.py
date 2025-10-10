class Artist:
    def __init__(self, name, genre, location):
        self.name = name
        self.genre = genre
        self.location = location
        self.portfolio = []

    def add_to_portfolio(self, piece):
        self.portfolio.append(piece)

    def display_profile(self):
        print(f"Name: {self.name}")
        print(f"Genre: {self.genre}")
        print(f"Location: {self.location}")
        print("Portfolio:")
        if self.portfolio:
            for piece in self.portfolio:
                print(f"- {piece}")
        else:
            print("- No pieces in portfolio yet.")