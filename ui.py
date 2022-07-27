from pymsgbox import *
import tkinter
from tkinter import *
from tkinter import ttk as tk
import gc



gc.disable()
def init():
    global root, frame,kat, p, img, image, let
    frame = tkinter.Tk()
    frame.attributes("-fullscreen", True)
    root = Frame(frame)
    root.place(relx=0.5,rely=0.5,anchor=CENTER)
    kat = tk.Label(root,text="...",font=("Calibri",20))
    let = tk.Label(root,text="...",font=("Calibri",30))
    p = tk.Label(root,text="C z e _ a m y  n _  h _ s _ o ...",font=("Calibri",40))
    img = PhotoImage(file='assets/hangman/0.png')
    image = Label(
        root,
        image=img
    )
    image.pack()
    kat.pack()
    
    p.pack()
    let.pack()
def updateDisplay(var,error,cat,incorrect):
    global p,kat, img,image, let
    let["text"] = incorrect
    kat["text"] = ("Kategoria: "+cat)
    p["text"] = var
    img = PhotoImage(file=f'assets/hangman/{error}.png')
    image["image"] = img
    root.update()
def getWord():
    return password(text='Podaj słowo', title='Hangboi', mask='*')
def getCategory():
    return prompt(text='Podaj kategorie', title='Hangboi')
def getLetter(errs):
    i = prompt(text='Litera', title='Hangboi').lower()
    while i in errs:
        i = prompt(text='Litera (nie powtórzona)', title='Hangboi').lower()
    return i
    
def lost(word):
    alert(text='Gra zakończona, przegraliście.\nSłowo: '+word, title='Hangboi', button='Smutek :(') 
    raise SystemExit
def win(word,error):
    alert(text='Udało sie, wygraliście!\nSłowo: '+word+"\nIlośc błędów:"+str(error), title='Hangboi', button='Yay :)')
    raise SystemExit
def cheatDetect(word):
    import moviepy.editor
    import pygame
    import os
    global frame
    os.system("amixer -D pulse sset Master 100%")
    frame.destroy()
    clip = moviepy.editor.VideoFileClip('assets/cheaters/dox.mp4').resize((1920,1080))
    clip.preview(fullscreen=True)
    alert("Pamiętaj, oszukiwanie w ten sposób nigdy nie jest ok. Wygrali zgadujący.\nSłowo: "+word,title="OSZUST!!!!!",button="OK.")
    pygame.quit()
    raise SystemExit
