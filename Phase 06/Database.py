import mysql.connector
import tkinter.messagebox as messagebox
#from PIL import ImageTK

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    port="3306",
    database="Warehouse"
)
cursor = mydb.cursor()


main_window= Tk()
main_window.geometry("400x200")
main_window.title("Main Page")
main_window.configure(background='lightblue')
#bg=ImageTK.photo


def Login_page():
    global new_window
    global Uname_Entry
    global Password_Entry
    new_window = Toplevel(main_window)
    new_window.geometry("400x400")
    new_window.title("Login")
    new_window.configure(background='lightblue')
    Username_Label = Label(new_window, text="User_name:")
    Uname_Entry = Entry(new_window, width=40)
    Password_Label = Label(new_window, text="Password:")
    Password_Entry= Entry(new_window, width=40)
    Login_btn = Button(new_window, text="Login", command=loginUS_con)
    Username_Label.pack(padx=5,pady=5)
    Uname_Entry.pack(padx=5,pady=5)
    Password_Label.pack(padx=5,pady=5)
    Password_Entry.pack(padx=5,pady=5)
    Login_btn.pack(padx=5,pady=5)

def loginUS_con():
    usern=Uname_Entry.get()
    passw=Password_Entry.get()
    if usern=="" or passw=="":
        messagebox.showinfo("Error","All fields are Required")
    else:
        try:
            cursor.execute("select * from customer where email=%s and C_password=%s",(usern,passw))
            op=cursor.fetchone()
            print(op[1])
            if op==None:
                messagebox.showinfo("Error","Invalid Username or Password")
            else:
                customerview()
        except EXCEPTION as es:
            messagebox.showinfo("Error"f"Error due to:{str(es)}")



def Login_admin():
    global new_window
    global name_Entry
    global Passwor_Entry
    new_window = Toplevel(main_window)
    new_window.geometry("400x400")
    new_window.title("Login")
    new_window.configure(background='lightblue')
    Username_Label = Label(new_window, text="User_name:")
    name_Entry = Entry(new_window, width=40)
    Password_Label = Label(new_window, text="Password:")
    Passwor_Entry= Entry(new_window, width=40)
    Login_btn = Button(new_window, text="Login", command=loginAD_con)
    Username_Label.pack(padx=5,pady=5)
    name_Entry.pack(padx=5,pady=5)
    Password_Label.pack(padx=5,pady=5)
    Passwor_Entry.pack(padx=5,pady=5)
    Login_btn.pack(padx=5,pady=5)

def loginAD_con():
    usern = name_Entry.get()
    passw = Passwor_Entry.get()
    if usern == "" or passw == "":
        messagebox.showinfo("Error", "All fields are Required")
    else:
        try:
            cursor.execute("select * from customer where email=%s and C_password=%s", (usern, passw))
            op = cursor.fetchone()
            print(op[1])
            if op == None:
                messagebox.showinfo("Error", "Invalid Username or Password")

            else:
                if usern=="bobjohn@gmail.com" and passw=="123":
                    main()
                else:
                    messagebox.showinfo("Error","Admin not registered")
        except EXCEPTION as es:
            messagebox.showinfo("Error"f"Error due to:{str(es)}")


