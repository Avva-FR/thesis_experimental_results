import matplotlib.pyplot as plt

# Extracted data points for each codec
avif_data = {
    'Speed': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    'SSIM': [   0.879580961,
                0.879580961,
                0.88432688,
                0.886983332,
                0.895631767,
                0.900454622,
                0.901385805,
                0.901775421,
                0.903544614,
                0.903844601,
                0.905895263],
    'fs [B]': [ 69227.04688,
                69227.04688,
                66898.64278,
                66341.1897,
                68120.95151,
                68911.26724,
                68855.54041,
                68946.89,
                69034.97522,
                69106.45313,
                69584.32597]
}

jpegxl_data = {
    'Speed': [9, 8, 7, 6, 5, 4, 3, 2, 1],
    'SSIM': [   0.87248866,
                0.872403795,
                0.884850558,
                0.888335971,
                0.872750916,
                0.88880259,
                0.888335971,
                0.888335971,
                0.888335971],
    'fs [B]': [ 39560.5,
                39416.40586,
                41210.30828,
                40903.67138,
                40255.9341,
                44262.1059,
                43567.8431,
                47014.99552,
                47028.23897]
}

webp_data = {
    'Speed': [6, 5, 4, 3, 2, 1, 0],
    'SSIM': [   0.911997891,
                0.913421991,
                0.916769403,
                0.916441436,
                0.916224219,
                0.916848977,
                0.916787666],
    'fs [B]': [ 46664.2531,
                47795.81034,
                48969.12483,
                48969.12483,
                50384.98207,
                54377.31724,
                57580.40897]
}

fig, ax1 = plt.subplots()
fontsize_ticks = 12
fontsize_labels = 13

# left y axis
for data, color in zip([avif_data, webp_data, jpegxl_data], ['#16335B', '#2E68AF', '#459BDE']):
    ax1.scatter(data['Speed'], data['fs [B]'], color=color, label=None, marker='.')
    for i in range(len(data['Speed']) - 1):
        ax1.plot([data['Speed'][i], data['Speed'][i + 1]], [data['fs [B]'][i], data['fs [B]'][i + 1]], color=color, linestyle='--')

# right y
ax2 = ax1.twinx()
for data, color in zip([avif_data, webp_data, jpegxl_data], ['#16335B', '#2E68AF', '#459BDE']):
    ax2.scatter(data['Speed'], data['SSIM'], color=color, label=None, marker='x')
    for i in range(len(data['Speed']) - 1):
        ax2.plot([data['Speed'][i], data['Speed'][i + 1]], [data['SSIM'][i], data['SSIM'][i + 1]], color=color, linestyle='--')


# Legends
legend_handles_fs = [plt.Line2D([0], [0], color='#16335B', marker='.', linestyle='--', markersize=10),
                     plt.Line2D([0], [0], color='#2E68AF', marker='.', linestyle='--', markersize=10),
                     plt.Line2D([0], [0], color='#459BDE', marker='.', linestyle='--', markersize=10)]
legend_handles_ssim = [plt.Line2D([0], [0], color='#16335B', marker='x', linestyle='--', markersize=10),
                       plt.Line2D([0], [0], color='#2E68AF', marker='x', linestyle='--', markersize=10),
                       plt.Line2D([0], [0], color='#459BDE', marker='x', linestyle='--', markersize=10)]
legend_labels_fs = ['AVIF fs [B]', 'WebP fs [B]', 'JPEG XL fs [B]']
legend_labels_ssim = ['AVIF SSIM', 'WebP SSIM', 'JPEG XL SSIM']

#ax1.legend(legend_handles_fs + legend_handles_ssim, legend_labels_fs + legend_labels_ssim, loc='upper center', fontsize='small', ncol=3)
ax1.legend(legend_handles_fs + legend_handles_ssim, legend_labels_fs + legend_labels_ssim, loc='upper center', fontsize='small', ncol=len(legend_labels_fs)*2, bbox_to_anchor=(0.5, -0.125))
# X-axis settings
ax1.set_xlabel('Geschwindigkeitsparameter', fontsize=fontsize_labels)
ax1.set_ylabel('fs [B]', fontsize=fontsize_labels)
ax2.set_ylabel('SSIM', fontsize=fontsize_labels)

ax1.tick_params(axis='x', labelsize=fontsize_ticks)
ax1.set_xticks(avif_data['Speed'])
ax1.set_xlim(-0.5, 10.5)
ax1.tick_params(axis='y', labelsize=fontsize_ticks)
ax1.set_ylim(35000, 70000)

ax2.tick_params(axis='y', labelsize=fontsize_ticks)
ax2.set_ylim(0.8, 1)


plt.tight_layout()
plt.show()
