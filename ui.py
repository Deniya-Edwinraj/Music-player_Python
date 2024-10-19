import tkinter as tk
from tkinter import filedialog
from ttkthemes import ThemedTk  
from tkinter import ttk 
from player import MusicPlayer

class MusicPlayerApp:
    def __init__(self):
        self.root = ThemedTk(theme="breeze")
        self.player = MusicPlayer()
        self.root.title("Music Player")
        self.root.geometry("400x300")  
        
        self.root.config(bg='#282a36') 
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10, background='#bd93f9')

        self.load_button = ttk.Button(self.root, text="Load Song", command=self.load_song, style="TButton")
        self.load_button.pack(pady=10)

        self.play_button = ttk.Button(self.root, text="Play", command=self.play_song, style="TButton")
        self.play_button.pack(pady=10)

        self.pause_button = ttk.Button(self.root, text="Pause", command=self.pause_song, style="TButton")
        self.pause_button.pack(pady=10)

        self.unpause_button = ttk.Button(self.root, text="Unpause", command=self.unpause_song, style="TButton")
        self.unpause_button.pack(pady=10)

        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_song, style="TButton")
        self.stop_button.pack(pady=10)

    def load_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if song_path:
            self.player.load_song(song_path)

    def play_song(self):
        self.player.play()

    def pause_song(self):
        self.player.pause()

    def unpause_song(self):
        self.player.unpause()

    def stop_song(self):
        self.player.stop()

    def run(self):
        self.root.mainloop()
