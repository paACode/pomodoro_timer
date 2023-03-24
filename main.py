import math
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
working_phase = 0
check_mark_text = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global working_phase
    global check_mark_text
    window.after_cancel(timer)
    countdown(WORK_MIN * 60)
    timer_label.config(text="Work", fg=GREEN)
    window.after_cancel(timer)
    check_mark_text = ""
    checkMark_label.config(text=check_mark_text)
    working_phase = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global working_phase
    global check_mark_text

    if working_phase == 8:
        reset()
        working_phase = -1
    elif working_phase % 2 == 0:
        countdown(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
    else:
        if working_phase == 7:
            countdown(LONG_BREAK_MIN * 60)
            timer_label.config(text="Break", fg=PINK)
        else:
            countdown(SHORT_BREAK_MIN * 60)
            timer_label.config(text="Break", fg=PINK)
        check_mark_text += "✓"
        checkMark_label.config(text=check_mark_text)
    working_phase += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(seconds):
    global timer
    text_minutes = int(math.floor(seconds / 60))
    text_seconds = int(seconds % 60)
    canvas.itemconfig(timer_text, text=f"{text_minutes:02d}:{text_seconds:02d}")
    if seconds > 0:
        timer = window.after(1000, countdown, seconds - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

checkMark_label = tkinter.Label(text=check_mark_text, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkMark_label.grid(column=1, row=3)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.config(width=10)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", command=reset)
reset_button.config(width=10)
reset_button.grid(column=2, row=2)

tkinter.mainloop()
