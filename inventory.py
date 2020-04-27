import sqlite3

# defining connection
db = sqlite3.connect('custom.db')
# to add database
def writeDataCustomer(name , cat , color , price , pay_r , pay_l , contact):
    db.execute(''' INSERT INTO customers(Name,Category,Colour,Price,'Payment Received','Payment Left',Contact)
        VALUES(?,?,?,?,?,?,?)''',(name , cat , color , price , pay_r , pay_l , contact))

    db.commit()
# to read database
def readDataCustomer():
    return(db.execute(''' SELECT * FROM customers '''))

# merchant database
def writeDataMerchant(name ,order , price , colour , size , shipping ,total_price, total_paid, total_left):
    db.execute(''' INSERT INTO merchant(Name,'Order Name','Merchant Price',Colour,Size,Shipping,'Total Price','Total Paid','Total Left')
        VALUES(?,?,?,?,?,?,?,?,?)''',(name,order,price, colour , size , shipping ,total_price, total_paid,total_left))

    db.commit()

def readDataMerchant():
    return(db.execute(''' SELECT * FROM merchant '''))

def checkProfit():
    totalCost = 0
    totalPayR = 0
    totalPayL = 0
    dataM = db.execute(''' SELECT ("Merchant Price") FROM merchant ''')
    for d in dataM:
        totalCost += int(d[0])
    dataC = db.execute(''' SELECT ("Payment Received"),("Payment Left") FROM customers ''')
    for d in dataC:
        totalPayR += d[0]
        totalPayL += d[1]
    np = db.execute(''' SELECT Name FROM customers WHERE ("Payment Left")>0 ''')
    actualProfit = (totalPayR+totalPayL) - totalCost
    currentProfit = totalPayR - totalCost
    if actualProfit == currentProfit:
        print(f'Your profit is Rs{actualProfit}.All the best for your future work.')
    else:
        print(f'Your current profit is Rs{currentProfit} but it should be Rs{actualProfit}.You have pending payment of Rs{totalPayL}.Customers who have payment left are :-\n')
        for c in np:
            print(f'{c[0]}')
        print('\n')


# taking input entries
run = True
while(run):
    print('''(1).Add new order entry\n(2).To check profit\n(3)Add a note\n(4)View all customer records\n(5)View merchant records\n(6)Exit''')
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
        name = input('Enter the name of merchant :')
        orderName = input('Enter the name of order :')
        mprice = int(input('Enter the price of order from merchant :'))
        color = input('Enter the colour of order :')
        size = (input('Size of order :'))
        shipping = int(input("Enter the shipping charges :"))
        tprice = mprice + shipping
        print(f'Total price is :{tprice}')
        tpaid =int(input("Enter total amount paid :"))
        tleft = tprice - tpaid
        writeDataMerchant(name,orderName,mprice,color,size,shipping,tprice,tpaid,tleft)
    elif ch == 2 :
        checkProfit()
    elif ch == 3 :
        pass
    elif ch == 4 :
        data = readDataCustomer()
        for entry in data:
            print(f'Id: {entry[0]}\nName: {entry[1]}\nCategory: {entry[2]}\nColor: {entry[3]}\nPrice: {entry[4]}\nPay Received: {entry[5]}\nPay Left: {entry[6]}\nContact: {entry[7]}\n\n')          
    elif ch == 5:
        data = readDataMerchant()
        for entry in data:
            print(f'Id: {entry[0]}\nName: {entry[1]}\nOrder Name: {entry[2]}\nMerchant Price: {entry[3]}\nColour: {entry[4]}\nSize: {entry[5]}\nShipping: {entry[6]}\nTotal Price: {entry[7]}\nTotal Paid: {entry[8]}\nTotal Left: {entry[9]}\n\n')
    elif ch == 6 :
        run = False
        db.close()
    else:
        print('Sorry wrong input choice !\nTry again.')

