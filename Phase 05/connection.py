import tkinter
from tkinter import *
from tkinter.ttk import *
import mysql.connector
import tkinter.messagebox as messagebox

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
t=[]


def Login_page():
   global new_window
   new_window = Toplevel(main_window)
   new_window.geometry("400x400")
   new_window.title("Login")
   new_window.configure(background='lightblue')
   Username_Label = Label(new_window, text="User_name:")
   Uname_Entry = Entry(new_window, width=40)
   Password_Label = Label(new_window, text="Password:")
   Password_Entry= Entry(new_window, width=40)
   Login_btn = Button(new_window, text="Login", command=customerview)
   Username_Label.pack(padx=5,pady=5)
   Uname_Entry.pack(padx=5,pady=5)
   Password_Label.pack(padx=5,pady=5)
   Password_Entry.pack(padx=5,pady=5)
   Login_btn.pack(padx=5,pady=5)
def Login_admin():
   global new_window
   new_window = Toplevel(main_window)
   new_window.geometry("400x400")
   new_window.title("Login")
   new_window.configure(background='lightblue')
   Username_Label = Label(new_window, text="User_name:")
   Uname_Entry = Entry(new_window, width=40)
   Password_Label = Label(new_window, text="Password:")
   Password_Entry= Entry(new_window, width=40)
   Login_btn = Button(new_window, text="Login", command=main)
   Username_Label.pack(padx=5,pady=5)
   Uname_Entry.pack(padx=5,pady=5)
   Password_Label.pack(padx=5,pady=5)
   Password_Entry.pack(padx=5,pady=5)
   Login_btn.pack(padx=5,pady=5)


def Sign_up():
   global new_window2
   global Fname_Entry
   global Lname_textbox
   global Phone_textbox
   global Email_textbox
   global Pass_textbox
   new_window2= Toplevel(main_window)
   new_window2.geometry("400x400")
   new_window2.title("Sign Up")
   new_window2.configure(background="lightblue")
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
   First_name=Fname_Entry.get()
   Last_name=Lname_textbox.get()
   Phone=Phone_textbox.get()
   Email=Email_textbox.get()
   C_password=Pass_textbox.get()

   if (First_name=="" or Last_name=="" or C_password==""):
       messagebox.showinfo("Insert satus","Missing Fields")
   else:
       cursor.execute("insert into Customer values('"+First_name+"','"+Last_name+"','"+Phone+"','"+Email+"','"+C_password+"')")
       cursor.execute("commit");
       messagebox.showinfo("Insert status","Inserted Succesfully")
       cursor.close();

def main():
   new_window3 = Toplevel(main_window)
   new_window3.geometry("400x400")
   new_window3.title("Home page")
   new_window3.configure(background="lightblue")

   register_product=Button(new_window3,text="Register new Product", command=register_p)
   delete_product=Button(new_window3,text="Delete Products",command=delete_p)
   Update_product=Button(new_window3,text="Update Products",command=update_p)
   search_products=Button(new_window3,text="Search Products")
   register_product.pack(padx=5,pady=5)
   delete_product.pack(padx=5,pady=5)
   Update_product.pack(padx=5,pady=5)
   search_products.pack(padx=5,pady=5)

def register_p():
   new_window4= Toplevel(main_window)
   new_window4.geometry("400x400")
   new_window4.title("Product Registration")
   new_window4.configure(background="lightblue")
   p_name=Label(new_window4,text="Product Name")
   pname_box=Entry(new_window4,width=40)
   p_desc=Label(new_window4,text="Description")
   pdesc_box=Entry(new_window4,width=70)
   p_name.pack(padx=5,pady=5)
   pname_box.pack(padx=5,pady=5)
   p_desc.pack(padx=5,pady=5)
   pdesc_box.pack(padx=5,pady=5)

def delete_p():
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

def update_p():
   new_window6 = Toplevel(main_window)
   new_window6.geometry("400x400")
   new_window6.title("Update Product")
   new_window6.configure(background="lightblue")
   pid=Label(new_window6,text="Product ID")
   id_box=Entry(new_window6,width=40)
   namelabel= Label(new_window6, text="Product name")
   pname= Entry(new_window6, width=40)
   productdesc = Label(new_window6, text="Product Description")
   pdesc = Entry(new_window6, width=70)
   pid.pack()
   id_box.pack()
   namelabel.pack()
   pname.pack()
   productdesc.pack()
   pdesc.pack()

def customerview():
   global list
   new_window7= Toplevel(main_window)
   new_window7.geometry("700x700")
   frmleft = tkinter.Frame(new_window7, bg='grey', width=300, height=1000)
   frmright = tkinter.Frame(new_window7, bg='lightblue', width=1000, height=1000)
   frmleft.grid(row=0, column=0)
   frmright.grid(row=0, column=1)
   products_btn=tkinter.Button(frmleft,text="Shop")
   products_btn.grid(row=2,column=1)
   search_btn = tkinter.Button(frmleft, text="search")
   search_btn.grid(row=3,column=1)
   checkout_btn=tkinter.Button(frmleft,text="Check Out",command=show)
   checkout_btn.grid(row=4,column=1,)
   list=Listbox(frmright,)
   list.grid(row=1,column=2)

def show():
   cursor.execute("Select * from Product")
   Products = cursor.fetchall();

   for product in Products:
       insertdata=str(product[0])+'        '+product[1]
       list.insert(list.size()+1,insertdata)
       cursor.close()




Title = Text(main_window, height =1, width = 50)
login=Button(main_window, text="Login as Admin", command=Login_admin)
login_user=Button(main_window, text="Login as user", command=Login_page)
sign_up=Button(main_window, text="Register as User", command=Sign_up)
Title.pack()
login.pack(padx=30,pady=10)
login_user.pack(padx=30,pady=10)
sign_up.pack(padx=30,pady=10)
mainloop()
