from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 7
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECONDS_IN_MIN = 1
REP_SEQUENCE = {
    1: WORK_MIN,
    2: SHORT_BREAK_MIN,
    3: WORK_MIN,
    4: SHORT_BREAK_MIN,
    5: WORK_MIN,
    6: SHORT_BREAK_MIN,
    7: WORK_MIN,
    8: LONG_BREAK_MIN
}

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, timer
    reps = 0
    window.after_cancel(timer)
    label_title.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"{WORK_MIN}:00")
    label_checks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    minutes = REP_SEQUENCE[reps]

    if reps in (1, 3, 5, 7):
        label_title.config(text="Work")
    else:
        # checkkmark
        if reps == 2:
            label_checks.config(text="✅")
        if reps == 4:
            label_checks.config(text="✅✅")
        if reps == 6:
            label_checks.config(text="✅✅✅")
        if reps == 8:
            label_checks.config(text="✅✅✅✅")

        label_title.config(text="Break")

    count_down(minutes * SECONDS_IN_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes_left = int(count / 60)
    seconds_left = count % 60
    time_left = f"{minutes_left}:{seconds_left:02d}"
    canvas.itemconfig(timer_text, text=time_left)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text=f"{WORK_MIN}:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_title = Label()
label_title.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, "bold"))
label_title.grid(column=1, row=0)

button_start = Button()
button_start.config(text="Start", command=start_timer, bg=YELLOW, highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button()
button_reset.config(text="Reset", command=reset, bg=YELLOW, highlightthickness=0)
button_reset.grid(column=2, row=2)

label_checks = Label()
label_checks.config(text="", fg=GREEN)
label_checks.grid(column=1, row=3)

window.mainloop()
