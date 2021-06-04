number1 = 10
number2 = 2

addition    = number1 + number2
minus       = number1 - number2
subtraction = number1 * number2
divide      = number1 / number2

print (number1,"+",number2,"=",addition)
print (number1,"-",number2,"=",minus)
print (number1,"*",number2,"=",subtraction)
print (number1,"/",number2,"=",divide)

"""

10 + 2 = 12
10 - 2 = 8
10 * 2 = 20
10 / 2 = 5


ข้อนี้ผมคิดว่าโจทย์ผลลัพธ์ที่ได้จากการหารคือ 5 ผิด ถูกจะเป็น 5.0 (ไม่แน่ใจอาจจะวางบัคไว้หรือเปล่า)
หากนำไปหารกันไม่ว่าการประเภทข้อมูลจะเป็นชนิด integer หรือ float 
ผลลัพธ์จะออกมาได้เป็น float ตามที่พี่เปรมได้เคยอธิบายไว้ใน EP ก่อนในเรื่องของตัว Operator
"""
