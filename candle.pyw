import tkinter as tk

root = tk.Tk()
gif_count = 121

frames = [tk.PhotoImage(file='c:\\Programme\\candle\\light.gif', format='gif -index %i' % i) for i in range(gif_count)]
label = tk.Label(root, borderwidth=0, highlightthickness=0, bg="black")

lastClickX = 0
lastClickY = 0


def save_last_click_pos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x, y))


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind > gif_count - 1:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)


label.pack()
root.overrideredirect(True)
root.geometry("-3730-0")
root.lift()
root.wm_attributes("-topmost", True)
root.wm_attributes('-transparentcolor', 'black')
root.bind('<Button-1>', save_last_click_pos)
root.bind('<B1-Motion>', dragging)
root.after(0, update, 0)
root.mainloop()
