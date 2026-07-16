total = 0
shop = int(input("shop: "))
for i in range(shop):
    money = int(input(f"เก็บเงินร้านที่{i+1}: "))
    total = money + total  # total += money
    
print(total)