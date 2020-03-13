from tkinter import *
from book_store.src.backend import Backend

selectedRow = None
backend = Backend()

def getSelectedRow(event):
    global selectedRow
    index = recordList.curselection()[0]
    selectedRow = recordList.get(index)
    titleVar.set(selectedRow[1])
    authorVar.set(selectedRow[2])
    yearVar.set(selectedRow[3])
    isbnVar.set(selectedRow[4])


def viewCommand():
    recordList.delete(0, END)
    for record in backend.view():
        recordList.insert(END, record)

def searchCommand():
    recordList.delete(0, END)
    for record in backend.search(titleVar.get(), authorVar.get(), yearVar.get(), isbnVar.get()):
        recordList.insert(END, record)

def addCommand():
    backend.insert(titleVar.get(), authorVar.get(), yearVar.get(), isbnVar.get())
    recordList.delete(0, END)
    for record in backend.search(titleVar.get(), authorVar.get(), yearVar.get(), isbnVar.get()):
        recordList.insert(END, record)

def deleteCommand():
    backend.delete(selectedRow[0])

def updateCommand():
    backend.update(selectedRow[0], titleVar.get(), authorVar.get(), yearVar.get(), isbnVar.get())



window = Tk()
window.wm_title("Book Database")

titleLabel = Label(window, text="Title")
titleLabel.grid(row=0, column=0)

titleVar = StringVar()
titleEntry = Entry(window, textvariable=titleVar)
titleEntry.grid(row = 0, column=1)


authorLabel = Label(window, text="Author")
authorLabel.grid(row=0, column=2)

authorVar = StringVar()
authorEntry = Entry(window, textvariable=authorVar)
authorEntry.grid(row = 0, column=3)


yearLabel = Label(window, text="Year")
yearLabel.grid(row=1, column=0)

yearVar = StringVar()
yearEntry = Entry(window, textvariable=yearVar)
yearEntry.grid(row = 1, column=1)


isbnLabel = Label(window, text="ISBN")
isbnLabel.grid(row=1, column=2)

isbnVar = StringVar()
isbnEntry = Entry(window, textvariable=isbnVar)
isbnEntry.grid(row = 1, column=3)


recordList = Listbox(window, height=10, width=50)
recordList.grid(row=2, column=0, rowspan=6, columnspan=2)

recordScrollBar = Scrollbar(window)
recordScrollBar.grid(row=2, column=2, rowspan=6)

recordList.configure(yscrollcommand=recordScrollBar.set)
recordScrollBar.configure(command=recordList.yview)

recordList.bind('<<ListboxSelect>>', getSelectedRow)


b1=Button(window,text="View all", width=12, command=viewCommand)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12, command=searchCommand)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12, command=addCommand)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12, command=updateCommand)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12, command=deleteCommand)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12, command=window.destroy)
b6.grid(row=7,column=3)


window.mainloop()
