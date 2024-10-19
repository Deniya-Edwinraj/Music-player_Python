import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.current_song = None

    def load_song(self, song_path):
        if os.path.exists(song_path):
            self.current_song = song_path
            pygame.mixer.music.load(song_path)

    def play(self):
        if self.current_song:
            pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()
