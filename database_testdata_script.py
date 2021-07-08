import random

from nltk.corpus import words

allWords = words.words()

def add_borrowed(borrowed, i):
    memberid = random.randint(1, 1000)
    year = random.randint(2015, 2021)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    f.write("insert into borrowed (bookid, memberid, dueDate, returned) values ({}, {}, '{}-{}-{}', {});\n".format(str(i), str(memberid), str(year), str(month), str(day), borrowed))

with open("testdata.sql", "a") as f:
    statuses = ["available", "borrowed", "deleted"]
    conditions = ["new", "used", "bad"]
    isbns = []

    for i in range(100):
        isbn = "".join(str(random.randint(0, 9)) for i in range(13))
        title = random.choice(allWords) + random.choice(allWords) + random.choice(allWords)
        authour_name = random.choice(allWords)
        authour_surname = random.choice(allWords)
        f.write("insert into bookinfo (isbn, title, authorname, authorsurname) values ("
                + isbn + ", '" + title + "', '" + authour_name + "', '" + authour_surname + "');\n")
        isbns.append(isbn)

    for i in range(1000):
        name = random.choice(allWords)
        surname = random.choice(allWords)
        f.write("insert into member (name, surname) values ('"
                + name + "', '" + surname + "');\n")

    for i in range(1000):
        isbn = random.choice(isbns)
        status = random.choice(statuses)
        condition = random.choice(conditions)
        f.write("insert into book (isbn, bookstatus, bookcondition) values ("
                + isbn + ", '" + status + "', '" + condition + "');\n")

        if status == "borrowed":
           add_borrowed('false', i + 1)

        elif status == "deleted":
            reason = random.choice(allWords) + random.choice(allWords) + random.choice(allWords)
            f.write("insert into deletedreasons (bookid, reason) values (" +
                str(i + 1) + ", '" + reason + "');\n")

        else:
            if random.random() < 0.5:
                add_borrowed('true', i + 1)


    # for i in range(100):
    #     types = ["InStore", "Collection", "Delivery"]
    #     months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    #     orderType = types[random.randint(0,2)]
    #     orderCompleted = random.randint(0,1)
    #     if (orderType == "InStore"):
    #         orderCompleted = 1
    #     staffid = random.randint(1, 6)
    #     productid = random.randint(0, 99)  
    #     dateStr = "{}{}-{}-{}{}"
    #     firstDigit = random.randint(0,2)
    #     secondDigit = 0

    #     if firstDigit < 2:
    #         secondDigit = random.randint(0,9)
    #     orderDate = dateStr.format(random.randint(0,2), random.randint(1,9), months[random.randint(0,11)], firstDigit, secondDigit)

    #     f.write("insert into orders (orderid, ordertype, ordercompleted, orderplaced) values (" 
    #             + str(i) + ", '" + orderType + "', " + str(orderCompleted) + ", '" + orderDate + "');\n")
    #     f.write("insert into staff_orders (staffid, orderid) values (" + str(staffid) + ", " + str(i) + ");\n")  

    #     f.write("insert into order_products (orderid, productid, productquantity) values (" + str(i) + ", " + str(productid) + ", " + str(random.randint(1,50)) + ");\n")  

    #     if orderType == "Delivery":
    #         deliveryDate = dateStr.format(random.randint(0,2), random.randint(1,9), months[random.randint(0,11)], firstDigit, secondDigit)
    #         f.write("insert into deliveries (orderid, fname, lname, house, street, city, deliverydate) values (" 
    #                 + str(i) + ", " + "'Bob', 'Bob', 1, 'Street', 'London', '" + deliveryDate + "');\n")   

    #     if orderType == "Collection":
    #         deliveryDate = dateStr.format(random.randint(0,2), random.randint(1,9), months[random.randint(0,11)], firstDigit, secondDigit)
    #         f.write("insert into collections (orderid, fname, lname, collectiondate) values (" 
    #                 + str(i) + ", " + "'Bob', 'Bob', '" + deliveryDate + "');\n")                       