import matplotlib.pyplot as plt
import numpy as np

# 矩形形状のデータ
Vp_rect = [
    0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09,
    0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19,
    0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29,
    0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39,
    0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49,
    0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59,
    0.6, 0.61, 0.62, 0.63, 0.64, 0.65
]
I_rect = [
    0.9675, 0.9675, 0.96749, 0.96749, 0.96749, 0.96748, 0.96747, 0.96745,
    0.96743, 0.96739, 0.96734, 0.96726, 0.96715, 0.96697, 0.96672, 0.96633,
    0.96577, 0.96494, 0.96371, 0.96191, 0.9593, 0.95555, 0.95023, 0.94284,
    0.93281, 0.91958, 0.90268, 0.88183, 0.85695, 0.8282, 0.7959, 0.76052,
    0.72258, 0.68265, 0.64128, 0.59901, 0.55635, 0.51377, 0.4717, 0.43054,
    0.39065, 0.35233, 0.31584, 0.28141, 0.24921, 0.21934, 0.19189, 0.16688,
    0.14429, 0.12405, 0.10606, 0.090189, 0.076289, 0.064185, 0.053699,
    0.044649, 0.036856, 0.03015, 0.024371, 0.019375, 0.015029, 0.011215,
    0.0078257, 0.0047549, 0.0018937, -0.00087513
]
# 平行四辺形形状のデータ
Vp_para = [
    0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09,
    0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19,
    0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29,
    0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39,
    0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49,
    0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59,
    0.6, 0.61, 0.62, 0.63, 0.64, 0.65
]
I_para = [
    0.9675, 0.9675, 0.9675, 0.9675, 0.9675, 0.96749, 0.96749, 0.96749,
    0.96748, 0.96747, 0.96746, 0.96743, 0.9674, 0.96736, 0.96728, 0.96718,
    0.96702, 0.96679, 0.96644, 0.96593, 0.96517, 0.96405, 0.9624, 0.95999,
    0.95648, 0.95146, 0.94436, 0.93453, 0.92123, 0.90377, 0.88158, 0.85432,
    0.82197, 0.78482, 0.74344, 0.69858, 0.65116, 0.6021, 0.55235, 0.50277,
    0.45416, 0.40718, 0.3624, 0.32026, 0.28108, 0.24507, 0.21233, 0.18286,
    0.15659, 0.13339, 0.11306, 0.09537, 0.080079, 0.066929, 0.055666,
    0.046047, 0.037842, 0.03084, 0.02485, 0.019703, 0.01525, 0.011361,
    0.0079165, 0.0048054, 0.0019127, -0.000884
]

# numpy配列化
Vp_rect_np = np.array(Vp_rect)
I_rect_np = np.array(I_rect)
Vp_para_np = np.array(Vp_para)
I_para_np = np.array(I_para)

plt.figure(figsize=(12, 7))

# 矩形データ
rect_line, = plt.plot(I_rect_np, Vp_rect_np, marker='o', linestyle='-', linewidth=1, label='Rectangular Data')

# 平行四辺形データ
para_line, = plt.plot(I_para_np, Vp_para_np, marker='^', linestyle='--', linewidth=1, label='Parallelogram Data')

# 支配領域の色分け（低→抵抗過電圧、 中→活性化過電圧、 高→濃度過電圧）
max_I = max(np.max(I_rect_np), np.max(I_para_np))
ohmic = plt.axvspan(0, 0.2, color='orange', alpha=0.2)
activation = plt.axvspan(0.2, 0.9, color='red', alpha=0.2)
concentration = plt.axvspan(0.9, max_I, color='blue', alpha=0.2)

# 支配領域の凡例用のダミーライン
ohmic_patch = plt.Rectangle((0,0),1,1, color='orange', alpha=0.2)
activation_patch = plt.Rectangle((0,0),1,1, color='red', alpha=0.2)
concentration_patch = plt.Rectangle((0,0),1,1, color='blue', alpha=0.2)

# 凡例を2つに分けて表示
legend1 = plt.legend(handles=[rect_line, para_line], loc='upper right', title="Data Type")
plt.gca().add_artist(legend1)

legend2 = plt.legend(handles=[ohmic_patch, activation_patch, concentration_patch],
                     labels=['Ohmic Overpotential (Low current)', 'Activation Overpotential (Mid current)', 'Concentration Overpotential (High current)'],
                     loc='lower left', title="Overpotential Regions")

plt.xlabel("Current (mA)", fontsize=12)
plt.ylabel("Voltage (V)", fontsize=12)
plt.title("I-V Curves: Rectangular & Parallelogram with Overpotential Regions", fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()
