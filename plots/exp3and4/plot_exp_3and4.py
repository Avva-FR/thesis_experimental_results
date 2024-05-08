import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#replaced with corresponding file
df = pd.read_csv('exp4_95.csv', sep=';')
codecs = df['Codec']
file_size = df['Dateigröße [B]'].str.replace(',', '.').astype(float)  
encode_speed = df['Encode-Speed [s]'].str.replace(',', '.').astype(float) 

# tud corpa colors db and lb1
colors = ['#16335B', '#459BDE']

fig, ax1 = plt.subplots()
bar_width = 0.35
bar_positions1 = np.arange(len(codecs))

# left y axis values
for i, (codec, size) in enumerate(zip(codecs, file_size)):
    ax1.bar(bar_positions1[i] - (bar_width / 2) -0.025, size, color=colors[0], width=bar_width, label='Dateigröße [B]')

ax1.set_ylabel('Dateigröße [B]')
ax1.tick_params(axis='y')
ax1.set_ylim(0, max(file_size) * 1.1)
ax1.get_yaxis().get_major_formatter().set_scientific(False)

# right y axis
ax2 = ax1.twinx()
# right y axis values
for i, (codec, speed) in enumerate(zip(codecs, encode_speed)):
    ax2.bar(bar_positions1[i] + (bar_width / 2) +0.025, speed, color=colors[1], width=bar_width, label='Encode-Geschwindigkeit [s]')
ax2.set_ylabel('Encode-Geschwindigkeit [s]')
ax2.tick_params(axis='y')
ax2.set_ylim(0, max(encode_speed) * 1.1)

# legend format
legend_labels = ['Dateigröße [B]', 'Encode-Geschwindigkeit [s]']
legend_colors = colors
ax1.legend(handles=[plt.Rectangle((0,0),1,1, color=color) for color in legend_colors], 
           labels=legend_labels, loc='upper center', fontsize='small', ncol=2, bbox_to_anchor=(0.5, -0.06))

ax1.set_xticks(bar_positions1)
ax1.set_xticklabels(codecs)
plt.tight_layout()
plt.show()
