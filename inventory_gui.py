import tkinter
from tkinter import ttk , messagebox
import custom


root = tkinter.Tk()
root.title('Inventory')
root.geometry("1300x650+100+50")

style = ttk.Style()
style.configure("Treeview.insert" , font=(None , 50))

def success(nameEnt,cateEnt,colorEnt,sizeEnt,tpriceEnt,payrEnt,contactEnt,MNameEnt,MpriceEnt,shipEnt,TlpaidEnt):
    custom.writeDataCustomer(nameEnt,cateEnt,colorEnt,sizeEnt,tpriceEnt,payrEnt,contactEnt,MNameEnt,MpriceEnt,shipEnt,TlpaidEnt)
    nameEnt.delete(0,tkinter.END)
    cateEnt.delete(0,tkinter.END)
    colorEnt.delete(0,tkinter.END)
    sizeEnt.delete(0,tkinter.END)
    tpriceEnt.delete(0,tkinter.END)
    payrEnt.delete(0,tkinter.END)
    contactEnt.delete(0,tkinter.END)
    MNameEnt.delete(0,tkinter.END)
    MpriceEnt.delete(0,tkinter.END)
    shipEnt.delete(0,tkinter.END)
    TlpaidEnt.delete(0,tkinter.END)
    messagebox.showinfo('Success' , 'Data added successfully')

def cEntry():
    frame = tkinter.ttk.Frame(root)
    frame.place(x=50 , y= 50 , relheight=0.75 , relwidth=0.88)

    entries = custom.readDataCustomer()
    entryView = tkinter.ttk.Treeview(frame,height=18)
    entryView["columns"] = ("1", "2", "3","4", "5", "6","7")
    entryView.column("#0" ,width=50, minwidth=50)
    entryView.column("1" ,width=50, minwidth=50)
    entryView.column("2" ,width=50, minwidth=50)
    entryView.column("3" ,width=50, minwidth=50)
    entryView.column("4" ,width=50, minwidth=50)
    entryView.column("5" ,width=50, minwidth=50)
    entryView.column("6" ,width=50, minwidth=50)
    entryView.column("7" ,width=50, minwidth=50)
    entryView.heading("#0",text="Name", anchor=tkinter.W)
    entryView.heading("1",text="Category", anchor=tkinter.W)
    entryView.heading("2",text="Color", anchor=tkinter.W)
    entryView.heading("3",text="Size", anchor=tkinter.W)
    entryView.heading("4",text="Price", anchor=tkinter.W)
    entryView.heading("5",text="Payment Receieved", anchor=tkinter.W)
    entryView.heading("6",text="Payment Left", anchor=tkinter.W)
    entryView.heading("7",text="Contact", anchor=tkinter.W)
    for entry in entries:
        entryView.insert("" , 'end' , text=f'{entry[1]}' , values=(f'{entry[2]}' , f'{entry[3]}',f'{entry[4]}',f'{entry[5]}',f'{entry[6]}',f'{entry[7]}',f'{entry[8]}'))
    entryView.pack(fill = tkinter.X)
    cbtn = tkinter.ttk.Button(frame , text='Close',command=lambda : frame.destroy())
    cbtn.place(relx=0.5 , rely=0.9)

def add():
    frame = tkinter.ttk.Frame(root)
    frame.place(x=50 , y= 50 , relheight=0.6 , relwidth=0.88)

    nameLbl = tkinter.ttk.Label(frame , text="Enter customer name")
    nameEnt = tkinter.ttk.Entry(frame , width=25)
    nameLbl.place(relx=0.1 , rely=0.10)
    nameEnt.place(relx=0.22 , rely=0.10)

    cateLbl = tkinter.ttk.Label(frame , text="Enter order category")
    cateEnt = tkinter.ttk.Entry(frame , width=15)
    cateLbl.place(relx=0.1 , rely=0.18)
    cateEnt.place(relx=0.22 , rely=0.18)

    colorLbl = tkinter.ttk.Label(frame , text="Enter order colour")
    colorEnt = tkinter.ttk.Entry(frame , width=15)
    colorLbl.place(relx=0.1 , rely=0.25)
    colorEnt.place(relx=0.22 , rely=0.25)

    sizeLbl = tkinter.ttk.Label(frame , text="Enter order size")
    sizeEnt = tkinter.ttk.Entry(frame , width=8)
    sizeLbl.place(relx=0.1 , rely=0.33)
    sizeEnt.place(relx=0.22 , rely=0.33)

    tpriceLbl = tkinter.ttk.Label(frame , text="Enter total price")
    tpriceEnt = tkinter.ttk.Entry(frame , width=8)
    tpriceLbl.place(relx=0.1 , rely=0.41)
    tpriceEnt.place(relx=0.22 , rely=0.41)

    payrLbl = tkinter.ttk.Label(frame , text="Enter received payment")
    payrEnt = tkinter.ttk.Entry(frame , width=8)
    payrLbl.place(relx=0.1 , rely=0.49)
    payrEnt.place(relx=0.22 , rely=0.49)

    contactLbl = tkinter.ttk.Label(frame , text="Enter customer contact")
    contactEnt = tkinter.ttk.Entry(frame , width=15)
    contactLbl.place(relx=0.1 , rely=0.57)
    contactEnt.place(relx=0.22, rely=0.57)
    # merchant
    MNameLbl = tkinter.ttk.Label(frame , text="Enter merchant name")
    MNameEnt = tkinter.ttk.Entry(frame , width=25)
    MNameLbl.place(relx=0.5 , rely=0.10)
    MNameEnt.place(relx=0.65, rely=0.10)

    MpriceLbl = tkinter.ttk.Label(frame , text="Enter merchant price")
    MpriceEnt = tkinter.ttk.Entry(frame , width=10)
    MpriceLbl.place(relx=0.5 , rely=0.20)
    MpriceEnt.place(relx=0.65, rely=0.20)

    shipLbl = tkinter.ttk.Label(frame , text="Enter shipping amount")
    shipEnt = tkinter.ttk.Entry(frame , width=10)
    shipLbl.place(relx=0.5 , rely=0.30)
    shipEnt.place(relx=0.65, rely=0.30)

    TlpaidLbl = tkinter.ttk.Label(frame , text="Enter amount paid")
    TlpaidEnt = tkinter.ttk.Entry(frame , width=10)
    TlpaidLbl.place(relx=0.5 , rely=0.40)
    TlpaidEnt.place(relx=0.65, rely=0.40)

    addBtn = tkinter.ttk.Button(frame , text='Add Entry', command= lambda: success(nameEnt,cateEnt,colorEnt,sizeEnt,tpriceEnt,payrEnt,contactEnt,MNameEnt,MpriceEnt,shipEnt,TlpaidEnt))
    cancelBtn = tkinter.ttk.Button(frame , text='Cancel' , command=lambda :frame.destroy())
    addBtn.place(relx=0.5 , rely=0.60)
    cancelBtn.place(relx=0.65 , rely=0.60)

