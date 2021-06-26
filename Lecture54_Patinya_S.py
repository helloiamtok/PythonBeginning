def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "root" and passwordInput == "admin":
        print ("Welcome : ",usernameInput)
        return showMenu()
    else :
        print ("Invalid username or password please try againt")
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input("Selected 1 or 2 : "))
    if userSelected == 1 :
        return vatCalculator()
    elif userSelected == 2 :
        return priceCalculator()
    else :
        print ("No More Option")
        return menuSelect()

def vatCalculator():
    totalPrice = int(input("Enter total Price : "))
    vat = 7
    result = (totalPrice) + (totalPrice * vat / 100)
    print ("Total Price + Vat : ", int(result))
    userInput = input("Do you want to continues y/n : ")
    if userInput == "y" :
        return showMenu()
    elif userInput == "n" :
        return login()
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    result = (price1+price2) + ((price1+price2)*7/100)
    print (int(result))
    userInput = input("Do you want to continues y/n : ")
    if userInput == "y" :
        return showMenu()
    elif userInput == "n" :
        return login()


login()