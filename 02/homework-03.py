fruits = ["りんご  ", "オレンジ", "ぶどう  "]
price = [100, 200, 300]

print("(1)")
print(f"品目:{fruits[0]} ; 単価:{price[0]}円")
print(f"品目:{fruits[1]} ; 単価:{price[1]}円")
print(f"品目:{fruits[2]} ; 単価:{price[2]}円")

'-------------------------------------------------------------------------------'
print()
print("(2)")
tax = 0.08
a_total_price = price[0]*1 + price[1]*2 + price[2]*3    #1400
b_total_price = price[0]*0 + price[1]*2 + price[2]*3    #1300
c_total_price = price[0]*2 + price[1]*4 + price[2]*0    #1000

a_tax_price = a_total_price * (1 + tax)    #1512
b_tax_price = b_total_price * (1 + tax)    #1404
c_tax_price = c_total_price * (1 + tax)    #1080

print(f"Aさん；税別:{a_total_price}円, 税込:{a_tax_price:.0f}円")
print(f"Bさん；税別:{b_total_price}円, 税込:{b_tax_price:.0f}円")
print(f"Cさん；税別:{c_total_price}円, 税込:{c_tax_price:.0f}円")







