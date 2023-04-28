class MusicLibrary():
    def __init__(self):
        self._music_list = []

    def add_music_track(self, track):
        if track == "":
            raise Exception("You have not set a track.")
        else:
            self._music_list.append(track)
    
    def show_music_tracks(self):
        if self._music_list == []:
            return "You have not added any tracks."
        else:
            tracks_string = ", ".join(self._music_list)
            return f"Songs You've Listened To: {tracks_string}"