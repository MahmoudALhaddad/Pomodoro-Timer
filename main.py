from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
which_turn = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_pomodoro():
    window.after_cancel(timer)
    global which_turn
    which_turn = 0
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_emoji.config(text="")
    start_button.config(state=NORMAL)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_pomodoro():
    global which_turn
    which_turn = which_turn + 1
    start_button.config(state=DISABLED)
    if which_turn % 2 == 1:
        count_down(WORK_MIN * 60)
        timer_label.config(text="WORK", fg=RED)
    elif which_turn % 2 == 0 and which_turn != 8:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=PINK)
    elif which_turn == 8:
        timer_label.config(text="BREAK", fg=PINK)
        count_down(LONG_BREAK_MIN * 60)
        which_turn = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_pomodoro()
        mark = ""
        work_sessions = math.floor(which_turn / 2)
        for i in range(work_sessions):
            mark += "✔"
        check_emoji.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=("Arial", 20, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=("Arial", 24, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_pomodoro)
start_button.grid(row=2, column=0)

reset_button = Button(text="reset", highlightthickness=0, command=reset_pomodoro)
reset_button.grid(row=2, column=2)

check_emoji = Label(fg=GREEN, bg=YELLOW, font=("Arial", 17, "bold"))
check_emoji.grid(row=3, column=1)

window.mainloop()