def Sign_up():
    global new_window2
    global Fname_Entry
    global Lname_textbox
    global Phone_textbox
    global Email_textbox
    global Pass_textbox
    global Fid_Entry
    new_window2= Toplevel(main_window)
    new_window2.geometry("400x400")
    new_window2.title("Sign Up")
    new_window2.configure(background="lightblue")
    Fid_Entry = Entry(new_window2, width=40)
    Fid_Entry.pack()
    Fname_label=Label(new_window2,text="First Name")
    Fname_Entry=Entry(new_window2,width=40)
    Lname_label= Label(new_window2, text="Last Name")
    Lname_textbox = Entry(new_window2, width=40)
    Phone_label = Label(new_window2, text="phone number")
    Phone_textbox = Entry(new_window2, width=40)
    Email_label = Label(new_window2, text="Email")
    Email_textbox = Entry(new_window2, width=40)
    Pass_label= Label(new_window2, text="password")
    Pass_textbox = Entry(new_window2, width=40)
    sign_btn = Button(new_window2, text="Sign Up", command=insert)
    Fname_label.pack(padx=5,pady=5)
    Fname_Entry.pack(padx=5,pady=5)
    Lname_label.pack(padx=5,pady=5)
    Lname_textbox.pack(padx=5,pady=5)
    Phone_label.pack(padx=5,pady=5)
    Phone_textbox.pack(padx=5,pady=5)
    Email_label.pack(padx=5,pady=5)
    Email_textbox.pack(padx=5,pady=5)
    Pass_label.pack(padx=5,pady=5)
    Pass_textbox.pack(padx=5,pady=5)
    sign_btn.pack(padx=5,pady=5)

def insert():
    ID=Fid_Entry.get()
    First_name=Fname_Entry.get()
    Last_name=Lname_textbox.get()
    Phone=Phone_textbox.get()
    Email=Email_textbox.get()
    C_password=Pass_textbox.get()

    if (First_name=="" or Last_name=="" or C_password==""):
        messagebox.showinfo("Insert satus","Missing Fields")
    else:
        cursor.execute("insert into Customer values('"+ID+"','"+First_name+"','"+Last_name+"','"+Phone+"','"+Email+"','"+C_password+"')")
        cursor.execute("commit");
        messagebox.showinfo("Insert status","Inserted Succesfully")
        cursor.close();

def main():
    new_window3 = Toplevel(main_window)
    new_window3.geometry("400x400")
    new_window3.title("Home page")
    new_window3.configure(background="lightblue")

    register_product=Button(new_window3,text="Register new Product", command=register_p, width=20)
    delete_product=Button(new_window3,text="Delete Products",command=delete_p, width=20)
    Update_product=Button(new_window3,text="Update Products",command=update_p,width=20)
    search_products=Button(new_window3,text="Search Products",command=search_p,width=20)
    register_product.pack(padx=5,pady=5)
    delete_product.pack(padx=5,pady=5)
    Update_product.pack(padx=5,pady=5)
    search_products.pack(padx=5,pady=5)

def register_p():
    global P_ID
    global pname_box
    global pdesc_box
    global Pmanifactuer_box
    global pExpiration_box
    new_window4= Toplevel(main_window)
    new_window4.geometry("400x400")
    new_window4.title("Product Registration")
    new_window4.configure(background="lightblue")
    P_ID = Entry(new_window4, width=40)
    P_ID.pack()
    p_name=Label(new_window4,text="Product Name")
    pname_box=Entry(new_window4,width=40)
    p_desc=Label(new_window4,text="Description")
    pdesc_box=Entry(new_window4,width=40)
    p_Manifacturer = Label(new_window4, text="Manifacturer")
    Pmanifactuer_box = Entry(new_window4, width=40)
    p_Expiration = Label(new_window4, text="Expiration Date")
    pExpiration_box = Entry(new_window4, width=40)
    p_name.pack(padx=5,pady=5)
    pname_box.pack(padx=5,pady=5)
    p_desc.pack(padx=5,pady=5)
    pdesc_box.pack(padx=5,pady=5)
    p_Manifacturer.pack(padx=5, pady=5)
    Pmanifactuer_box.pack(padx=5, pady=5)
    p_Expiration.pack(padx=5, pady=5)
    pExpiration_box.pack(padx=5, pady=5)
    register_product = Button(new_window4, text="Register new Product", command=Register_con)
    register_product.pack()
