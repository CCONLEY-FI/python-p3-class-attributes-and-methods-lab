# Song Class Initialization**    
    #Initialize with `name`, `artist`, and `genre`.
        #Example: `ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")`.
    #Class Attribute: `count`
        #Initialize `count` to 0.
        #Increment `count` for each new song via `add_song_to_count()` class method.

#Class Methods
    #add_to_genres()`
        #Adds unique genres to a class attribute `genres` list.
        #Update `genres` in `__init__` method for every new song.
    #add_to_artists()`
        #Adds unique artists to a class attribute `artists` list.
        #Update `artists` in `__init__` method for every new song.
    #add_to_genre_count()`
        #Creates a histogram `genre_count` dictionary with genres as keys and song counts as values.
    #add_to_artist_count()`
        #Creates a histogram `artist_count` dictionary with artists as keys and song counts as values.
#Histograms
    #Maintain numerical data (`genre_count` and `artist_count`) showing how many songs belong to each genre and artist.
    
class Song:
    # these are class attributes
    count = 0
    genres = []
    artists = []
    all = []
    genre_count = {}
    artist_count = {}


    # __init__ method to initialize the Song class with name, artist, and genre.
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_to_genres()
        self.add_to_artists()
        Song.add_song_to_count()
        Song.all.append(self)

    # add_song_to_count() method to the Song class. This method should increment the class attribute count by 1.
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    # add_to_genres() method to the Song class. This method should take in a genre and add it to the class attribute genres if it is not already there. It should then call the add_to_genre_count() method.
    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)
        Song.add_to_genre_count(self.genre)
    
    # add_to_artists() method to the Song class. This method should take in an artist and add it to the class attribute artists if it is not already there. It should then call the add_to_artist_count() method.        
    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)
        Song.add_to_artist_count(self.artist)


    # add_to_genre_count() method to the Song class. This method should take in a genre and increment the class attribute genre_count.
    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1


    # add_to_artist_count() method to the Song class. This method should take in an artist and increment the class attribute artist_count.
    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
