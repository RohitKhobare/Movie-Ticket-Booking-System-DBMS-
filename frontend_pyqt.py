# frontend_pyqt.py
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPushButton, QTextEdit, QTableWidget, QTableWidgetItem,
                             QMessageBox)
from PyQt6.QtCore import Qt
import MiniProject_Backend

MiniProject_Backend.MovieData()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movie Ticket Booking - PyQt6")
        self.resize(1100,700)
        main = QVBoxLayout()
        header = QLabel("ONLINE MOVIE TICKET BOOKING")
        header.setStyleSheet("font-size:22px; font-weight:bold; color: orange;")
        main.addWidget(header, alignment=Qt.AlignmentFlag.AlignCenter)

        body = QHBoxLayout()
        left = QVBoxLayout()
        right = QVBoxLayout()

        # Input fields
        self.fields = {}
        labels = ["Movie ID","Name","Release Date","Director","Cast","Budget","Duration","Rating"]
        for lab in labels:
            row = QHBoxLayout()
            lbl = QLabel(lab+":")
            ent = QLineEdit()
            row.addWidget(lbl)
            row.addWidget(ent)
            left.addLayout(row)
            self.fields[lab] = ent

        btn_row = QHBoxLayout()
        btn_add = QPushButton("Add")
        btn_disp = QPushButton("Display")
        btn_search = QPushButton("Search")
        btn_update = QPushButton("Update")
        btn_delete = QPushButton("Delete")
        btn_clear = QPushButton("Clear")
        for b in (btn_add, btn_disp, btn_search, btn_update, btn_delete, btn_clear):
            btn_row.addWidget(b)
        left.addLayout(btn_row)

        # Right: table
        self.table = QTableWidget(0,9)
        self.table.setHorizontalHeaderLabels(["DB_ID","M_ID","Name","Date","Director","Cast","Budget","Dur","Rating"])
        self.table.setSelectionBehavior(self.table.SelectionBehavior.SelectRows)
        right.addWidget(self.table)

        body.addLayout(left, 1)
        body.addLayout(right, 2)
        main.addLayout(body)
        self.setLayout(main)

        # Connect
        btn_add.clicked.connect(self.add)
        btn_disp.clicked.connect(self.display)
        btn_search.clicked.connect(self.search)
        btn_update.clicked.connect(self.update)
        btn_delete.clicked.connect(self.delete)
        btn_clear.clicked.connect(self.clear)
        self.table.cellClicked.connect(self.load_from_table)

        self.display()

    def get_inputs(self):
        return {k: self.fields[k].text().strip() for k in self.fields}

    def add(self):
        d = self.get_inputs()
        if not d["Movie ID"] or not d["Name"]:
            QMessageBox.warning(self, "Missing", "Provide Movie ID & Name")
            return
        MiniProject_Backend.AddMovieRec(d["Movie ID"], d["Name"], d["Release Date"], d["Director"],
                                       d["Cast"], d["Budget"], d["Duration"], d["Rating"])
        QMessageBox.information(self, "Added", "Movie added.")
        self.display()
        self.clear()

    def display(self):
        rows = MiniProject_Backend.ViewMovieData()
        self.table.setRowCount(0)
        for r in rows:
            rowpos = self.table.rowCount()
            self.table.insertRow(rowpos)
            for i, val in enumerate(r):
                self.table.setItem(rowpos, i, QTableWidgetItem(str(val)))

    def search(self):
        d = self.get_inputs()
        rows = MiniProject_Backend.SearchMovieData(d["Movie ID"], d["Name"], d["Release Date"], d["Director"],
                                                  d["Cast"], d["Budget"], d["Duration"], d["Rating"])
        self.table.setRowCount(0)
        for r in rows:
            rowpos = self.table.rowCount()
            self.table.insertRow(rowpos)
            for i, val in enumerate(r):
                self.table.setItem(rowpos, i, QTableWidgetItem(str(val)))

    def load_from_table(self, row, col):
        vals = [self.table.item(row, i).text() for i in range(self.table.columnCount())]
        # populate fields
        keys = ["Movie ID","Name","Release Date","Director","Cast","Budget","Duration","Rating"]
        for i,k in enumerate(keys):
            self.fields[k].setText(vals[i+1])  # shift by 1 because dbid at 0

    def delete(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Select", "Select a row to delete")
            return
        dbid = int(self.table.item(selected, 0).text())
        MiniProject_Backend.DeleteMovieRec(dbid)
        QMessageBox.information(self, "Deleted", "Record deleted.")
        self.display()

    def update(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Select", "Select a row to update")
            return
        dbid = int(self.table.item(selected, 0).text())
        d = self.get_inputs()
        MiniProject_Backend.DeleteMovieRec(dbid)
        MiniProject_Backend.AddMovieRec(d["Movie ID"], d["Name"], d["Release Date"], d["Director"],
                                       d["Cast"], d["Budget"], d["Duration"], d["Rating"])
        QMessageBox.information(self, "Updated", "Record updated.")
        self.display()

    def clear(self):
        for f in self.fields.values():
            f.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