def Register_con():
    ID=P_ID.get()
    Product_name=pname_box.get()
    description=pdesc_box.get()
    manifacturer=Pmanifactuer_box.get()
    Expiration_date=pExpiration_box.get()

    if (Product_name=="" or description==""):
        messagebox.showinfo("Insert satus","Missing Fields")
    else:
        cursor.execute("insert into Product values('"+ID+"','"+Product_name+"','"+description+"','"+manifacturer+"','"+Expiration_date+"')")
        cursor.execute("commit");
        messagebox.showinfo("Insert status","Inserted Succesfully")
        cursor.close();

def delete_p():
    global p_id
    new_window5= Toplevel(main_window)
    new_window5.geometry("400x400")
    new_window5.title("Delete Product")
    new_window5.configure(background="lightblue")
    idlabel=Label(new_window5,text="Product Id")
    p_id=Entry(new_window5,width=40)
    name_label=Label(new_window5,text="Product name")
    pname=Entry(new_window5,width=40)
    idlabel.pack()
    p_id.pack()
    name_label.pack()
    pname.pack()
    delete_product = Button(new_window5, text="Delete new Product", command=delete_con)
    delete_product.pack()

def delete_con():
    Product_id=p_id.get()
    if (Product_id == ""):
        messagebox.showinfo("Delete Status", "IDmust be completed")
    else:
        cursor.execute("Delete from product where Product_id='" + Product_id + "'")

        cursor.execute("commit");

        messagebox.showinfo("Delete Status", "Deletion Succesfull")


def update_p():
    global id_box
    global pname
    global pdesc
    new_window6 = Toplevel(main_window)
    new_window6.geometry("400x400")
    new_window6.title("Update Product")
    new_window6.configure(background="lightblue")
    pid=Label(new_window6,text="Product ID")
    id_box=Entry(new_window6,width=40)
    namelabel= Label(new_window6, text="Product name")
    pname= Entry(new_window6, width=40)
    productdesc = Label(new_window6, text="Product Description")
    pdesc = Entry(new_window6, width=40)
    pid.pack()
    id_box.pack()
    namelabel.pack()
    pname.pack()
    productdesc.pack()
    pdesc.pack()
    Update_product = Button(new_window6, text="Update Product", command=update_con)
    Update_product.pack()

def update_con():
    Product_id=id_box.get()
    Product_name = pname.get()
    description = pdesc.get()

    if (Product_name == "" or description == ""):
        messagebox.showinfo("Insert satus", "Missing Fields")
    else:
        cursor.execute("Update Product set description='" + description + "' where Product_id='" +Product_id+ "')")
        cursor.execute("commit");
        messagebox.showinfo("Insert status", "Inserted Succesfully")
        cursor.close(); # cant figure out what the problem is

def search_p():
    global listi
    new_window7 = Toplevel(main_window)
    new_window7.geometry("400x400")
    new_window7.title("Update Product")
    new_window7.configure(background="lightblue")

    listi=Listbox(new_window7,width=30,height=20)
    listi.pack()
    Search=Button(new_window7,text='search',command=search_con)
    Search.pack(padx=5,pady=5)
def search_con():
    cursor.execute("Select * from Product")
    Products = cursor.fetchall();

    for product in Products:
        insertdata = str(product[0]) + '        ' + product[1]
        listi.insert(listi.size() + 1, insertdata)
        cursor.close()


def customerview():
    global list
    new_window7 = Toplevel(main_window)
    new_window7.geometry("500x500")
    new_window7.title("Update Product")
    new_window7.configure(background="lightblue")
    list=Listbox(new_window7,height=20, width=40)
    list.pack()
    search=Button(new_window7,text="Look up products", command=show)
    search.pack(padx=5,pady=5)

def show():
    cursor.execute("Select * from Product")
    Products = cursor.fetchall();

    for product in Products:
        insertdata=str(product[0])+'        '+product[1]
        list.insert(list.size()+1,insertdata)
        cursor.close()

import tkinter
from tkinter import *
from tkinter.ttk import *
import mysql.connector
import tkinter.messagebox as messagebox
#from PIL import ImageTK

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    port="3306",
    database="Warehouse"
)
cursor = mydb.cursor()


