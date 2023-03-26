from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from AnotherClass import CustomerInfoDb
from tkinter.messagebox import showerror
import pickle 

db = CustomerInfoDb('dbactivity3.db')

# db.fetch() Kuhaon ang data then  parts_list.insert(END, row) is gi sulod niya sa katong white box
def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
    try:    
        db.insert(CustomerID.get(), Firstname.get(), Lastname.get(),
               Age.get(), OrderStatus.get())
        parts_list.delete(0, END)
        parts_list.insert(END, (CustomerID.get(), Firstname.get(), Lastname.get(),
                Age.get(), OrderStatus.get()))
    
    except:
        if Firstname.get() == '' or Lastname.get() == '' or Age.get() == '' or OrderStatus.get() == '':
            messagebox.showerror('*Required Fields', 'Please include all fields')
        return
    
    finally:
        clear_text()
        populate_list()

# Allows user  to select the data either
def select_item(event):
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        Firstname.delete(0, END)
        Firstname.insert(END, selected_item[1])
        Lastname.delete(0, END)
        Lastname.insert(END, selected_item[2])
        Age.delete(0, END)
        Age.insert(END, selected_item[3])
        OrderStatus.delete(0, END)
        OrderStatus.insert(END, selected_item[4])
        
def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def clear_text():
    try:
        CustomerID.delete(0, END)
        Firstname.delete(0, END)
        Lastname.delete(0, END)
        Age.delete(0, END)
        
    except:
        return
            
#Open to Read the file 
def open_file():
    path = filedialog.askopenfilename(initialdir="C:\\Users\\Karen\\Documents\\test", defaultextension='.txt',filetypes=[("Text file",".txt"),])
    
    if(path):
        fh =open(path, 'r')
        messagebox.showinfo(path,fh.read())
         
#Write File Handling
def save_file():
    try:
        file = open("storeData.txt", "wb")
        file.write(db.fetch())
        
    finally:
        file.close()
        messagebox.showinfo("*", "Database as text has been saved successfully!")
        
def convert_binary():
    all = (str(db.fetch()))
    try:
        result = ' '. join(format(ord(i), 'b') for i in all)
        x = open("storeBinary.txt", "wb") #wb
        pickle.dump(result, x)

    except:
        messagebox.showerror("", "Fail to convert file")
        
    finally:
        x.close()
        messagebox.showinfo("++The Database has been converted into Binary file++", result)
        print("Finally")

#===============================Root GUI====================================
root = Tk()
root = root
root.title("SIA Activity 3 ni Karen Cadalo ")
root.geometry("1000x690")
root.resizable('false', 'false')

my_menu = Menu(root)
root.configure(menu = my_menu,  bg = "#FFCC00")

file_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label = "File", menu=file_menu)
file_menu.add_command(label = "Open File", command = open_file)
file_menu.add_command(label = "Save Database as text", command = save_file)
file_menu.add_command(label = "Save As..")
file_menu.add_separator()
file_menu.add_command(label = "Convert File Database As Binary", command = convert_binary)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command=root.quit)

status_bar = Label(root, text = 'Ready     ', anchor = E)
status_bar.pack(fill=X, side = BOTTOM)

TopHeader =Label(root,text="Data Entry of Customer Order Status ", bg = '#FFCC00',  fg = '#000000', font = 'Roboto 38 bold')
TopHeader.pack(side=TOP, fill= X, ipady = 18)  

#===============================Left Layout Form====================================
LeftLayoutForm =  Frame(root, bg='#FF6464')
LeftLayoutForm.place(x=0, y=100, width=350, height=550)

CustomerText = Label(LeftLayoutForm, text = "Customer ID", bg = '#FF6B6B', font = ("Roboto 14"))
CustomerText.grid(row = 1, column = 0, padx=20, pady = 10, sticky="w")
CustomerID = Entry(LeftLayoutForm, font= ("Roboto", 15), borderwidth = 2)
CustomerID.grid(row = 2, column = 0, padx=20, pady=0, ipadx=20, ipady=3)