def mEntry():
    frame = tkinter.ttk.Frame(root)
    frame.place(x=50 , y= 50 , relheight=0.75 , relwidth=0.88)

    entries = custom.readDataMerchant()
    entryView = tkinter.ttk.Treeview(frame,height=18)
    entryView["columns"] = ("1", "2", "3","4", "5", "6","7","8","9")
    entryView.column("#0" ,width=30, minwidth=50)
    entryView.column("1" ,width=30, minwidth=50)
    entryView.column("2" ,width=30, minwidth=50)
    entryView.column("3" ,width=30, minwidth=50)
    entryView.column("4" ,width=30, minwidth=50)
    entryView.column("5" ,width=30, minwidth=50)
    entryView.column("6" ,width=30, minwidth=50)
    entryView.column("7" ,width=30, minwidth=50)
    entryView.column("8" ,width=30, minwidth=50)
    entryView.column("9" ,width=30, minwidth=50)
    entryView.heading("#0",text="Name", anchor=tkinter.W)
    entryView.heading("1",text="Order", anchor=tkinter.W)
    entryView.heading("2",text="Merchant Price", anchor=tkinter.W)
    entryView.heading("3",text="Colour", anchor=tkinter.W)
    entryView.heading("4",text="Size", anchor=tkinter.W)
    entryView.heading("5",text="Shipping", anchor=tkinter.W)
    entryView.heading("6",text="Total Price", anchor=tkinter.W)
    entryView.heading("7",text="Total Paid", anchor=tkinter.W)
    entryView.heading("8",text="Total Left", anchor=tkinter.W)
    entryView.heading("9",text="Ordered For", anchor=tkinter.W)
    for entry in entries:
        entryView.insert("" , 'end' , text=f'{entry[1]}' , values=(f'{entry[2]}' , f'{entry[3]}',f'{entry[4]}',f'{entry[5]}',f'{entry[6]}',f'{entry[7]}',f'{entry[8]}',f'{entry[9]}',f'{entry[10]}'))
    entryView.pack(fill = tkinter.X)
    cbtn = tkinter.ttk.Button(frame , text='Close',command=lambda : frame.destroy())
    cbtn.place(relx=0.5 , rely=0.9)

def checkProfit():
    frame = tkinter.ttk.Frame(root)
    frame.place(x=50 , y= 50 , relheight=0.25 , relwidth=0.25)
    actualP,currentP,leftPay = custom.checkProfit()
    if actualP == currentP :
        messagebox.showinfo("Profit" , f"Your total profit is {currentP}.\nAll the best for future.")
    else :
        messagebox.showerror("Loss" , f"Your total profit is {currentP}, but it should be {actualP}.\nYou have remaining balance of {leftPay}.")
    
def close():
   msg = messagebox.askyesnocancel('Exit' , 'Do you want to exit ?')
   if msg:
       root.destroy()
   else:
       return

# widgets
writeBtn = tkinter.ttk.Button(root, text='Add Entry' ,command=add)
cRecordBtn = tkinter.ttk.Button(root, text='Show all Customers Records',command=cEntry)
mRecordBtn = tkinter.ttk.Button(root , text='Show all Merchant Records' , command=mEntry)
profitBtn = tkinter.ttk.Button(root , text='Check Profit' , command=checkProfit)
closeBtn = tkinter.ttk.Button(root , text='Exit' , command=close)

writeBtn.place(x=100 , y=10)
cRecordBtn.place(x=250 , y=10)
mRecordBtn.place(x=500 , y=10)
profitBtn.place(x=750 , y=10)
closeBtn.place(x=920 , y=10)

root.mainloop()
