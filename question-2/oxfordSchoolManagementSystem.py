
"""
Created on Mon Feb 15 22:33:40 2021

@author: temi
"""

from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql



def insert():
    id = e_id.get();
    name =  e_name.get();
    age =   e_age.get();
    mat_no = e_mat_no.get(); 
    score = e_score.get();

    if(name=="" or age=="" or mat_no=="" or score==""):
        MessageBox.showinfo("Insert Status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="admin", password="123456", database="oxford_db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO grad_students values('"+id+"', '"+name+"', '"+age+"', '"+mat_no+"', '"+score+"' )")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_age.delete(0, 'end')
        e_mat_no.delete(0, 'end')
        e_score.delete(0, 'end')

        show()
        MessageBox.showinfo("Insert Status ", "Inserted Successfully");
        con.close();

def update():
    id = e_id.get();
    name =  e_name.get();
    age =   e_age.get();
    mat_no = e_mat_no.get(); 
    score = e_score.get();

    if(name=="" or age=="" or mat_no=="" or score==""):
        MessageBox.showinfo("Update Status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="admin", password="123456", database="oxford_db")
        cursor = con.cursor()
        cursor.execute("UPDATE grad_students SET name='"+name+"', age= '"+age+"', mat_no = '"+mat_no+"', score = '"+score+"' WHERE id='"+id+"'")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_age.delete(0, 'end')
        e_mat_no.delete(0, 'end')
        e_score.delete(0, 'end')

        show()
        MessageBox.showinfo("Update Status ", "Updated Successfully");
        con.close();
    

def delete():
    if(e_id.get() == ""):
        MessageBox.showinfo("Delete Status", "ID is compulsory for delete")
    else:
        con = mysql.connect(host="localhost", user="admin", password="123456", database="oxford_db")
        cursor = con.cursor()
        cursor.execute("DELETE FROM grad_students WHERE id= '"+e_id.get()+"'")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_age.delete(0, 'end')
        e_mat_no.delete(0, 'end')
        e_score.delete(0, 'end')

        show()
        MessageBox.showinfo("Delete Status ", "Deleted Successfully");
        con.close();

def get():
    
    if(e_id.get() == ""):
        MessageBox.showinfo("Fetch Status", "ID is compulsory for Fetching all students")
    else:
        con = mysql.connect(host="localhost", user="admin", password="123456", database="oxford_db")
        cursor = con.cursor()
        cursor .execute("SELECT * FROM grad_students WHERE id= '"+e_id.get()+"'")
        rows = cursor.fetchall()

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_age.delete(0, 'end')
        e_mat_no.delete(0, 'end')
        e_score.delete(0, 'end')

        for row in rows:
            e_id.insert(0, row[0])
            e_name.insert(0, row[1])
            e_age.insert(0, row[2])
            e_mat_no.insert(0, row[3])
            e_score.insert(0, row[4])

def show():
    con = mysql.connect(host="localhost", user="admin", password="123456", database="oxford_db")
    cursor = con.cursor()
    cursor .execute("SELECT * FROM grad_students")
    rows = cursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData = str(row[0])+' '+ row[1] + '    '+ str(row[2]) + '    '+str(row[3]) + '    '+str(row[4]) +'  '
        list.insert(list.size() + 1, insertData)


root = Tk()
root.geometry("700x350");
root.title("OXFORD Student Database Management System")

id = Label(root, text='Id', font=('bold', 10))
id.place(x=20, y=30)

name = Label(root, text='Name',font=('bold', 10))
name.place(x=20, y=60)

age = Label(root, text='Age',font=('bold', 10))
age.place(x=20, y=90)

mat_no = Label(root, text='Matriculation no.',font=('bold', 10))
mat_no.place(x=20, y=120)

e_score = Label(root, text="Student score", font=("bold", 10))
e_score.place(x=20, y=150)

e_id = Entry()
e_id.place(x=170, y=30)

e_name = Entry()
e_name.place(x=170, y=60)

e_age = Entry()
e_age.place(x=170, y=90)

e_mat_no = Entry()
e_mat_no.place(x=170, y=120)

e_score = Entry()
e_score.place(x=170, y=150)

insert = Button(root, text="Insert", font=('italic', 10), bg="white", command=insert)
insert.place(x=20, y=190)

update = Button(root, text="Update", font=('italic', 10), bg="white", command=update)
update.place(x=120, y=190)

delete = Button(root, text="Delete", font=('italic', 10), bg="white", command=delete)
delete.place(x=220, y=190)

get = Button(root, text="Get details", font=('italic', 10), bg="white", command=get)
get.place(x=320, y=190)

list = Listbox(root)
list.place(x=500, y=30)
show()

root.mainloop()



