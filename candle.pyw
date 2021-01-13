import tkinter as tk

root = tk.Tk()
# The image must be stored to Tk or it will be garbage collected.
gif_count = 121

frames = [tk.PhotoImage(file='c:\\Programme\\candle\\light.gif', format='gif -index %i' % i) for i in range(gif_count)]
label = tk.Label(root, borderwidth=0, highlightthickness=0, bg='green')


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
root.wm_attributes("-disabled", True)
root.wm_attributes("-alpha", 0.7)
root.wm_attributes("-transparentcolor", "green")
root.after(0, update, 0)
root.mainloop()
