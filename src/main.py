from artist import Artist

def main():
    print("Welcome to the Arts and Talents Promotion Platform!")
    print("--------------------------------------------------")

    # Create a sample artist
    sample_artist = Artist("John Doe", "Painter", "New York")

    # Add some pieces to the portfolio
    sample_artist.add_to_portfolio("Starry Night Rework")
    sample_artist.add_to_portfolio("Abstract Cityscape")

    # Display the artist's profile
    sample_artist.display_profile()

    print("\nThis is a simple demonstration of the artist profile feature.")
    print("More features coming soon!")


if __name__ == "__main__":
    main()