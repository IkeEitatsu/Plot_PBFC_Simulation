import matplotlib.pyplot as plt

# カソードのデータ（Set 1）
current_mA = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
cathode_parallelogram = [5.9004, 15.424, 26.385, 38.231, 50.769, 63.801, 77.456, 91.454, 105.89]
cathode_rectangle = [5.9013, 15.45, 26.391, 38.3, 50.847, 64.039, 77.652, 91.865, 106.24]
cathode_min_output = [6.0177, 15.837, 27.18, 39.538, 52.718, 66.485, 81.009, 96.129, 112.85]

# アノードのデータ（Set 2）
anode_parallelogram = [7.5286, 19.155, 32.908, 48.434, 65.858, 85.426, 108.154, 136.12, 176.64]
anode_rectangle = [7.5292, 19.184, 32.9, 48.484, 65.871, 85.601, 108.27, 136.36, 176.71]
anode_min_output = [7.6326, 19.535, 33.666, 49.789, 68.123, 89.021, 114.2, 146.62, 202.27]

# グラフ作成（2つ並べる）
fig, axs = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

# カソードグラフ（左）
axs[0].plot(current_mA, cathode_parallelogram, 'o', label='Parallelogram')
axs[0].plot(current_mA, cathode_rectangle, 's', label='Rectangle')
axs[0].plot(current_mA, cathode_min_output, '^', label='Min Output Shape')
axs[0].set_title('Cathode Activation Loss')
axs[0].set_xlabel('Current [mA]')
axs[0].set_ylabel('Activation Loss [μW]')
axs[0].legend()
axs[0].grid(True)

# アノードグラフ（右）
axs[1].plot(current_mA, anode_parallelogram, 'o', label='Parallelogram')
axs[1].plot(current_mA, anode_rectangle, 's', label='Rectangle')
axs[1].plot(current_mA, anode_min_output, '^', label='Min Output Shape')
axs[1].set_title('Anode Activation Loss')
axs[1].set_xlabel('Current [mA]')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()
