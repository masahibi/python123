# coding: utf-8


from numpy import sqrt, log, arange, sum, exp
from pandas import read_excel
from matplotlib.pyplot import figure, show

# 以下の2行は日本語表示を行う場合のフォント指定
import matplotlib.font_manager

fp = matplotlib.font_manager.FontProperties(fname='C:\WINDOWS\Fonts\msgothic.ttc', size=14)


def calc_regression_line(x_data, y_data):  # 回帰直線を求める関数 x_data：時刻、Y_data：温度
    """\
    回帰直線を求める関数．
    x_data：時刻 t
    y_data：測定温度-室温 <- g(t)
    戻り値：傾き、切片の値\
    """

    number_of_data = x_data.shape[0]

    # x軸(時刻)の平均と分散を計算
    x_average = sum(x_data) / number_of_data
    x_std = sqrt((sum((x_data - x_average) ** 2) / number_of_data))
    # y軸(温度)の平均と分散を計算
    y_average = sum(y_data) / number_of_data
    y_std = sqrt((sum((y_data - y_average) ** 2) / number_of_data))

    # 共分散を求める
    covariance = sum((x_data - x_average) * (y_data - y_average)) / number_of_data

    # 相関係数を求める <--相関係数の意味を考え、レポートに加えると良い。
    # 相関係数値は、実験から得られた結果=事実、それを根拠に何を考察するか?
    r = covariance / (x_std * y_std)
    print('相関係数=', r)

    # 回帰直線の傾きと切片を求める
    # 計算式
    a = (number_of_data * sum(x_data * y_data) - sum(x_data) * sum(y_data)) / \
        (number_of_data * sum(x_data ** 2) - (sum(x_data)) ** 2)
    b = y_average - a * x_average

    return a, b


# pandasでのエクセルファイル読み込み
fname = "ex1.xlsx"
sname = 'Sheet1'
dataframe = read_excel(fname, sheet_name=sname)
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

# 測定値から室温を引く
temperature1 = values[:, 1] - ROOMTEMPERATURE
temperature2 = values[:, 2] - ROOMTEMPERATURE
temperature3 = values[:, 3] - ROOMTEMPERATURE

# 作図
# 参考：https://qiita.com/tsuruokax/items/90167693f142ebb55a7d

fig = figure(figsize=(8, 6))  # グラフ用のfigure領域を確保
ax = fig.add_subplot(1, 1, 1)  # グラフ用のplot領域を確保

# 測定点をプロットする。ラベルを文字列で指定する場合は、label=”文字列” とする。
ax.plot(time, temperature1, 'bo', label=dataframe_label[1][:])  # 実験条件に応じたラベル名を記入すること
ax.plot(time, temperature2, 'gx', label=dataframe_label[2][:])  # 実験条件に応じたラベル名を記入すること
ax.plot(time, temperature3, 'r^', label=dataframe_label[3][:])  # 実験条件に応じたラベル名を記入すること

# 図のタイトルを下に表示するのは難しいのでグラフを貼り付けた後に別途記入しましょう。
# ax.set_title('保温ビーカの温度変化', fontproperties=fp)

# 回帰直線の値を元に指数関数で換算してあるので、片対数グラフを指定する。
ax.set_yscale('log')
ax.grid(which='both')

ax.set_yticks(arange(3.5, 4.5, 0.2))  # 全ての測定点が入る範囲を指定し、目盛間隔を指定する(最小値、最大値、間隔)

ax.set_xlabel('経過時間(秒)', fontproperties=fp)
ax.set_ylabel('(測定温度－ 室温)(℃)', fontproperties=fp)  # y軸は、logを求めた後に表示しているのでその旨の表示を行う

# 回帰直線の計算と表示
# 回帰直線を求めるためにlog{g(t)}を計算しておく。
temperature1_log = log(temperature1)
temperature2_log = log(temperature2)
temperature3_log = log(temperature3)

# 同じ計算を繰り返すので、関数を用いて回帰直線の傾き(a)と切片(b)を求める
a, b = calc_regression_line(time, temperature1_log)
# print(a,b)
ax.plot(time, exp(time * a + b), 'b')

a, b = calc_regression_line(time, temperature2_log)
# print(a,b)
ax.plot(time, exp(time * a + b), 'g')

a, b = calc_regression_line(time, temperature3_log)
# print(a,b)
ax.plot(time, exp(time * a + b), 'r')

# 凡例を有効化
ax.legend(prop=fp)
show()
