#import部分
import matplotlib
import pandas as pd
matplotlib.use('tkagg')
import matplotlib.pyplot as plt

#フォント日本語可能にする
matplotlib.rc('font', **{'family':'Yu Gothic'})

#エクセルからdfに格納する関数の定義
def read_excel_data(file_path):
    df = pd.read_excel(file_path)
    voltage = df['電圧']
    power_density = df['電力密度']
    return voltage, power_density

#最適化前...Aのデータを読み込む
voltage_A, power_density_A = read_excel_data("C:\\Users\\eitat\\OneDrive\\ドキュメント\\Mpd1.xlsx")

#トポロジー最適化後...Bのデータを読み込む
voltage_B, power_density_B = read_excel_data("C:\\Users\\eitat\\OneDrive\\ドキュメント\\Mpd2.xlsx")

#形状最適化後...Cのデータを読み込む
voltage_C, power_density_C = read_excel_data("C:\\Users\\eitat\\OneDrive\\ドキュメント\\Mpd3.xlsx")

#グラフを描画する
plt.figure(figsize=(10, 6))

plt.plot(voltage_A, power_density_A, label="最適化前", color="b")
plt.plot(voltage_B, power_density_B, label="トポロジー最適化後", color="g")
plt.plot(voltage_C, power_density_C, label="形状最適化後", color="r")

plt.xlabel("印可電圧 [V]", fontsize = 14)
plt.ylabel("電力密度 [uW/cm2]", fontsize = 14)
plt.title("印可電圧と電力密度の関係", fontsize = 18)
plt.legend(fontsize = 14)
plt.grid(True)
plt.show()

#df確認
print(voltage_A, power_density_A)
print(voltage_B, power_density_B)
print(voltage_C, power_density_C)