#import部分
import matplotlib
import pandas as pd
matplotlib.use('tkagg')
import matplotlib.pyplot as plt

#フォントを日本語可能にする
matplotlib.rc('font', **{'family':'Yu Gothic'})

#エクセルからdfに格納する関数の定義
def read_excel_data(file_path):
    df = pd.read_excel(file_path)
    voltage = df['電圧']
    power_density = df['電力密度']
    current_density = df['電流密度']
    return voltage, power_density, current_density

#最適化前...Aのデータを読み込む
voltage_A, power_density_A, current_density_A = read_excel_data("C:\\Users\\eitat\\OneDrive\\ドキュメント\\Mpd4.xlsx")

#トポロジー最適化後...Bのデータを読み込む
voltage_B, power_density_B, current_density_B = read_excel_data("C:\\Users\\eitat\\OneDrive\\ドキュメント\\Mpd5.xlsx")

#形状最適化後...Cのデータを読み込む
voltage_C, power_density_C, current_density_C = read_excel_data("C:\\Users\\eitat\\OneDrive\\ドキュメント\\Mpd6.xlsx")

#グラフを描画する（二軸設定）
fig, ax1 = plt.subplots(figsize=(10, 6))

#左側に電力密度をプロット(実線)
ax1.plot(voltage_A, power_density_A, label="最適化前の電力密度", color="b")
ax1.plot(voltage_B, power_density_B, label="トポロジー最適化後の電力密度", color="g")
ax1.plot(voltage_C, power_density_C, label="形状最適化後の電力密度", color="r")
ax1.set_xlabel("印可電圧 [V]", fontsize = 14)
ax1.set_ylabel("電力密度 [uW/cm2]", fontsize = 14)

#右側に電流密度をプロット (点線)
ax2 = ax1.twinx()
ax2.plot(voltage_A, current_density_A, label="最適化前の電流密度", color="b", linestyle='--')
ax2.plot(voltage_B, current_density_B, label="トポロジー最適化後の電流密度", color="g", linestyle='--')
ax2.plot(voltage_C, current_density_C, label="形状最適化後の電流密度", color="r", linestyle='--')
ax2.set_ylabel("電流密度 [mA/cm2]", fontsize = 14)

plt.title("印可電圧と電力密度、電流密度の関係", fontsize = 16)

#2軸の分レジェンドに表示
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
plt.legend(lines + lines2, labels + labels2, fontsize = 12)

#軸の数値のフォントサイズ
ax1.tick_params(axis='both', labelsize=12)
ax2.tick_params(axis='y', labelsize=12)

#横軸表示範囲
plt.xlim(0, 0.65)
plt.grid(True)
plt.show()

#df確認
print(voltage_A, power_density_A, current_density_A)
print(voltage_B, power_density_B, current_density_B)
print(voltage_C, power_density_C, current_density_C)