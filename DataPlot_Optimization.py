import pandas as pd
import matplotlib.pyplot as plt

# エクセルファイルからデータを読み込む
excel_file = "C:\\Users\\eitat\\OneDrive\\ドキュメント\\取り込み用_新電力密度.xlsx"  # ファイル名を適切なものに変更する
df = pd.read_excel(excel_file)

# 電池A、B、Cそれぞれのデータを抽出
# 電圧列を0~0.65 Vまででフィルタリングして抽出
battery_A = df[(df['電圧'] >= 0) & (df['電圧'] <= 0.65)].reset_index(drop=True)
battery_B = df[(df['電圧'] >= 0) & (df['電圧'] <= 0.65)].reset_index(drop=True)
battery_C = df[(df['電圧'] >= 0) & (df['電圧'] <= 0.65)].reset_index(drop=True)

# グラフを描画する
plt.plot(battery_A['電圧'], battery_A['電力密度'], label='Initial')
plt.plot(battery_B['電圧'], battery_B['電力密度'], label='After Topology Optimization')
plt.plot(battery_C['電圧'], battery_C['電力密度'], label='After Shape Optimization')

# グラフのタイトルとラベルを設定
plt.xlabel("Applied Voltage [V]")
plt.ylabel("Maximum Power Density [uW/cm2]")

# 凡例を表示
plt.legend()

# 日本語フォントの設定
plt.rcParams['font.family'] = 'IPAexGothic'

# グラフを表示
plt.show()