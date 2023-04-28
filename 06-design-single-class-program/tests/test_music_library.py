import pytest
from lib.music_library import *

"""
Initially tells the user that
there are no tracks in this list
When no tracks have been added yet
"""
def test_returns_statement_when_no_tracks_given():
    test_tracks = MusicLibrary()
    assert test_tracks.show_music_tracks() == "You have not added any tracks."

"""
Given a empty string as a track
#add_music_track raises an error
"""
def test_raises_error_when_empty_string_track_given():
    test_tracks = MusicLibrary()
    with pytest.raises(Exception) as err:
        test_tracks.add_music_track("") 
    error_message = str(err.value)
    assert error_message == "You have not set a track."

"""
Given a track
#show_music_tracks displays a list containing the track
"""
def test_given_one_track_returns_list_with_one_track():
    test_tracks = MusicLibrary()
    test_tracks.add_music_track("This Is the Best Burrito I've Ever Eaten")
    assert test_tracks.show_music_tracks() == "Songs You've Listened To: This Is the Best Burrito I've Ever Eaten"

"""
Given two tracks
#show_music_tracks displays a list of both tracks
"""
def test_given_two_tracks_returns_list_with_two_tracks():
    test_tracks = MusicLibrary()
    test_tracks.add_music_track("This Is the Best Burrito I've Ever Eaten")
    test_tracks.add_music_track("Crab Rave")
    assert test_tracks.show_music_tracks() == "Songs You've Listened To: This Is the Best Burrito I've Ever Eaten, Crab Rave"