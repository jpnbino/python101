import tkinter as tk

window = tk.Tk()


label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)

label.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
)

button.pack()

entry = tk.Entry(width=25)

entry.pack()

name = entry.get()

label = tk.Label (text=name)
text_box = tk.Text()
text_box.pack()

window.mainloop()