main_window= Tk()
main_window.geometry("400x200")
main_window.title("Main Page")
main_window.configure(background='lightblue')
#bg=ImageTK.photo


def Login_page():
    global new_window
    global Uname_Entry
    global Password_Entry
    new_window = Toplevel(main_window)
    new_window.geometry("400x400")
    new_window.title("Login")
    new_window.configure(background='lightblue')
    Username_Label = Label(new_window, text="User_name:")
    Uname_Entry = Entry(new_window, width=40)
    Password_Label = Label(new_window, text="Password:")
    Password_Entry= Entry(new_window, width=40)
    Login_btn = Button(new_window, text="Login", command=loginUS_con)
    Username_Label.pack(padx=5,pady=5)
    Uname_Entry.pack(padx=5,pady=5)
    Password_Label.pack(padx=5,pady=5)
    Password_Entry.pack(padx=5,pady=5)
    Login_btn.pack(padx=5,pady=5)

def loginUS_con():
    usern=Uname_Entry.get()
    passw=Password_Entry.get()
    if usern=="" or passw=="":
        messagebox.showinfo("Error","All fields are Required")
    else:
        try:
            cursor.execute("select * from customer where email=%s and C_password=%s",(usern,passw))
            op=cursor.fetchone()
            print(op[1])
            if op==None:
                messagebox.showinfo("Error","Invalid Username or Password")
            else:
                customerview()
        except EXCEPTION as es:
            messagebox.showinfo("Error"f"Error due to:{str(es)}")



def Login_admin():
    global new_window
    global name_Entry
    global Passwor_Entry
    new_window = Toplevel(main_window)
    new_window.geometry("400x400")
    new_window.title("Login")
    new_window.configure(background='lightblue')
    Username_Label = Label(new_window, text="User_name:")
    name_Entry = Entry(new_window, width=40)
    Password_Label = Label(new_window, text="Password:")
    Passwor_Entry= Entry(new_window, width=40)
    Login_btn = Button(new_window, text="Login", command=loginAD_con)
    Username_Label.pack(padx=5,pady=5)
    name_Entry.pack(padx=5,pady=5)
    Password_Label.pack(padx=5,pady=5)
    Passwor_Entry.pack(padx=5,pady=5)
    Login_btn.pack(padx=5,pady=5)

def loginAD_con():
    usern = name_Entry.get()
    passw = Passwor_Entry.get()
    if usern == "" or passw == "":
        messagebox.showinfo("Error", "All fields are Required")
    else:
        try:
            cursor.execute("select * from customer where email=%s and C_password=%s", (usern, passw))
            op = cursor.fetchone()
            print(op[1])
            if op == None:
                messagebox.showinfo("Error", "Invalid Username or Password")

            else:
                if usern=="bobjohn@gmail.com" and passw=="123":
                    main()
                else:
                    messagebox.showinfo("Error","Admin not registered")
        except EXCEPTION as es:
            messagebox.showinfo("Error"f"Error due to:{str(es)}")


def Sign_up():
    global new_window2
    global Fname_Entry
    global Lname_textbox
    global Phone_textbox
    global Email_textbox
    global Pass_textbox
    global Fid_Entry
    new_window2= Toplevel(main_window)
    new_window2.geometry("400x400")
    new_window2.title("Sign Up")
    new_window2.configure(background="lightblue")
    Fid_Entry = Entry(new_window2, width=40)
    Fid_Entry.pack()
    Fname_label=Label(new_window2,text="First Name")
    Fname_Entry=Entry(new_window2,width=40)
    Lname_label= Label(new_window2, text="Last Name")
    Lname_textbox = Entry(new_window2, width=40)
    Phone_label = Label(new_window2, text="phone number")
    Phone_textbox = Entry(new_window2, width=40)
    Email_label = Label(new_window2, text="Email")
    Email_textbox = Entry(new_window2, width=40)
    Pass_label= Label(new_window2, text="password")
    Pass_textbox = Entry(new_window2, width=40)
    sign_btn = Button(new_window2, text="Sign Up", command=insert)
    Fname_label.pack(padx=5,pady=5)
    Fname_Entry.pack(padx=5,pady=5)
    Lname_label.pack(padx=5,pady=5)
    Lname_textbox.pack(padx=5,pady=5)
    Phone_label.pack(padx=5,pady=5)
    Phone_textbox.pack(padx=5,pady=5)
    Email_label.pack(padx=5,pady=5)
    Email_textbox.pack(padx=5,pady=5)
    Pass_label.pack(padx=5,pady=5)
    Pass_textbox.pack(padx=5,pady=5)
    sign_btn.pack(padx=5,pady=5)

