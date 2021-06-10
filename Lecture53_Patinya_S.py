def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result
userInput = int(input("enter total price : "))
print(vatCalculate(userInput))