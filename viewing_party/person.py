class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.watchlist = []
        self.movies_watched = []

    def add_friend(self, new_friend):
        if new_friend not in self.friends:
            self.friends.append(new_friend)
    
    def add_to_watchlist(self, new_movie):
        if new_movie not in self.watchlist:
            self.watchlist.append(new_movie)
    
    def add_movie_to_watched(self, movie):
        if movie not in self.movies_watched:
            self.movies_watched.append(movie)
        
        if movie in self.watchlist:
            self.watchlist.remove(movie)