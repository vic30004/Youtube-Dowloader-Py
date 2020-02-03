from tkinter import Tk, Button, Label, StringVar, Entry
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from pytube import YouTube

# This is the interface
root = Tk()
root.title('Youtube Downloader')
root.configure(background="#333")
root.minsize(width=420, height=100)

# Main Functions


def open_file():
    global directory
    directory = askdirectory()
    print(directory)

def download():
    if len(link.get()) == 0:
        messagebox.showerror("Link Empty", "Link can not be empty")
    else:
        YouTube(link.get()).streams.first().download(directory)
        messagebox.showinfo("Complete", "Video downloaded successfully")
        link_entry.delete(0, 'end')


# this wont let user change the size of the widget
root.resizable(width=False, height=False)

# Link Label
link_lbl = Label(root, text="Enter Link",
                 font="Helvetica 12 bold").grid(row=1, column=0)
# Link Input
link = StringVar()
link_entry = Entry(root, textvariable=link, width=50,
                   borderwidth=4).grid(row=1, column=1)

# Select directory Buton
select_dir = Button(root, text="Choose Directory", bg="#DC143C", font="Helvetica 10 bold", width=15,
                    command=open_file).grid(row=1, column=2)

# Download Button
download_btn = Button(root, text="Download", bg="light green", font="Helvetica 10 bold", width=10,
                      command=download).grid(row=2, column=1)

root.mainloop()
