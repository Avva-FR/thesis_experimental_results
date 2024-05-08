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



fig, ax = plt.subplots()
fontsize_ticks = 12
fontsize_labels = 13

ax.scatter(avif_data['SSIM'], avif_data['fs [B]'], color='#16335B', label='AVIF', marker='o')
ax.scatter(jpegxl_data['SSIM'], jpegxl_data['fs [B]'], color='#2E68AF', label='JPEG XL', marker='o')
ax.scatter(webp_data['SSIM'], webp_data['fs [B]'], color='#459BDE', label='WebP', marker='o')

ax.set_xlabel('SSIM', fontsize=fontsize_labels)
ax.set_ylabel('fs [B]', fontsize=fontsize_labels)
ax.tick_params(axis='both', which='major', labelsize=fontsize_ticks)

# limits
ax.set_xlim(0.87, 0.92)
ax.set_ylim(35000, 70000)
ax.grid(True)

# legend
ax.legend(loc='upper center', fontsize=fontsize_ticks, ncol=3, bbox_to_anchor=(0.5, -0.125))

plt.tight_layout()
plt.show()