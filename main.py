import math
from tkinter import *

cnt: int = 0
timer: None = None

def start() :
    global cnt
    cnt += 1

    if cnt % 8 == 0:
        count_down(20)
        title_label.config(text = "Break")
        cnt = 0
    elif cnt % 2 == 0:
        count_down(5)
        title_label.config(text = "Break")
    else:
        title_label.config(text = "Work")
        count_down(25)
        marks = ''
        tik: int = math.floor(cnt/2)
        for _ in range(tik):
            marks += '✅︎'

        check_mark.config(text = marks)


def reset() :
    global cnt
    global timer
    cnt = 0
    screen.after_cancel(timer)
    canvas.itemconfig(time_text, text='00:00')
    check_mark.config(text = '')
    title_label.config(text = "Timer")



def count_down(count) :
    global timer
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_min < 10: count_min = f'0{count_min}'
    if count_sec < 10: count_sec = f'0{count_sec}'

    canvas.itemconfig(time_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = screen.after(1000, count_down,count - 1)
    else :
        start()



screen = Tk()
screen.title("Pomodoro Technique")
screen.config(padx= 10,pady=10, bg="#E07B39")

title_label = Label(text="Timer", fg="white", bg="#E07B39", font=("Courier", 35, "bold"))
title_label.grid(row=0, column=1, padx=10, pady=10)

canvas = Canvas(width=500, height=500, bg="#E07B39", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(250, 250, image=tomato_img)
time_text = canvas.create_text(260, 280,text="00:00", fill="white" ,font=("Courier", 30, "bold"))
canvas.grid(row=1, column=1, padx=10, pady=10)

start_button = Button(text= "start", bg= "#B83B5E",highlightthickness=0 ,font=("Courier", 15, "bold"), command=start)
start_button.grid(row=2, column=0, sticky="E")

reset_button = Button(text="reset", bg= "#B83B5E", highlightthickness=0 ,font=("Courier", 15, "bold"), command=reset)
reset_button.grid(row=2, column=2,sticky="W")

check_mark = Label(bg="#E07B39", font=("Courier", 25, "bold"))
check_mark.grid(row=2, column=1, padx=5, pady=5)

screen.mainloop()