# MiniProject_Frontend.py
from tkinter import *
from tkinter import messagebox
import MiniProject_Backend

# Initialize the main window
root = Tk()
root.title("Online Movie Ticket Booking System")
root.state("zoomed")   # open maximized
root.configure(bg="black")

# Enable high DPI scaling (for Windows)
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Create the database/table if not exists
MiniProject_Backend.MovieData()

# -----------------------------
# Functions for button actions
# -----------------------------
def AddData():
    if Movie_ID.get() == "" or Movie_Name.get() == "":
        messagebox.showwarning("Input Error", "Please enter Movie ID and Name")
        return
    MiniProject_Backend.AddMovieRec(Movie_ID.get(), Movie_Name.get(), Release_Date.get(),
                                    Director.get(), Cast.get(), Budget.get(),
                                    Duration.get(), Rating.get())
    DisplayData()
    ClearData()
    messagebox.showinfo("Success", "Movie record added successfully!")

def DisplayData():
    movie_list.delete(0, END)
    for row in MiniProject_Backend.ViewMovieData():
        movie_list.insert(END, row)

def SearchData():
    movie_list.delete(0, END)
    for row in MiniProject_Backend.SearchMovieData(Movie_ID.get(), Movie_Name.get(),
                                                   Release_Date.get(), Director.get(),
                                                   Cast.get(), Budget.get(),
                                                   Duration.get(), Rating.get()):
        movie_list.insert(END, row)

def DeleteData():
    try:
        selected = movie_list.curselection()[0]
        data = movie_list.get(selected)
        MiniProject_Backend.DeleteMovieRec(data[0])
        DisplayData()
        ClearData()
        messagebox.showinfo("Deleted", "Movie record deleted successfully!")
    except IndexError:
        messagebox.showwarning("Select Record", "Please select a movie record to delete")

def UpdateData():
    try:
        selected = movie_list.curselection()[0]
        data = movie_list.get(selected)
        # Delete old record first
        MiniProject_Backend.DeleteMovieRec(data[0])
        # Add updated record
        MiniProject_Backend.AddMovieRec(Movie_ID.get(), Movie_Name.get(), Release_Date.get(),
                                        Director.get(), Cast.get(), Budget.get(),
                                        Duration.get(), Rating.get())
        DisplayData()
        ClearData()
        messagebox.showinfo("Updated", "Movie record updated successfully!")
    except IndexError:
        messagebox.showwarning("Select Record", "Please select a movie record to update")

def ClearData():
    Movie_ID.set("")
    Movie_Name.set("")
    Release_Date.set("")
    Director.set("")
    Cast.set("")
    Budget.set("")
    Duration.set("")
    Rating.set("")

def MovieRec(event):
    try:
        global selected_tuple
        index = movie_list.curselection()[0]
        selected_tuple = movie_list.get(index)
        Movie_ID.set(selected_tuple[1])
        Movie_Name.set(selected_tuple[2])
        Release_Date.set(selected_tuple[3])
        Director.set(selected_tuple[4])
        Cast.set(selected_tuple[5])
        Budget.set(selected_tuple[6])
        Duration.set(selected_tuple[7])
        Rating.set(selected_tuple[8])
    except IndexError:
        pass

# -----------------------------
# Variables
# -----------------------------
Movie_ID = StringVar()
Movie_Name = StringVar()
Release_Date = StringVar()
Director = StringVar()
Cast = StringVar()
Budget = StringVar()
Duration = StringVar()
Rating = StringVar()

# -----------------------------
# Layout Design
# -----------------------------
title_label = Label(root, text="ONLINE MOVIE TICKET BOOKING SYSTEM",
                    font=("Arial Black", 28, "bold"), bg="black", fg="orange")
title_label.pack(side=TOP, fill=X, pady=10)

# Frames
MainFrame = Frame(root, bg="black")
MainFrame.pack(fill=BOTH, expand=True, padx=20, pady=20)

LeftFrame = LabelFrame(MainFrame, text="Movie Info", font=("Arial", 14, "bold"),
                       bg="black", fg="orange", bd=3, relief=RIDGE)
LeftFrame.place(x=20, y=20, width=600, height=600)

RightFrame = LabelFrame(MainFrame, text="Movie Details", font=("Arial", 14, "bold"),
                        bg="black", fg="orange", bd=3, relief=RIDGE)
RightFrame.place(x=650, y=20, width=800, height=600)

# Labels and Entry Fields
labels = ["Movie ID:", "Movie Name:", "Release Date:", "Director:",
          "Cast:", "Budget (Crores INR):", "Duration (Hrs):", "Rating (Out of 5):"]
vars = [Movie_ID, Movie_Name, Release_Date, Director,
        Cast, Budget, Duration, Rating]

for i, label_text in enumerate(labels):
    lbl = Label(LeftFrame, text=label_text, font=("Arial", 12, "bold"),
                bg="black", fg="orange")
    lbl.grid(row=i, column=0, sticky=W, pady=10, padx=10)
    ent = Entry(LeftFrame, font=("Arial", 12), textvariable=vars[i], width=25, bg="white")
    ent.grid(row=i, column=1, pady=10, padx=10)

# Listbox & Scrollbar
scroll_y = Scrollbar(RightFrame, orient=VERTICAL)
movie_list = Listbox(RightFrame, font=("Arial", 12), bg="black", fg="orange",
                     yscrollcommand=scroll_y.set, width=90, height=25)
scroll_y.config(command=movie_list.yview)
scroll_y.pack(side=RIGHT, fill=Y)
movie_list.pack(fill=BOTH, expand=True)
movie_list.bind('<<ListboxSelect>>', MovieRec)

# Buttons
ButtonFrame = Frame(root, bg="black")
ButtonFrame.pack(fill=X, pady=10)

btn_style = {"font": ("Arial Black", 12), "bg": "orange", "fg": "black", "width": 12, "height": 1}

Button(ButtonFrame, text="Add New", command=AddData, **btn_style).grid(row=0, column=0, padx=10)
Button(ButtonFrame, text="Display", command=DisplayData, **btn_style).grid(row=0, column=1, padx=10)
Button(ButtonFrame, text="Clear", command=ClearData, **btn_style).grid(row=0, column=2, padx=10)
Button(ButtonFrame, text="Search", command=SearchData, **btn_style).grid(row=0, column=3, padx=10)
Button(ButtonFrame, text="Delete", command=DeleteData, **btn_style).grid(row=0, column=4, padx=10)
Button(ButtonFrame, text="Update", command=UpdateData, **btn_style).grid(row=0, column=5, padx=10)
Button(ButtonFrame, text="Exit", command=root.destroy, **btn_style).grid(row=0, column=6, padx=10)

# Start GUI
root.mainloop()
