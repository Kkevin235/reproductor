import pygame
from tkinter import *
from PIL import Image, ImageTk

class MusicPlayer:
    def __init__(self, window):
        window.geometry('330x490')
        window.title('REPRODUCTOR DE MUSICA')
        window.configure(bg='#121212')

        # crear el marco principal y establecer el color de fondo
        self.frame = Frame(window, bg="#121212")
        self.frame.pack(expand=True, fill=BOTH)

        # cargar la imagen
        image = Image.open("musica.png")
        image = image.resize((320, 320), Image.ANTIALIAS)  # ajustar tamaño de la imagen

        # convertir la imagen en un objeto ImageTk
        self.img = ImageTk.PhotoImage(image)

        # crear el widget Label para mostrar la imagen
        self.image_label = Label(self.frame, image=self.img, bg='#121212')
        self.image_label.grid(row=0, column=0, columnspan=4)

        # crear los botones y establecer el color de fondo activo
        self.play_btn = Button(self.frame, text='▶', bg='#1DB954', fg='#FFFFFF', bd=0, font=('Helvetica', 24), command=self.play_music)
        self.pause_btn = Button(self.frame, text='⏸', bg='#1DB954', fg='#FFFFFF', bd=0, font=('Helvetica', 24), command=self.pause_music)
        self.prev_btn = Button(self.frame, text='⏮', bg='#1DB954', fg='#FFFFFF', bd=0, font=('Helvetica', 24), command=self.prev_music)
        self.next_btn = Button(self.frame, text='⏭', bg='#1DB954', fg='#FFFFFF', bd=0, font=('Helvetica', 24), command=self.next_music)
        self.volume_up_btn = Button(self.frame, text='🔊', bg='#1DB954', fg='#FFFFFF', bd=0, font=('Helvetica', 24), command=self.volume_up)
        self.volume_down_btn = Button(self.frame, text='🔉', bg='#1DB954', fg='#FFFFFF', bd=0, font=('Helvetica', 24), command=self.volume_down)

        # posicionar los botones en la pantalla
        self.prev_btn.grid(row=1, column=0, padx=10, pady=10)
        self.pause_btn.grid(row=1, column=1, padx=10, pady=10)
        self.play_btn.grid(row=1, column=2, padx=10, pady=10)
        self.next_btn.grid(row=1, column=3, padx=10, pady=10)
        self.volume_down_btn.grid(row=2, column=0, padx=10, pady=10)
        self.volume_up_btn.grid(row=2, column=3, padx=10, pady=10)
        # cargar la lista de canciones
        self.song_list = ['cancion 2.mp3', 'phyton.mp3', 'cancion 3.mp3']
        self.current_song_index = 0

        # cargar la canción actual
        pygame.mixer.init()
        self.load_music()

    def volume_up(self):
     current_volume = pygame.mixer.music.get_volume()
     if current_volume < 1.0:
        pygame.mixer.music.set_volume(current_volume + 0.1)

    def volume_down(self):
     current_volume = pygame.mixer.music.get_volume()
     if current_volume > 0.0:
        pygame.mixer.music.set_volume(current_volume - 0.1)


        

    def load_music(self):
        pygame.mixer.music.load(self.song_list[self.current_song_index])

    def play_music(self):
        pygame.mixer.music.play()

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def prev_music(self):
        if self.current_song_index > 0:
            self.current_song_index -= 1
        else:
            self.current_song_index = len(self.song_list) - 1
        self.load_music()
        self.play_music()

    def next_music(self):
        if self.current_song_index < len(self.song_list) - 1:
            self.current_song_index += 1
        else:
            self.current_song_index = 0
        self.load_music()
        self.play_music()

# crear la ventana y ejecutar el programa
window = Tk()
music_player = MusicPlayer(window)
window.mainloop()

