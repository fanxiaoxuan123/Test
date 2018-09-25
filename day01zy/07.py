amount=eval(raw_input(">>"))
z=0
for x in range(6):
    amount=amount*(1+0.00417)
    z=z+amount
z=round(z,2)
print(z)
