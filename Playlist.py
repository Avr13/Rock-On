from tkinter import *
from tkinter import filedialog
import pyglet
import os
j=0
Location= r'C:' #Insert directory location of Music player folder

root = Tk()
root.title("M. Player")
root.geometry("200x600")

top_frame = Frame(root, width=200, height=350, bg="lightblue")
top_frame.pack(side=TOP)
bottom_frame = Frame(root, width=200, height=50, bg="lightgreen")
bottom_frame.pack(side=BOTTOM)
tmiddle_frame=Frame(root, width=200, height=20, bg="yellow")
tmiddle_frame.pack(side=TOP)
middle_frame = Frame(root, width=200, height=180, bg="white")
middle_frame.pack(side=TOP)

pl=[]  #stack

def browse_file():
    global filepath
    filepath = filedialog.askopenfilename(initialdir=Location+r'\Music player')
    if (filepath != ''):
        pl.insert(0, filepath)  # push
    global j
    j = 0
    for widgets in middle_frame.winfo_children(): widgets.destroy()
    if (len(pl) != 0):
        for i in range(len(pl)):
            txt = Label(middle_frame, text=os.path.splitext(os.path.basename(pl[i]))[0])
            txt.pack()


def play_song():
    global player, j, txt
    if (j >= 0 and j < (len(pl))):
        player = pyglet.media.Player()
        src = pyglet.media.load(pl[j])
        player.queue(src)
        player.play()
        cs = Label(root, text=os.path.splitext(os.path.basename(pl[j]))[0])
        cs.place(x=0, y=300)
        j = j + 1
    if (j == (len(pl))):
        j = 0


def stop_music():
    if (len(pl) != 0): player.pause()


def resume_music():
    if (len(pl) != 0): player.play()


playlist = Label(tmiddle_frame, text="----- PLAYLIST -----")
playlist.pack()

img_play = PhotoImage(file=Location+r'\Music player\Icons\Play.png')
button_play = Button(bottom_frame, image=img_play, command=play_song)
button_play.place(x=20, y=8)

img_stop = PhotoImage(file=Location+r'\Music player\Icons\Stop.png')
button_stop = Button(bottom_frame, image=img_stop, command=stop_music)
button_stop.place(x=80, y=8)

img_resume = PhotoImage(file=Location+r'\Music player\Icons\Pause.png')
button_resume = Button(bottom_frame, image=img_resume, command=resume_music)
button_resume.place(x=140, y=8)

img = PhotoImage(file=Location+r'\Music player\Icons\Me.gif')
button_add_song = Button(top_frame, command=browse_file, image=img)
button_add_song.pack()
root.resizable(False, False)

root.mainloop()