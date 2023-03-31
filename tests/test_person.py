from viewing_party.person import Person


import pytest

def test_creating_person_initializes_instance_variables():
    # Arrange / Act
    kendall = Person("Kendall")

    # Assert
    assert kendall.name == "Kendall"
    assert kendall.friends == []

def test_adding_friend_multiple_times_does_not_create_duplicate():
    # Arrange
    kendall = Person("Kendall")
    simon = Person("Simon")

    # Act
    kendall.add_friend(simon)
    kendall.add_friend(simon)

    # Assert
    assert kendall.friends == [simon]

def test_add_new_movie_to_watchlist():
    #Arrange
    ana = Person("Ana")
    movie = "Mean Girls"

    #Act 
    ana.add_to_watchlist(movie)

    #Assert 
    assert movie in ana.watchlist 

def test_add_movie_to_watched():
    # Arrange
    kathleen = Person("Kathleen")
    movie = "Star Wars"

    # Act
    kathleen.add_movie_to_watched(movie)

    # Assert
    assert movie in kathleen.movies_watched

