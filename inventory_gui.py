import tkinter
from tkinter import ttk , messagebox
import custom


root = tkinter.Tk()
root.title('Inventory')
root.geometry("1300x650")

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
    frame.place(x=50 , y= 50 , relheight=0.6 , relwidth=0.88)

    entries = custom.readDataCustomer()
    resultBox = tkinter.Text(frame , width=800 , height=200)
    resultBox.grid(row=2 , column=0 , columnspan=2 , pady=10)
    resultBox.insert(tkinter.END , "\tCustomer\t\tCategory\t\tColour\t\tSize\t\tTotal Price\t\tPayment Received\t\tPayment Left\t\t\tContact\n\n")
    for entry in entries:
        resultBox.insert(tkinter.END , f"\t{entry[1]}\t\t{entry[2]}\t\t{entry[3]}\t\t{entry[4]}\t\t{entry[5]}\t\t{entry[6]}\t\t\t{entry[7]}\t\t{entry[8]}\n")
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
    frame.place(x=50 , y= 50 , relheight=0.6 , relwidth=0.95)

    entries = custom.readDataMerchant()
    resultBox = tkinter.Text(frame , width=800 , height=200)
    resultBox.grid(row=2 , column=0 , columnspan=2 , pady=10)
    resultBox.insert(tkinter.END , "Customer\t\tCategory\t\tPrice\t\tColour\t\tSize\t\tShipping\t\tTotal Price\t\tTotal Paid\t\tTotal Left\t\tCustomer\n\n")
    for entry in entries:
        resultBox.insert(tkinter.END , f"{entry[1]}\t\t{entry[2]}\t\t{entry[3]}\t\t{entry[4]}\t\t{entry[5]}\t\t{entry[6]}\t\t{entry[7]}\t\t{entry[8]}\t\t{entry[9]}\t\t{entry[10]}\n")
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

writeBtn.grid(row=0 , column=0 , padx=5,pady=5 )
cRecordBtn.grid(row=0 , column= 1 , padx=20 , pady=5)
mRecordBtn.grid(row=0 , column=2 , padx=5, pady=5)
profitBtn.grid(row=0 , column=3 , padx=20, pady=5)
closeBtn.grid(row=0 , column=4 , padx=5, pady=5)

root.mainloop()
