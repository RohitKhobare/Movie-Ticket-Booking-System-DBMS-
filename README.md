
# 🎬 Movie Ticket Booking System (DBMS Mini Project)

A complete **Database Management System (DBMS)** mini-project for managing online movie ticket bookings.  
Built using **Python (Tkinter / CustomTkinter)** for the frontend and **MySQL** for the backend.

---

## 📁 Project Structure

```
DBMS-Movie-Ticket-Booking-System/
│
├── backend.py                 # Handles all database operations (insert, delete, update, fetch)
├── frontend_customtk.py       # Modern CustomTkinter GUI (modern, responsive interface)
├── frontend_tkinter.py        # Classic Tkinter version (basic interface)
├── database.sql               # SQL script to create necessary tables
├── requirements.txt           # Python dependencies list
└── README.md                  # Project documentation (you are here)
```

---

## ⚙️ Software Requirements

| Component | Recommended Version |
|------------|--------------------|
| Python     | 3.10 or above |
| MySQL      | 8.0+ |
| pip        | Latest |
| Tkinter / CustomTkinter | Latest |
| VS Code / PyCharm | Optional (for editing) |

---

## 🧩 Required Python Libraries

Run the following commands to install all required modules:

```bash
pip install mysql-connector-python
pip install customtkinter
pip install pillow
```

---

## 🏗️ Database Setup (MySQL)

1. Open **MySQL Workbench** or **phpMyAdmin**.
2. Create a new database named:
   ```sql
   CREATE DATABASE movie_ticket_db;
   USE movie_ticket_db;
   ```
3. Run the provided SQL script (`database.sql`) to create all required tables.
4. Update your MySQL credentials (if necessary) in `backend.py`:
   ```python
   mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       password="your_password",
       database="movie_ticket_db"
   )
   ```

---

## 🖥️ Running the Project

### Option 1: Modern GUI (Recommended)

```bash
python frontend_customtk.py
```

> This launches the **modern, responsive GUI** made using `customtkinter`.

### Option 2: Classic Tkinter GUI

```bash
python frontend_tkinter.py
```

> This version is simpler and uses native Tkinter widgets.

---

## 🧠 Project Functionality

- 🎟️ Book Movie Tickets (select movie, time, seat, and price)
- 🧾 View All Bookings
- ✏️ Update or Delete Bookings
- 🧑‍💼 Manage Customer Records
- 🕒 Real-time Data stored in MySQL database

---

## 🌈 UI Features (CustomTkinter Version)

- Fully responsive design (auto-resizes with screen)
- Dark and light theme toggle
- Rounded buttons and modern input boxes
- Professional color palette
- Supports images and logos

---

## 🧰 Technologies Used

| Layer | Technology |
|--------|-------------|
| Frontend | Python (Tkinter / CustomTkinter) |
| Backend | MySQL Database |
| Language | Python 3 |
| Database Connector | mysql-connector-python |
| Styling | CustomTkinter themes and images |

---

## 📸 Screenshots

_Add screenshots of your UI here (e.g., main window, booking form, etc.)_

Example structure:
```
screenshots/
├── home_page.png
├── booking_page.png
├── view_bookings.png
```

---

## 🚀 Future Enhancements

- 🎞️ Add movie poster previews
- 📅 Integrate date/time picker for showtimes
- 💳 Add payment gateway simulation
- 🌐 Convert to a Flask/Django web application

---

## 🧑‍💻 Developer Info

**Project Title:** Movie Ticket Booking System  
**Developed by:** [Your Name / Team Name]  
**Department:** Computer Science (DBMS Mini Project)  
**Year:** 2025  

---

## 📝 License

This project is open-source and available for educational use.  
Feel free to modify and improve it!

---

⭐ *If you like this project, give it a star and share it with your classmates!*
