#import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#エクセルファイルのパス
excel_file_path = "C:\\Users\\eitat\\OneDrive\\ドキュメント\\取り込み用_差と平均値.xlsx"

# エクセルファイルをデータフレームに読み込む
df = pd.read_excel(excel_file_path)

#データフレーム表示
print(df)

#定義
Phi = df.iloc[:,0]
F = df.iloc[:,1]
Mpd = df.iloc[:,2]

#3Dプロット
fig = plt.figure(figsize = (8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Phi, F, Mpd, color='blue')
ax.set_title('Relationship between Average Electric Field Norm, Range of Electric Field Norm and Maximum Power Density')
ax.set_xlabel('Average Electric Field Norm [V/m]')
ax.set_ylabel('Range of Electric Field Norm [V/m]')
ax.set_zlabel('Maximum Power Density [uW/cm2]')
ax.legend()
ax.view_init(elev=10, azim=75)
plt.show()


#2Dカラーマップ
plt.scatter(Phi, F, c=Mpd, cmap='viridis')
plt.xlabel('Average Electric Field Norm [V/m]')
plt.ylabel('Range of Electric Field Norm [V/m]')
plt.colorbar(label='Maximum Power Density [uW/cm2]')
plt.title('Relationship between Average Electric Field Norm, Range of Electric Field Norm and Maximum Power Density')
plt.show()

#2Dヒートマップ
from scipy.interpolate import griddata

# グリッドサイズを最適化（粗すぎても細かすぎてもだめ）
grid_res_x = 300
grid_res_y = 300

# グリッドを作成
xi = np.linspace(Phi.min(), Phi.max(), grid_res_x)
yi = np.linspace(F.min(), F.max(), grid_res_y)
xx, yy = np.meshgrid(xi, yi)

# griddataで補間（method='linear' や 'cubic'、または 'nearest' を試す）
nz = griddata((Phi, F), Mpd, (xx, yy), method='linear')

# NaNを含む場合の処理（オプション）
# nz = np.nan_to_num(nz, nan=np.nanmean(Mpd))  # 全NaNを平均値で埋める例

# ヒートマップの描画
plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, nz, levels=300, cmap='viridis')
plt.xlabel('Average Electric Field Norm [V/m]')
plt.ylabel('Range of Electric Field Norm [V/m]')
plt.colorbar(label='Maximum Power Density [uW/cm2]')
plt.title('Relationship between Average Electric Field Norm, Range of Electric Field Norm and Maximum Power Density')
plt.show()