import tkinter as tk
from tkinter import ttk

main_window = tk.Tk()
main_window.title("Placing elements in Tk")

label1 = tk.Label(text="Hello, world!", bg="#FF1493")
label1.grid(row=0, column=0, sticky="nsew")

label2 = tk.Label(text="Hello, world!", bg="#00CC99")
label2.grid(row=1, column=0, sticky="nsew")

entry = ttk.Entry()
entry.grid(row=1, column=1)

button = ttk.Button(text="Press here")
button.grid(row=0, column=1)

main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=1)
main_window.mainloop()
