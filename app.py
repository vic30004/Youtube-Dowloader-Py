from tkinter import Tk(), Button, Lable, StringVar, Entry
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from tkinter import YouTube

# This is the interface 
root = Tk()
root.title('Youtube Downloader')
root.configure(background="#333")
root.minsize(width=420, height=100)
root.resizable(width=False, height=False) #this wont let user change the size of the widget 
