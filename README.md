# Book-Store-DB

An application containing book records for a store.

![Screen of the app](https://github.com/MariuszGaljan/Book-Store-DB/blob/master/GUI.png)

Every record contains four fields:
* Title
* Author
* Year of Publication
* ISBN

The app allows various operations on the records:
* viewing the list of books
* searching for an entry absed on given data
* adding a new entry
* updating selected entry from the list
* deleting selected entry

The program is divided into two files:
* backend.py containing functions responsible for DB connection (creation if neccessary) and management
* frontend.py which creates the GUI of the app

In order to run the app, execute the frontend.py script. Installation of sqlite3 module may be required.

### Things I learned from writing this program:
* using tkinter library to create GUI with Python
* using SQLite library to perform various operations on a database
