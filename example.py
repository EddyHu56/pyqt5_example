import sys
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sqlite3

app = QApplication(sys.argv)
main_window = QWidget()
# con = QSqlDatabase.addDatabase("QSQLITE")
# con.setDatabaseName("notes.sqlite")

conn = sqlite3.connect('notes.db')
# cursor object
cursor = conn.cursor()
# drop query
cursor.execute("DROP TABLE IF EXISTS STUDENT")
# create query
query = """
        CREATE TABLE notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            title VARCHAR(255) NOT NULL,
            description VARCHAR(255),
            date_start TIMESTAMP,
            date_end TIMESTAMP,
            date_created TIMESTAMP,
            date_modified TIMESTAMP
        )
        """
cursor.execute(query)
# commit and close
conn.commit()
conn.close()

def submitData(title, description):
    conn = sqlite3.connect('notes.db')
    conn.execute("INSERT INTO NOTES (ID,NAME,ROLL,ADDRESS,CLASS) "
                "VALUES (1, 'John', '001', 'Bangalore', '10th')")
    conn.execute("INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS) "
                "VALUES (2, 'Naren', '002', 'Hyd', '12th')")
    conn.commit()
    conn.close()
    print("Judul notes",title)
    print("Description notes", description)
    print("Submit data executed")

def deleteData(self):
    print("Judul notes" + self.title)
    print("Description notes" + self.description)
    print("Delete data executed")

def checkConnectionDb():
    if conn.open():
        return True
    print("Database Error: %s" % conn.lastError().databaseText())
    return False
        
def createTable():
    createTableQuery = QSqlQuery()
    createTableQuery.exec(
        """
        CREATE TABLE NOTES (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            title VARCHAR(255) NOT NULL,
            description VARCHAR(255),
            date_start TIMESTAMP,
            date_end TIMESTAMP,
            date_created TIMESTAMP,
            date_modified TIMESTAMP
        )
        """
    )
    cursor.execute(query)
    # commit and close
    conn.commit()
    conn.close()

def mainWindow():

    main_layout = QHBoxLayout()
    child_layout = QVBoxLayout()
    date_layout = QHBoxLayout()
    listView = QListView()

    et_title = QTextEdit()
    et_description = QPlainTextEdit()
    addButton = QPushButton("Submit")
    deleteButton = QPushButton("Delete")

    et_timeStart = QDateTimeEdit()
    et_timeEnd = QDateTimeEdit()

    child_layout.addWidget(et_title)
    et_title.setPlaceholderText("Masukkan judul") 
    child_layout.addLayout(date_layout)
    child_layout.addWidget(et_description)
    et_description.setPlaceholderText("Masukkan deskripsi") 
    date_layout.addWidget(et_timeStart)
    date_layout.addWidget(et_timeEnd)
    child_layout.addWidget(addButton)

    addButton.clicked.connect(lambda : submitData(et_title.toPlainText(), et_description.toPlainText()))
    child_layout.addWidget(deleteButton)
    main_layout.addWidget(listView)

    main_window.setLayout(main_layout)
    main_layout.addLayout(child_layout)
    child_layout.addLayout(date_layout)
    # main_layout.addWidget(addButton)
    # main_layout.addWidget(deleteButton)

    main_window.show()

if __name__ == '__main__':
    # createTable()
    if checkConnectionDb():
        mainWindow()
        main_window.setGeometry(600,400,600,400)
        main_window.setWindowTitle("PyQt")
    else:
        sys.exit(1)


    sys.exit(app.exec_())