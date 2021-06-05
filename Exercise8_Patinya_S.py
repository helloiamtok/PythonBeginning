"""
Patinya Sribrowornnara
5/6/2564 19:36 น.

เขียนโปรแกรมร้านขายของโดยดัดแปลงจากโปรแกรมใน Lecture 40
ในการเข้าใช้งานโปรแกรมให้ผู้ล็อคอินโดยใช้ Username และ Password(ผู้เรียนกำหนดเอง) #INPUT
หากสำเร็จ โปรแกรมจะขึ้นหน้าต้อนรับและแสดงรายการสินค้าพร้อมราคา (ผู้เรียนกำหนดเอง)
เมื่อเลือกสินค้าที่ต้องการเรียบร้อยแล้ว โปรแกรมจะถามจำนวนที่ต้องการซื้อ #PROCESS
หลังจากผู้ซื้อเลือกเรียบร้อยแล้ว โปรแกรมจะทำการแสดงสรุปราคารวมของรายการสั่งซื้อทั้งหมด #OUTPUT

"""

print ("---------- Welcome to Tok Family Shop ---------- \nSystem : Please Enter Username and Password to place an order\n------------------------------------------------")
usernameInput = input("username : ")
passwordInput = input("password : ")

if usernameInput == "admin" and passwordInput == "123456" :
    print ("Welcome : ",usernameInput)

    print ("Welcome to Stock Oroder Please Selected 1 item")
    product1 = ("1.Cola    30 (THB)")
    product2 = ("2.Toffy   15 (THB)")
    product3 = ("3.Popcorn 25 (THB)")
    product4 = ("4.Smoking 50 (THB)")

    print (product1)
    print (product2)
    print (product3)
    print (product4)



    selected = int(input ("Please Enter Number Product 1,2,3 or 4 : "))
    if   selected == 1 :
        print ("you choose the product : 1.Cola 30 (THB)")
        amount = int(input("please enter your amount : "))
        print ("you choose the product : 1.Cola 30 (THB) : ",amount,"piece")
        price = amount * 30
        print ("total price : ",price,"THB")


    elif selected == 2 :
        print ("you choose the product : 2.Toffy 15 (THB)")
        amount = int(input("please enter your amount : "))
        print ("you choose the product : 2.Toffy 15 (THB) : ",amount,"piece")
        price = amount * 15
        print ("total price : ",price,"THB")



    elif selected == 3 :
        print ("you choose the product : 3.Popcorn 25 (THB)")
        amount = int(input("please enter your amount : "))
        print ("you choose the product : 3.Popcorn 25 (THB) : ",amount,"piece")
        price = amount * 25
        print ("total price : ",price,"THB")



    elif selected == 4:
        print ("you choose the product :  4.Smoking 50 (THB)")
        amount = int(input("please enter your amount : "))
        print ("you choose the product :  4.Smoking 50 (THB) : ",amount,"piece")
        price = amount * 50
        print ("total price : ",price,"THB")


    else :
        print ("You did not select the product")

else:
    print("System : invalid username or password please try again")