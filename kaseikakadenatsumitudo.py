import matplotlib.pyplot as plt

# データ
current = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]

cathode_parallel = [7.8672, 20.56533333, 35.18, 50.97466667, 67.692, 85.068, 103.2746667, 121.9386667, 141.1866667, 150.4933333]
cathode_rectangle = [7.8684, 20.6, 35.188, 51.06666667, 67.796, 85.38533333, 103.536, 122.4866667, 141.6533333, 151.4666667]
cathode_min_output = [8.0236, 21.116, 36.24, 52.71733333, 70.29066667, 88.64666667, 108.012, 128.172, 150.4666667, 161.12]

anode_parallel = [10.03813333, 25.54, 43.87733333, 64.57866667, 87.81066667, 113.9013333, 144.2053333, 181.4933333, 235.52, 293.6533333]
anode_rectangle = [10.03893333, 25.57866667, 43.86666667, 64.64533333, 87.828, 114.1346667, 144.36, 181.8133333, 235.6133333, 293.7066667]
anode_min_output = [10.1768, 26.04666667, 44.888, 66.38533333, 90.83066667, 118.6946667, 152.2666667, 195.4933333, 269.6933333, 345.2]

# 縦軸の余白を持たせた設定
all_values = cathode_parallel + cathode_rectangle + cathode_min_output + \
             anode_parallel + anode_rectangle + anode_min_output
y_min = min(all_values)
y_max = max(all_values)
y_margin = (y_max - y_min) * 0.05  # 5%余白

# グラフ描画
plt.figure(figsize=(12, 6))

# カソード
plt.subplot(1, 2, 1)
plt.plot(current, cathode_parallel, 'o', label='Parallelogram')
plt.plot(current, cathode_rectangle, 's', label='Rectangle')
plt.plot(current, cathode_min_output, '^', label='Min Output')
plt.xlabel("Current [mA]")
plt.ylabel("Activation Loss Density [uW/cm²]")
plt.title("Cathode Activation Loss Density")
plt.ylim(y_min, y_max + y_margin)
plt.legend()
plt.grid(True)

# アノード
plt.subplot(1, 2, 2)
plt.plot(current, anode_parallel, 'o', label='Parallelogram')
plt.plot(current, anode_rectangle, 's', label='Rectangle')
plt.plot(current, anode_min_output, '^', label='Min Output')
plt.xlabel("Current [mA]")
plt.ylabel("Activation Loss Density [uW/cm²]")
plt.title("Anode Activation Loss Density")
plt.ylim(y_min, y_max + y_margin)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
