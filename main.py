from tkinter import *
import time
from schedule import every, repeat, run_pending

# from tkinter import Canvas
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 1
timer = ""


# ------------------------------ Convert Seconds to HH:MM format----------------#
def convert_hhmm(seconds):
    minute = str(seconds // 60)
    if len(minute) < 2:
        minute = '0' + minute
    second = str(seconds % 60)
    if len(second) < 2:
        second = '0' + second
    return f"{minute}:{second}"


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    global reps
    reps = 1
    subject.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps % 2 > 0:
        count_down(WORK_MIN)
    elif reps == 8:
        count_down(LONG_BREAK_MIN)
    else:
        count_down(SHORT_BREAK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps

    hhmm = convert_hhmm(count)

    canvas.itemconfig(timer_text, text=hhmm)
    if count > 0:
        global timer
        timer = window.after(5, count_down, count - 1)
    else:
        reps += 1
        if reps % 8 == 0:
            count = LONG_BREAK_MIN
            subject_text = "Break"
            color = RED
        elif reps % 2 > 0:
            count = WORK_MIN
            subject_text = "Work"
            color = GREEN
        else:
            count = SHORT_BREAK_MIN
            subject_text = "Break"
            color = PINK
        hhmm = convert_hhmm(count)
        canvas.itemconfig(timer_text, text=hhmm)
        subject.config(text=subject_text, fg=color)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

# count_down(5)

start_button = Button(text="START", command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="RESET", command=reset)
reset_button.grid(column=2, row=3)

subject = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'bold'))
subject.grid(column=1, row=0)

check_mark = Label(text="✓", bg=YELLOW, font=(FONT_NAME, 20, 'bold'), fg=GREEN)
check_mark.grid(column=1, row=3)

# comment
print('Hello')
window.mainloop()