def insert():
    ID=Fid_Entry.get()
    First_name=Fname_Entry.get()
    Last_name=Lname_textbox.get()
    Phone=Phone_textbox.get()
    Email=Email_textbox.get()
    C_password=Pass_textbox.get()

    if (First_name=="" or Last_name=="" or C_password==""):
        messagebox.showinfo("Insert satus","Missing Fields")
    else:
        cursor.execute("insert into Customer values('"+ID+"','"+First_name+"','"+Last_name+"','"+Phone+"','"+Email+"','"+C_password+"')")
        cursor.execute("commit");
        messagebox.showinfo("Insert status","Inserted Succesfully")
        cursor.close();

def main():
    new_window3 = Toplevel(main_window)
    new_window3.geometry("400x400")
    new_window3.title("Home page")
    new_window3.configure(background="lightblue")

    register_product=Button(new_window3,text="Register new Product", command=register_p, width=20)
    delete_product=Button(new_window3,text="Delete Products",command=delete_p, width=20)
    Update_product=Button(new_window3,text="Update Products",command=update_p,width=20)
    search_products=Button(new_window3,text="Search Products",command=search_p,width=20)
    register_product.pack(padx=5,pady=5)
    delete_product.pack(padx=5,pady=5)
    Update_product.pack(padx=5,pady=5)
    search_products.pack(padx=5,pady=5)

def register_p():
    global P_ID
    global pname_box
    global pdesc_box
    global Pmanifactuer_box
    global pExpiration_box
    new_window4= Toplevel(main_window)
    new_window4.geometry("400x400")
    new_window4.title("Product Registration")
    new_window4.configure(background="lightblue")
    P_ID = Entry(new_window4, width=40)
    P_ID.pack()
    p_name=Label(new_window4,text="Product Name")
    pname_box=Entry(new_window4,width=40)
    p_desc=Label(new_window4,text="Description")
    pdesc_box=Entry(new_window4,width=40)
    p_Manifacturer = Label(new_window4, text="Manifacturer")
    Pmanifactuer_box = Entry(new_window4, width=40)
    p_Expiration = Label(new_window4, text="Expiration Date")
    pExpiration_box = Entry(new_window4, width=40)
    p_name.pack(padx=5,pady=5)
    pname_box.pack(padx=5,pady=5)
    p_desc.pack(padx=5,pady=5)
    pdesc_box.pack(padx=5,pady=5)
    p_Manifacturer.pack(padx=5, pady=5)
    Pmanifactuer_box.pack(padx=5, pady=5)
    p_Expiration.pack(padx=5, pady=5)
    pExpiration_box.pack(padx=5, pady=5)
    register_product = Button(new_window4, text="Register new Product", command=Register_con)
    register_product.pack()
def Register_con():
    ID=P_ID.get()
    Product_name=pname_box.get()
    description=pdesc_box.get()
    manifacturer=Pmanifactuer_box.get()
    Expiration_date=pExpiration_box.get()

    if (Product_name=="" or description==""):
        messagebox.showinfo("Insert satus","Missing Fields")
    else:
        cursor.execute("insert into Product values('"+ID+"','"+Product_name+"','"+description+"','"+manifacturer+"','"+Expiration_date+"')")
        cursor.execute("commit");
        messagebox.showinfo("Insert status","Inserted Succesfully")
        cursor.close();

