# 問題1
def map_square(values):    # リストの要素を2乗したリスト
    result = []
    for x in values:
        result.append(x ** 2)
    return result


v = [1, 2, -1, -2]
print(map_square(v))


# 問題2
def filter_positive(values):    # リストの正の要素のリスト
    result = []
    for x in values:
        if x >= 0:
            result.append(x)
    return result


v = [1, 2, -1, -2]
print(filter_positive(v))


# 問題3
def fold_plus(values):    # 要素の和を求める
    result = 0
    for x in values:
        result += x
    return result


v = [1, -2, 3, -4, 5]
result = fold_plus(map_square(v))
print(f"result = {result}")


# 問題4
v = [1, -2, 3, -4, 5]
result = fold_plus(filter_positive(v))
print(f"result = {result}")
