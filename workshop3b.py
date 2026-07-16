total = 0 
ร้านที่เก็บแล้ว = 0
shop = int(input("จำนวนร้าน: "))

for i in range(shop):
    money = int(input(f"ร้านที่{i+1}: "))
    while total < 50000:
        total = total + money
print(to