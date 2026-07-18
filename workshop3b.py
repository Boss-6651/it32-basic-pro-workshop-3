total = 0 
ร้านที่เก็บแล้ว = 0
target_money = int(input("Enter money: "))

while True:
    if total < 50000:
        income_money = int(input("Enter income money: "))
        total += income_money
        ร้านที่เก็บแล้ว += 1

    else:
        break

print(f"สรุปเก็บเงินไปทั้งหมด {total} เก็บไป {ร้านที่เก็บแล้ว} ร้าน")


