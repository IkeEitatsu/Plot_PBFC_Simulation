import matplotlib.pyplot as plt

# データ
current = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# カソード
cathode_parallel = [0.059128, 0.077178, 0.087825, 0.095352, 0.10018, 0.10592, 0.10996, 0.11343, 0.11649]
cathode_rectangle = [0.059128, 0.077179, 0.087739, 0.095217, 0.10094, 0.1056, 0.10948, 0.11285, 0.11573]
cathode_min_output = [0.058107, 0.075267, 0.085198, 0.092117, 0.097363, 0.10147, 0.1048, 0.10742, 0.10939]

# アノード
anode_parallel = [0.075449, 0.095865, 0.10958, 0.1209, 0.13143, 0.14212, 0.15417, 0.16972, 0.19604]
anode_rectangle = [0.075454, 0.095893, 0.10955, 0.12089, 0.13141, 0.14221, 0.15427, 0.16992, 0.19613]
anode_min_output = [0.074698, 0.094834, 0.10859, 0.12026, 0.13152, 0.14315, 0.15791, 0.17827, 0.22076]

# グラフ描画
plt.figure(figsize=(12, 6))

# カソード
plt.subplot(1, 2, 1)
plt.plot(current, cathode_parallel, 'o', label='Parallel Quadrilateral')
plt.plot(current, cathode_rectangle, 's', label='Rectangle')
plt.plot(current, cathode_min_output, '^', label='Min Output')
plt.xlabel("Current [mA]")
plt.ylabel("Activation Overvoltage (Avg) [V]")
plt.title("Cathode Activation Overvoltage")
plt.legend()
plt.grid(True)

# アノード
plt.subplot(1, 2, 2)
plt.plot(current, anode_parallel, 'o', label='Parallel Quadrilateral')
plt.plot(current, anode_rectangle, 's', label='Rectangle')
plt.plot(current, anode_min_output, '^', label='Min Output')
plt.xlabel("Current [mA]")
plt.ylabel("Activation Overvoltage (Avg) [V]")
plt.title("Anode Activation Overvoltage")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