FirstnameText = Label(LeftLayoutForm, text = "Firstname", bg = '#FF6B6B', font = ("Roboto 14"))
FirstnameText.grid(row = 3, column = 0, padx=20, pady = 10, sticky="w")
Firstname = Entry(LeftLayoutForm, font= ("Roboto", 15), borderwidth = 2)
Firstname.grid(row = 4, column = 0, padx=20, pady=0, ipadx=20, ipady=3)

LastnameText = Label(LeftLayoutForm, text = "Lastname", bg = '#FF6B6B', font = ("Roboto 14"))
LastnameText.grid(row = 5, column = 0, padx=20, pady = 10, sticky="w")
Lastname = Entry(LeftLayoutForm, font= ("Roboto", 15), borderwidth = 2)
Lastname.grid(row = 6, column = 0, padx=20, pady=0, ipadx=20, ipady=3)

AgeText = Label(LeftLayoutForm, text = "Age", bg = '#FF6B6B', font = ("Roboto 14"))
AgeText.grid(row = 7, column = 0, padx=20, pady = 10, sticky="w")
Age= Spinbox(LeftLayoutForm, from_=18, to=110, font= ("Roboto", 15), borderwidth = 2)
Age.grid(row = 8, column = 0, padx=20, pady=0, ipadx=12, ipady=3)

OrderStatusText = Label(LeftLayoutForm, text = "Order Status", bg = '#FF6B6B', font = ("Roboto 14 bold"))
OrderStatusText.grid(row = 9, column = 0, padx=20, pady = 10, sticky="w")

OrderStatus = StringVar(value="Order Failed")
OrderStatus1 = Checkbutton(LeftLayoutForm, text="Order Completed",
                                       variable=OrderStatus, onvalue="Order Completed", offvalue="Order Failed",  bg = '#FF6B6B', font = ("Roboto 12"))

OrderStatus1.grid(row = 10, column = 0, padx=20, pady=0, ipadx=20, ipady=3)

#================================================
DatabaseFrame = Frame(root, bg ="red")
DatabaseFrame.place(x= 350, y=100, width=900, height= 550)

parts_list = Listbox(DatabaseFrame, width = 70, height = 28, font ='consolas')
parts_list.grid(row=0, column=1,  pady = 0, padx = 0)
scrollbar = Scrollbar(DatabaseFrame, orient = VERTICAL)
scrollbar.grid(row=0, column=2, ipady = 257, padx = 0)

parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

parts_list.bind('<<ListboxSelect>>', select_item)

#================================================

add_btn = Button(LeftLayoutForm, font='Roboto 12 bold', bg='#FFCC00', fg='#000000', text = "Enter Data", command = add_item)
add_btn.grid(row = 11, column = 0,ipady = 12, ipadx = 25, pady= 20, padx = 25)

### Ibutang sa dnhi abeg magamit pa
# def update_item():
#     try:
#         db.update(selected_item[0], Firstname.get(), Lastname.get(),
#                 Age.get(), OrderStatus.get())
#         populate_list()
    
#     except:
#         if Firstname.get() == '' or Lastname.get() == '' or Age.get() == '' or OrderStatus.get() == '':
#             messagebox.showerror('Required Fields', 'Please include all fields')
#         return

# update_btn = Button(btnFrame, font='Roboto 12 bold', bg='#FDDA0D', fg='#204399',  text = "Update", command = update_item)
# update_btn.grid(row = 2, column = 2, ipady = 12, ipadx = 25, pady= 20, padx = 25)

# del_btn= Button(btnFrame, font='Roboto 12 bold', bg='#FDDA0D', fg='#204399',  text = "Delete", command = remove_item)
# del_btn.grid(row = 2, column = 3, ipady = 12, ipadx = 25, pady= 20, padx = 25)

# clear_btn = Button(btnFrame, font='Roboto 12 bold', bg='#FDDA0D', fg='#204399', text = "Clear", command = clear_text)
# clear_btn.grid(row = 2, column = 4, ipady = 12, ipadx = 25, pady= 20, padx = 25)
# populate_list()

root.mainloop()