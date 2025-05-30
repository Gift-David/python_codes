# 
amount = float(input("Enter the total amount of purchase: "))

if amount >= 200:
    discount = (0.15 * amount)
elif 50 <= amount < 200:
    discount = (0.05 * amount)
else:
    discount = 0

final_amount = (amount - discount)

print(f"Original amount: ${amount}\nDiscount: ${discount}\nFinal amount: ${final_amount}")