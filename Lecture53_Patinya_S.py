userInput = int(input("Enter Pirce : ")) #รับ input เข้ามาจากผู้ใช้โดยจะต้องเป็น int แต่เดิมเป็น str เพื่อนำไปคำนวณต่อไป
def vat (totalprice) : #สร้างฟังก์ชั่น
    result = totalprice+(totalprice*7/100) #ประมวลผลสูตรค่าคำตอบ
    return int(result) #คำตอบที่เก็บไว้ในตัวแปร result หลังจาก return ค่ากลับมาแล้วจะเป็น float ต้องการแปลงเป็น int โดยใส่ int () ครอบตัวแปรไว้
print ("All Price + Vat : ",vat(userInput)) #ปริ้นข้อความออกมา