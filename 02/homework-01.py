apple_price = 100
orange_price = 200
grape_price =300
tax = 0.08

a_total_price = apple_price*1 + orange_price*2 + grape_price*3    #1400
b_total_price = apple_price*0 + orange_price*2 + grape_price*3    #1300
c_total_price = apple_price*2 + orange_price*4 + grape_price*0    #1000

a_tax_price = a_total_price * (1 + tax)    #1512
b_tax_price = b_total_price * (1 + tax)    #1404
c_tax_price = c_total_price * (1 + tax)    #1080

print(f"Aさん；税別:{a_total_price}円, 税込:{a_tax_price:.0f}円")
print(f"Bさん；税別:{b_total_price}円, 税込:{b_tax_price:.0f}円")
print(f"Cさん；税別:{c_total_price}円, 税込:{c_tax_price:.0f}円")
#


