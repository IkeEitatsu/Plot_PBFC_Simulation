#import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#エクセルファイルのパス
excel_file_path = "C:\\Users\\eitat\\OneDrive\\ドキュメント\\二変数解析\\取り込み用データ_重心と中間電解質に垂直で端子中点を通る直線の距離.xlsx"

# エクセルファイルをデータフレームに読み込む
df = pd.read_excel(excel_file_path)

#データフレーム表示
print(df)

#定義
Phi = df.iloc[:,0]
F = df.iloc[:,1]
G2 = df.iloc[:,2]

#2Dカラーマップを作成
#端子の中点を通り、中間電解質に垂直な直線と重心の距離
plt.scatter(Phi, F, c=G2, cmap='viridis')
plt.xlabel('Phi [degree]')
plt.ylabel('F')
plt.colorbar(label='G2 [mm]')
plt.title('Relationship between Φ, F and G2')
plt.show()

#ヒートマップ
from scipy.interpolate import griddata
Phimin=Phi.min()
Phimax=Phi.max()
Fmin=F.min()
Fmax=F.max()
msize=0.5
nsize=0.001
ax=np.arange(Phimin, Phimax+0.5, msize)
ay=np.arange(Fmin, Fmax, nsize)
xx, yy = np.meshgrid(ax, ay)
nz=griddata((Phi,F),G2,(xx,yy))
plt.contourf(xx, yy, nz)
plt.xlabel('Phi [degree]')
plt.ylabel('F')
plt.colorbar(label='G2 [mm]')
plt.title('Relationship between Φ, F and G2')
plt.show()