# convert uml diagram into python class and methods
 # Create a music player web app using oops with the following features.
    # 1.Users can create audio using URLs available online.
    # 2.Users can create multiple Playlists based on the genre of the song.
    # 3.Users can add multiple audio files into each playlist created.
    # 4.Users can search audio by name.
    # 5.Users can search the playlist by name.
    # 6.Users can give ratings to playlist and audio. Rating displayed is the average rating calculated after each submission.
    # 7.For displaying Average rating:
    #   i.Create 3 users and randomly generate ratings from 1 to 5.
    #   ii.find the average rating from the random number generated and display it in the front end.
    # 8.Audio player customization feature will fetch additional points.


import random

class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.rating = 0

    def rate(self, user, rating):
        # Assume user is an instance of the User class
        self.rating = (self.rating + rating) / 2

class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audios = []
        self.rating = 0

    def add_audio(self, audio):
        # Assume audio is an instance of the Audio class
        self.audios.append(audio)

    def rate(self, user, rating):
        # Assume user is an instance of the User class
        self.rating = (self.rating + rating) / 2

class User:
    def __init__(self, username):
        self.username = username

class MusicPlayer:
    def __init__(self):
        self.users = []
        self.audios = []
        self.playlists = []

    def create_user(self, username):
        user = User(username)
        self.users.append(user)
        return user

    def create_audio(self, name, url):
        audio = Audio(name, url)
        self.audios.append(audio)
        return audio

    def create_playlist(self, name, genre):
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist

# Example usage:
music_player = MusicPlayer()

# Creating users
user1 = music_player.create_user("User1")
user2 = music_player.create_user("User2")
user3 = music_player.create_user("User3")

# Creating audio files
audio1 = music_player.create_audio("Song1", "https://example.com/song1.mp3")
audio2 = music_player.create_audio("Song2", "https://example.com/song2.mp3")
audio3 = music_player.create_audio("Song3", "https://example.com/song3.mp3")

# Creating playlists
playlist1 = music_player.create_playlist("Playlist1", "Rock")
playlist2 = music_player.create_playlist("Playlist2", "Pop")

# Adding audio files to playlists
playlist1.add_audio(audio1)
playlist1.add_audio(audio2)
playlist2.add_audio(audio3)

# Rating audio files and playlists
audio1.rate(user1, random.randint(1, 5))
audio2.rate(user2, random.randint(1, 5))
playlist1.rate(user3, random.randint(1, 5))
playlist2.rate(user1, random.randint(1, 5))

# Displaying average ratings (for frontend implementation)
print("Average Rating for Playlist1:", playlist1.rating)
print("Average Rating for Audio1:", audio1.rating)
