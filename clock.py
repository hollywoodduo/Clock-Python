import tkinter
import time

currentTime = ''
clock = tkinter.Label()
clock.pack()


def tick():

    global currentTime # Set 24 hour standard
    newtime = time.strftime('%H:%M:%S')
    if newtime != currentTime:
        currentTime = newtime
        clock.config(text=currentTime)
    clock.after(200, tick)


tick()
clock.mainloop()
