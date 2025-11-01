# frontend_customtk.py
import customtkinter as ctk
from tkinter import messagebox
import MiniProject_Backend

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

MiniProject_Backend.MovieData()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Movie Ticket Booking - Modern")
        self.state("zoomed")
        self.configure(bg_color="#0b0b0b")
        # Left form
        self.grid_columnconfigure(1, weight=1)
        frm_left = ctk.CTkFrame(self, corner_radius=10)
        frm_left.grid(row=0, column=0, padx=20, pady=20, sticky="ns")
        frm_right = ctk.CTkFrame(self, corner_radius=10)
        frm_right.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        # Title
        lbl_title = ctk.CTkLabel(self, text="ONLINE MOVIE TICKET BOOKING", font=ctk.CTkFont(size=26, weight="bold"))
        lbl_title.grid(row=0, column=0, columnspan=2, pady=(10,0))

        # Variables
        self.vars = {k: ctk.StringVar() for k in ["id","name","date","director","cast","budget","duration","rating"]}

        labels = [("Movie ID","id"),("Movie Name","name"),("Release Date","date"),
                  ("Director","director"),("Cast","cast"),("Budget (Cr)","budget"),
                  ("Duration (Hrs)","duration"),("Rating (Out of 5)","rating")]
        for i,(text,key) in enumerate(labels):
            ctk.CTkLabel(frm_left, text=text).grid(row=i, column=0, padx=10, pady=8, sticky="w")
            ctk.CTkEntry(frm_left, textvariable=self.vars[key], width=260).grid(row=i, column=1, padx=10, pady=8)

        # Buttons (styled)
        btns = ctk.CTkFrame(frm_left, fg_color="transparent")
        btns.grid(row=len(labels), column=0, columnspan=2, pady=(15,0))
        actions = [("Add", self.add), ("Display", self.display),
                   ("Search", self.search), ("Update", self.update),
                   ("Delete", self.delete), ("Clear", self.clear)]
        for i,(t,cmd) in enumerate(actions):
            ctk.CTkButton(btns, text=t, command=cmd, width=120).grid(row=0, column=i, padx=6)

        # Right: list / details
        self.listbox = ctk.CTkTextbox(frm_right, width=800, height=560, state="normal")
        self.listbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.listbox.configure(state="disabled")

        # click-to-load: emulate by selecting line number (simple)
        self.display()

    def get_inputs(self):
        return {k:v.get().strip() for k,v in self.vars.items()}

    def add(self):
        d = self.get_inputs()
        if not d["id"] or not d["name"]:
            messagebox.showwarning("Missing", "Provide Movie ID and Name")
            return
        MiniProject_Backend.AddMovieRec(d["id"], d["name"], d["date"], d["director"], d["cast"], d["budget"], d["duration"], d["rating"])
        self.display()
        self.clear()
        messagebox.showinfo("Added", "Movie added.")

    def display(self):
        rows = MiniProject_Backend.ViewMovieData()
        self.listbox.configure(state="normal")
        self.listbox.delete("1.0","end")
        header = f"{'DB_ID':<6} {'M_ID':<12} {'Name':<30} {'Date':<12} {'Director':<12} {'Cast':<18} {'Budget':<8} {'Dur':<4} {'R'}\n"
        self.listbox.insert("end", header + "-"*140 + "\n")
        for r in rows:
            line = f"{r[0]:<6} {r[1]:<12} {r[2]:<30} {r[3]:<12} {r[4]:<12} { (r[5][:15]+'..') if r[5] and len(r[5])>17 else (r[5] or '') :<18} {r[6]:<8} {r[7]:<4} {r[8]}\n"
            self.listbox.insert("end", line)
        self.listbox.configure(state="disabled")

    def search(self):
        d = self.get_inputs()
        rows = MiniProject_Backend.SearchMovieData(d["id"], d["name"], d["date"], d["director"], d["cast"], d["budget"], d["duration"], d["rating"])
        self.listbox.configure(state="normal")
        self.listbox.delete("1.0","end")
        for r in rows:
            self.listbox.insert("end", str(r)+"\n")
        self.listbox.configure(state="disabled")

    def delete(self):
        # ask DB id
        dbid = self.vars["id"].get().strip()
        if not dbid:
            messagebox.showwarning("Delete", "Enter Movie ID (DB id / Movie ID) in Movie ID field to delete")
            return
        # try delete by matching DB numeric id (if numeric) else delete first match by Movie_ID
        try:
            rid = int(dbid)
            MiniProject_Backend.DeleteMovieRec(rid)
        except:
            rows = MiniProject_Backend.SearchMovieData(dbid, dbid, dbid, dbid, dbid, dbid, dbid, dbid)
            if rows:
                MiniProject_Backend.DeleteMovieRec(rows[0][0])
        self.display()
        self.clear()
        messagebox.showinfo("Deleted", "Record deleted if it existed.")

    def update(self):
        # simple update: find DB id by Movie_ID or numeric id then delete and add updated
        dbid = self.vars["id"].get().strip()
        d = self.get_inputs()
        rows = MiniProject_Backend.SearchMovieData(d["id"], "", "", "", "", "", "", "")
        if rows:
            MiniProject_Backend.DeleteMovieRec(rows[0][0])
            MiniProject_Backend.AddMovieRec(d["id"], d["name"], d["date"], d["director"], d["cast"], d["budget"], d["duration"], d["rating"])
            messagebox.showinfo("Updated", "Record updated.")
            self.display()
            self.clear()
        else:
            messagebox.showwarning("Not found", "No record found to update.")

    def clear(self):
        for v in self.vars.values():
            v.set("")

if __name__ == "__main__":
    app = App()
    app.mainloop()
