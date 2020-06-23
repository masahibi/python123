# coding: utf-8

# 回帰直線を求めるプログラム
# 回帰直線の傾き、切片の算出
# 結果を真数グラフにプロット

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 以下の2行は日本語表示を行う場合のフォント指定
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname='C:\WINDOWS\Fonts\msgothic.ttc', size=14)


# ----> ここから回帰直線を求める関数
def calc_regression_line(x_data, y_data):  # 回帰直線を求める関数 x_data：時刻、Y_data：温度
    '''\
    回帰直線を求める関数．

x_data：時刻 t

y_data：測定温度-室温 <- g(t)


    戻り値：傾き、切片の値\

'''

    a = b = 0
    number_of_data = x_data.shape[0]

    # x軸(時刻)の平均と分散を計算
    x_average = np.sum(x_data) / number_of_data
    x_std = np.sqrt((np.sum((x_data - x_average) ** 2) / number_of_data))
    # y軸(温度)の平均と分散を計算
    y_average = np.sum(y_data) / number_of_data
    y_std = np.sqrt((np.sum((y_data - y_average) ** 2) / number_of_data))

    # 共分散を求める
    covariance = np.sum((x_data - x_average) * (y_data - y_average)) / number_of_data

    # 相関係数を求める <--相関係数の意味を考え、レポートに加えると良い。
    # 相関係数値は、実験から得られた結果=事実、それを根拠に何を考察するか?
    r = covariance / (x_std * y_std)
    print('相関係数=', r)

    # 回帰直線の傾きと切片を求める
    # 計算式
    a = (number_of_data * np.sum(x_data * y_data) - np.sum(x_data) * np.sum(y_data)) / \
        (number_of_data * np.sum(x_data ** 2) - (np.sum(x_data)) ** 2)
    b = y_average - a * x_average

    return a, b


# <----関数はここまで

# pandasでのエクセルファイル読み込み
fname = 'C:OneDrive\デスクトップ\Graph_Python_Moodle用\ex1.xlsx'
sname = 'Sheet1'
dataframe = pd.read_excel(fname, sheetname=sname)
# print(dataframe)
# type(dataframe)

values = dataframe.values
# print(values)
# type(values)

# 時刻、実験条件など1行目の読出し
dataframe_label = dataframe.columns

# 室温の設定
ROOMTEMPERATURE = 24.0

time = values[:, 0]
# 回帰直線をプロットするので、通常の真数グラフにプロットする
# そのため、計測値のlogを求めて、その値を使用する
temperature1 = np.log(values[:, 1] - ROOMTEMPERATURE)
temperature2 = np.log(values[:, 2] - ROOMTEMPERATURE)
temperature3 = np.log(values[:, 3] - ROOMTEMPERATURE)

# 作図
# 参考：https://qiita.com/tsuruokax/items/90167693f142ebb55a7d

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)

# 測定点をプロットする。ラベルを文字列で指定する場合は、label=”文字列” とする。
ax.plot(time, temperature1, 'bo', label=dataframe_label[1][:])  # 実験条件に応じたラベル名を記入すること
ax.plot(time, temperature2, 'gx', label=dataframe_label[1][:])  # 実験条件に応じたラベル名を記入すること
ax.plot(time, temperature3, 'r^', label=dataframe_label[1][:])  # 実験条件に応じたラベル名を記入すること

# 図のタイトルを下に表示するのは難しいのでグラフを貼り付けた後に別途記入しましょう。
# ax.set_title('保温ビーカの温度変化', fontproperties=fp)

# 片対数のグラフではないので、'log'は設定しない。
# ax.set_yscale('log')
ax.grid(which='both')

ax.set_yticks(np.arange(3.5, 4.5, 0.2))  # 全ての測定点が入る範囲を指定し、目盛間隔を指定する(最小値、最大値、間隔)

ax.set_xlabel('経過時間(秒)', fontproperties=fp)  # MSゴシックを使いようにfontproperties を設定
ax.set_ylabel('log(測定温度－ 室温)(℃)', fontproperties=fp)  # y軸は、logを求めた後に表示しているのでその旨の表示を行う

# 回帰直線の計算と表示
# 同じ計算を繰り返すので、回帰直線の傾き(a)と切片(b)を求める

a, b = calc_regression_line(time, temperature1)
# print(a,b)
ax.plot(time, time * a + b, 'b')

a, b = calc_regression_line(time, temperature2)
# print(a,b)
ax.plot(time, time * a + b, 'g')

a, b = calc_regression_line(time, temperature3)
# print(a,b)
ax.plot(time, time * a + b, 'r')

# 凡例を有効化
ax.legend(prop=fp)
plt.show()
