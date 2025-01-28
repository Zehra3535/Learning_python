item = input("What idem would you like to buy? =")
price = float(input("What's the price? ="))
quantity = int(input(f"How many would you like?"))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}")
# Virgülden sonraki iki basamağı yuvarlayarak yazacak
# float degerin çok uzun çıkmaması için yuvarlama(round) fonksiyonunu kullandık.
