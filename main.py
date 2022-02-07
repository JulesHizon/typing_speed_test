import tkinter as tk 
import time
from threading import Thread

root = tk.Tk()
root.title("Typing Speed Test")
root.minsize(width=700, height=400)

text_one = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
game_started = True
seconds = 0

def start_game(event):
    global game_started
    if game_started:
        t1 = Thread(target=display_wpm)
        t1.start()
        game_started = False

def display_wpm():
    global seconds
    game_running = True
    while game_running:
        seconds += 1
        wpm_label.config(text=f"WPM: {(len(text_one)/(seconds/60)):.1f}")
        if text_input.get() == text_one:
            game_running = False
        time.sleep(0.1)
        

def reset_game():
    game_running = False
    wpm_label.config(text="WPM: 0")

reset_btn = tk.Button(text="Reset", command=reset_game)
wpm_label = tk.Label(text="WPM: 0", font=("Roboto", 18))
text_to_write = tk.Label(text=text_one, wraplength=600, justify="left", font=("Roboto", 18))
text_input = tk.Entry(width=50, font=("Roboto", 18))

text_to_write.grid(row=1, column=0, columnspan=2, padx=25, pady=50)
text_input.grid(row=2, column=0, columnspan=2, padx=25, ipady=5)
reset_btn.grid(row=3, column=0, pady=50)
wpm_label.grid(row=3, column=1, pady=50)

text_input.bind("<KeyRelease>", start_game)

root.mainloop()