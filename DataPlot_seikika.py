#import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#エクセルファイルのパス
excel_file_path = "C:\\Users\\eitat\\OneDrive\\ドキュメント\\取り込み用_正規化0505.xlsx"

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
ax.set_title('Relationship between Phi, F and Comprehensive Evaluation')
ax.set_xlabel('Phi [degree]')
ax.set_ylabel('F')
ax.set_zlabel('Comprehensive Evaluation')
ax.legend()
ax.view_init(elev=10, azim=75)
plt.show()

#2Dカラーマップ
plt.scatter(Phi, F, c=Mpd, cmap='viridis')
plt.xlabel('Phi [degree]')
plt.ylabel('F')
plt.colorbar(label='Comprehensive Evaluation')
plt.title('Relationship between Phi, F and Comprehensive Evaluation')
plt.show()

#2Dヒートマップ
from scipy.interpolate import griddata
Phimin=Phi.min()
Phimax=Phi.max()
Fmin=F.min()
Fmax=F.max()
msize=1
nsize=0.001
ax=np.arange(Phimin, Phimax+1, msize)
ay=np.arange(Fmin, Fmax, nsize)
xx, yy = np.meshgrid(ax, ay)
nz=griddata((Phi,F),Mpd,(xx,yy))
plt.contourf(xx, yy, nz)
plt.xlabel('Phi [degree]')
plt.ylabel('F')
plt.colorbar(label='Comprehensive Evaluation')
plt.title('Relationship between Phi, F and Comprehensive Evaluation')
plt.show()