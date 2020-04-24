import sqlite3

# defining connection
db = sqlite3.connect('custom.db')

def writeDataCustomer(name , cat , color , price , pay_r , pay_l , contact):
    db.execute(''' INSERT INTO customers(Name,Category,Colour,Price,'Payment Received','Payment Left',Contact)
        VALUES(?,?,?,?,?,?,?)''',(name , cat , color , price , pay_r , pay_l , contact))

    db.commit()
def readDataCustomer():
    return(db.execute(''' SELECT * FROM customers '''))

# taking input entries
run = True
while(run):
    print('''(1).Add new order entry\n(2)Add new merchant entry\n(3).To check profit\n(4)Add a note\n(5)View all customer records\n(6)Exit''')
    ch = int(input('Enter your choice :'))
    # to add new order
    if ch == 1:
        name = input('Enter the name of customer :')
        order_cat = input('Enter the category of order :')
        order_col = input('Enter the colour of order :')
        order_price = int(input('Price :'))
        pay_r = int(input('Payment Received :'))
        pay_left = order_price - pay_r
        contact = int(input('Enter the contact number of customer :'))
        writeDataCustomer(name,order_cat,order_col,order_price,pay_r,pay_left,contact)
    # to add new merchant entry
    elif ch == 2 :
        pass
    elif ch == 3 :
        pass
    elif ch == 4 :
        pass
    elif ch == 5 :
        data = readDataCustomer()
        for entry in data:
            print(f'Id: {entry[0]}\nName: {entry[1]}\nCategory: {entry[2]}\nColor: {entry[3]}\nPrice: {entry[4]}\nPay Received: {entry[5]}\nPay Left: {entry[6]}\nContact: {entry[7]}\n\n')          
    elif ch == 6 :
        run = False
        db.close()
    else:
        print('Sorry wrong input choice !\nTry again.')