def delete_p():
    global p_id
    new_window5= Toplevel(main_window)
    new_window5.geometry("400x400")
    new_window5.title("Delete Product")
    new_window5.configure(background="lightblue")
    idlabel=Label(new_window5,text="Product Id")
    p_id=Entry(new_window5,width=40)
    name_label=Label(new_window5,text="Product name")
    pname=Entry(new_window5,width=40)
    idlabel.pack()
    p_id.pack()
    name_label.pack()
    pname.pack()
    delete_product = Button(new_window5, text="Delete new Product", command=delete_con)
    delete_product.pack()

def delete_con():
    Product_id=p_id.get()
    if (Product_id == ""):
        messagebox.showinfo("Delete Status", "IDmust be completed")
    else:
        cursor.execute("Delete from product where Product_id='" + Product_id + "'")

        cursor.execute("commit");

        messagebox.showinfo("Delete Status", "Deletion Succesfull")


def update_p():
    global id_box
    global pname
    global pdesc
    new_window6 = Toplevel(main_window)
    new_window6.geometry("400x400")
    new_window6.title("Update Product")
    new_window6.configure(background="lightblue")
    pid=Label(new_window6,text="Product ID")
    id_box=Entry(new_window6,width=40)
    namelabel= Label(new_window6, text="Product name")
    pname= Entry(new_window6, width=40)
    productdesc = Label(new_window6, text="Product Description")
    pdesc = Entry(new_window6, width=40)
    pid.pack()
    id_box.pack()
    namelabel.pack()
    pname.pack()
    productdesc.pack()
    pdesc.pack()
    Update_product = Button(new_window6, text="Update Product", command=update_con)
    Update_product.pack()

def update_con():
    Product_id=id_box.get()
    Product_name = pname.get()
    description = pdesc.get()

    if (Product_name == "" or description == ""):
        messagebox.showinfo("Insert satus", "Missing Fields")
    else:
        cursor.execute("Update Product set description='" + description + "' where Product_id='" +Product_id+ "')")
        cursor.execute("commit");
        messagebox.showinfo("Insert status", "Inserted Succesfully")
        cursor.close(); # cant figure out what the problem is

def search_p():
    global listi
    new_window7 = Toplevel(main_window)
    new_window7.geometry("400x400")
    new_window7.title("Update Product")
    new_window7.configure(background="lightblue")

    listi=Listbox(new_window7,width=30,height=20)
    listi.pack()
    Search=Button(new_window7,text='search',command=search_con)
    Search.pack(padx=5,pady=5)
def search_con():
    cursor.execute("Select * from Product")
    Products = cursor.fetchall();

    for product in Products:
        insertdata = str(product[0]) + '        ' + product[1]
        listi.insert(listi.size() + 1, insertdata)
        cursor.close()


def customerview():
    global list
    new_window7 = Toplevel(main_window)
    new_window7.geometry("500x500")
    new_window7.title("Update Product")
    new_window7.configure(background="lightblue")
    list=Listbox(new_window7,height=20, width=40)
    list.pack()
    search=Button(new_window7,text="Look up products", command=show)
    search.pack(padx=5,pady=5)

def show():
    cursor.execute("Select * from Product")
    Products = cursor.fetchall();

    for product in Products:
        insertdata=str(product[0])+'        '+product[1]
        list.insert(list.size()+1,insertdata)
        cursor.close()

login=Button(main_window, text="Login as Admin", command=Login_admin, width=20)
login_user=Button(main_window, text="Login as user", command=Login_page, width=20)
sign_up=Button(main_window, text="Register as User", command=Sign_up, width=20)
login.pack(padx=30,pady=10)
login_user.pack(padx=30,pady=10)
sign_up.pack(padx=30,pady=10)
mainloop()
