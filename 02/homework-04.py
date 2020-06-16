fruits = ["りんご  ", "オレンジ", "ぶどう  "]
fruits_price = {"apple":100, "orange":200, "grape":300}

print("(1)")
print(f"品目:{fruits[0]} ; 単価:{fruits_price['apple']}円")
print(f"品目:{fruits[1]} ; 単価:{fruits_price['orange']}円")
print(f"品目:{fruits[2]} ; 単価:{fruits_price['grape']}円")

'-------------------------------------------------------------------------------'
print()
print("(2)")
tax = 0.08
a_total_price = fruits_price["apple"]*1 + fruits_price["orange"]*2 + fruits_price["grape"]*3    #1400
b_total_price = fruits_price["apple"]*0 + fruits_price["orange"]*2 + fruits_price["grape"]*3    #1300
c_total_price = fruits_price["apple"]*2 + fruits_price["orange"]*4 + fruits_price["grape"]*0    #1000

a_tax_price = a_total_price * (1 + tax)    #1512
b_tax_price = b_total_price * (1 + tax)    #1404
c_tax_price = c_total_price * (1 + tax)    #1080

print(f"Aさん；税別:{a_total_price}円, 税込:{a_tax_price:.0f}円")
print(f"Bさん；税別:{b_total_price}円, 税込:{b_tax_price:.0f}円")
print(f"Cさん；税別:{c_total_price}円, 税込:{c_tax_price:.0f}円")

'-------------------------------------------------------------------------------'

"""
（３）
キー（例:上記の"apple"）と、値（例:上記の100）を１組のペアとして格納しておく事ができ、キーを指定する事でそれに対応する値を取得することができるものを辞書という。
"""
