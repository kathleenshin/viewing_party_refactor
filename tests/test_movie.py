from viewing_party.movie import Movie
import pytest

def test_create_movie():
    # Arrange/Act
    jaws_movie = Movie("Jaws", "Thriller", 4)

    # Assert
    assert jaws_movie.movie_name == "Jaws"
    assert jaws_movie.genre == "Thriller"
    assert jaws_movie.rating == 4