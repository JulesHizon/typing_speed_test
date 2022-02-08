import tkinter as tk 
import time
from threading import Thread
import random

root = tk.Tk()
root.title("Typing Speed Test")
root.minsize(width=700, height=400)

texts = ["It must be five o'clock somewhere.",
         "He was sitting in a trash can with high street class.",
         "It was a slippery slope and he was willing to slide all the way to the deepest depths.",
         "All you need to do is pick up the pen and begin.",
         "We have never been to Asia, nor have we visited Africa."]

game_started = True
seconds = 0
text_choice = random.choice(texts)

def start_game(*args):
    global game_started

    if game_started:
        t1 = Thread(target=display_wpm)
        t1.start()
        game_started = False

def display_wpm():
    global seconds
    game_running = True
    while game_running:
        seconds += 0.1
        wpm_label.config(text=f"WPM: {(len(text_choice.split(' '))/(seconds/60)):.1f}")
        if not text_choice.startswith(text_input.get()):
            text_input.config(foreground='red')
        else: text_input.config(foreground='green')
        if text_input.get() == text_choice:
            game_running = False
        time.sleep(0.1)
        
def reset_game():
    global game_started
    global seconds
    global text_choice
    seconds = 0
    game_started = True
    text_input.delete(0, 'end')
    wpm_label.config(text="WPM: 0")
    text_choice = random.choice(texts)
    text_to_write.config(text=text_choice)
    text_input.bind("<KeyRelease>", start_game)


reset_btn = tk.Button(text="Reset", command=reset_game)
wpm_label = tk.Label(text="WPM: 0", font=("Roboto", 18))
text_to_write = tk.Label(text=text_choice, wraplength=600, justify="left", font=("Roboto", 18))
text_input = tk.Entry(width=50, font=("Roboto", 18))

text_to_write.grid(row=1, column=0, columnspan=2, padx=25, pady=50)
text_input.grid(row=2, column=0, columnspan=2, padx=25, ipady=5)
reset_btn.grid(row=3, column=0, pady=50)
wpm_label.grid(row=3, column=1, pady=50)

text_input.bind("<KeyRelease>", start_game)

root.mainloop()