from tkinter import Tk, Button, Label, StringVar, Entry
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from pytube import YouTube

# This is the interface
root = Tk()
root.title('Youtube Downloader')
root.configure(background="#333")
root.minsize(width=420, height=100)
# this wont let user change the size of the widget
root.resizable(width=False, height=False)

link_lbl = Label(root, text="Enter Link",
                 font="Helvetica 12 bold").grid(row=1, column=0)

link = StringVar()
link_entry = Entry(root, textvariable=link, width=50,
                   borderwidth=4).grid(row=1, column=1)

select_dir = Button(root, text="Choose Directory", bg="#DC143C", font="Helvetica 10 bold", width=15,
                    command='').grid(row=1, column=2)

download_btn = Button(root, text="Download", bg="light green",font="Helvetica 10 bold", width=10,
                      command='').grid(row=2, column=1)

root.mainloop()
