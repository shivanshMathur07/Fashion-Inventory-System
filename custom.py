import sqlite3

def newDB():
    dbc = sqlite3.connect('custom.db')
    query=''' CREATE TABLE customers (
    [C-Id]             INTEGER      PRIMARY KEY AUTOINCREMENT,
    Name               CHAR (30)    NOT NULL,
    Category           CHAR (30)    NOT NULL,
    Colour             CHAR (20)    NOT NULL,
    Size               VARCHAR (10) NOT NULL
                                    DEFAULT None,
    Price              INT (10)     NOT NULL,
    [Payment Received] INT (10),
    [Payment Left]     INT (10),
    Contact            NUMERIC (11) 
    ) '''

    dbc.execute(query)

    query = ''' CREATE TABLE Merchant (
    Id               INTEGER      PRIMARY KEY AUTOINCREMENT,
    Name             CHAR (25)    NOT NULL,
    [Order Name]     CHAR (30)    NOT NULL,
    [Merchant Price] INTEGER (10) NOT NULL,
    Colour           CHAR (20)    NOT NULL,
    Size             VARCHAR (10) NOT NULL,
    Shipping         INTEGER (10),
    [Total Price]    INTEGER (10) NOT NULL
                                  DEFAULT (0),
    [Total Paid]     INTEGER (10) DEFAULT (0),
    [Total Left]     INTEGER (10),
    [Order For]      CHAR (30)    DEFAULT [No Name]
                                  NOT NULL
)'''

    dbc.execute(query)

def writeDataCustomer(nameEnt, cateEnt, colorEnt, sizeEnt, tpriceEnt, payrEnt, contactEnt, MNameEnt, MpriceEnt, shipEnt, TlpaidEnt, ):
    dbc = sqlite3.connect('custom.db')
    name = nameEnt.get()
    cat = cateEnt.get()
    color = colorEnt.get()
    size = sizeEnt.get()
    price = int(tpriceEnt.get())
    pay_r = int(payrEnt.get())
    contact = int(contactEnt.get())
    pay_l = price - pay_r
    dbc.execute(''' INSERT INTO customers(Name,Category,Colour,Size,Price,'Payment Received','Payment Left',Contact)
        VALUES(?,?,?,?,?,?,?,?)''', (name, cat, color, size, price, pay_r, pay_l, contact))

    dbc.commit()
    Mname = MNameEnt.get()
    price = int(MpriceEnt.get())
    shipping = int(shipEnt.get())
    total_paid = int(TlpaidEnt.get())
    total_price = price+shipping
    total_left = total_price - total_paid

    writeDataMerchant(Mname , cat , price , color , size , shipping , total_price , total_paid , total_left , name)
    dbc.close()

def readDataCustomer():
    dbc = sqlite3.connect('custom.db')
    return(dbc.execute(''' SELECT * FROM customers '''))
    

def writeDataMerchant(name, order, price, colour, size, shipping, total_price, total_paid, total_left, cusName):
    dbc = sqlite3.connect('custom.db')
    dbc.execute(''' INSERT INTO merchant(Name,'Order Name','Merchant Price',Colour,Size,Shipping,'Total Price','Total Paid','Total Left','Order For')
        VALUES(?,?,?,?,?,?,?,?,?,?)''', (name, order, price, colour, size, shipping, total_price, total_paid, total_left, cusName))

    dbc.commit()
    dbc.close()
    return


def readDataMerchant():
    dbc = sqlite3.connect('custom.db')
    return(dbc.execute(''' SELECT * FROM merchant '''))

def checkProfit():
    dbc = sqlite3.connect('custom.db')
    totalCost = 0
    totalPayR = 0
    totalPayL = 0
    dataM = dbc.execute(''' SELECT ("Merchant Price") FROM merchant ''')
    for d in dataM:
        totalCost += int(d[0])
    dataC = dbc.execute(
        ''' SELECT ("Payment Received"),("Payment Left") FROM customers ''')
    for d in dataC:
        totalPayR += d[0]
        totalPayL += d[1]
    actualProfit = (totalPayR+totalPayL) - totalCost
    currentProfit = totalPayR - totalCost
    dbc.close()
    return(actualProfit,currentProfit,totalPayL)

