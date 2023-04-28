# Music Library Class Design Recipe

## 1. Describe the Problem

> As a user  
> So that I can keep track of my music listening  
> I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class MusicLibrary():
    def __init__(self):
        # Parameters:
        #   none
        # States:
        #   music_list: an empty list
        # Side effects:
        #   none
        pass # No code here yet

    def add_music_track(self, track):
        # Parameters:
        #   track: string
        # Side effects:
        #   Appends the #track string to the #self.music_list list
        #   Throws an error if no track is set
        pass # No code here yet

    def show_music_tracks(self):
        # Parameters:
        #   none
        # Side effects:
        #   none
        pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Initially tells the user that
there are no tracks in this list
When no tracks have been added yet
"""
test_tracks = MusicLibrary()
test_tracks.show_music_tracks() => "You have not added any tracks."

"""
Given a empty string as a track
#add_music_track raises an error
"""
test_tracks = MusicLibrary()
test_tracks.add_music_track("") # raises an error with the message
"You have not set a track."

"""
Given a track
#show_music_tracks displays a list containing the track
"""
test_tracks = MusicLibrary()
test_tracks.add_music_track("This Is the Best Burrito I've Ever Eaten")
test_tracks.show_music_tracks() => "Songs You've Listened To: This Is the Best Burrito I've Ever Eaten"

"""
Given two tracks
#show_music_tracks displays a list of both tracks
"""
test_tracks = MusicLibrary()
test_tracks.add_music_track("This Is the Best Burrito I've Ever Eaten")
test_tracks.add_music_track("Crab Rave")
test_tracks.show_music_tracks() => "Songs You've Listened To: This Is the Best Burrito I've Ever Eaten, Crab Rave"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
