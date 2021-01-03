from tkinter import *
import pygame
import os

# Play the song
def play_song():
    pygame.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.music.play(0)
    lblSong.config(text = playlist.get(ACTIVE)[:-4])

# Pause the song
def pause_song():
    pygame.mixer.music.pause()

# Resume the song from where it left off when it was paused
def resume_song():
    pygame.mixer.music.unpause()

# Stop the song
def stop_song():
    pygame.mixer.music.stop()

# Increase the volume
def volume_up():
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() +
                                  0.05)

# Decrease the volume
def volume_down():
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() -
                                  0.05)

root = Tk()
root.title('Music Player')
frame = Frame(root, padx=20, pady=20)
frame.pack()

lblSong = Label(frame, width = 20, text = '---', padx = 5, font='TkDefaultFont 20 bold')
lblSong.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

btnPlay = Button(frame, width=10, text='PLAY', command=play_song)
btnPlay.grid(row=1, column=0, padx=5)

btnPause = Button(frame, width=10, text='PAUSE', command=pause_song)
btnPause.grid(row=1, column=1, padx=5)

btnResume = Button(frame, width=10, text='RESUME', command=resume_song)
btnResume.grid(row=1, column=2, padx=5)

btnStop = Button(frame, width=10, text='STOP', command=stop_song)
btnStop.grid(row=1, column=3, padx=5)

btnVolUp = Button(frame, width=10, text='\u21d1', command=volume_up)
btnVolUp.grid(row=2, column=0, padx=5, pady=10)

btnVolDown = Button(frame, width=10, text='\u21d3', command=volume_down)
btnVolDown.grid(row=2, column=3, padx=5, pady=10)

lblVolume = Label(frame, text='VOLUME CONTROL', padx=5, font='TkDefaultFont 10 bold', relief='solid', borderwidth=1, width=18)
lblVolume.grid(row=2, column=1, columnspan=2, padx=5, pady=10, ipady=4, ipadx=5)

#create song playlist
songsframe = LabelFrame(root, text = 'Songs', padx = 20, pady = 20, bd=5, relief=GROOVE)
songsframe.pack(fill = BOTH)
scrolly = Scrollbar(songsframe, orient = VERTICAL)

playlist = Listbox(songsframe, selectmode = SINGLE, bd=5, relief=GROOVE)

scrolly.pack(side = RIGHT, fill = Y)
scrolly.config(command = playlist.yview)
playlist.pack(fill = BOTH)

#find song directory and insert into playlist
os.chdir('PATH DIRECTORY HERE')
songtracks = os.listdir()

for x in songtracks:
    playlist.insert(END, x)

# Initialize and load the music file
pygame.mixer.init()
root.mainloop()
