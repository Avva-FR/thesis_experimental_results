import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('exp5_icb_decode.csv', sep=';')
codecs = df['Codec']
decode_speed = df['Decode-Geschwindigkeit [s]'].str.replace(',', '.').astype(float)


colors = ['#16335B',"#2E68AF", '#459BDE']

fig, ax1 = plt.subplots()
bar_width = 0.35
bar_positions1 = np.arange(len(codecs))

for i, (codec, size) in enumerate(zip(codecs, decode_speed)):
    ax1.bar(bar_positions1[i], size, color=colors[i], width=bar_width, label='Decode-Geschwindigkeit [s]')

ax1.grid(axis='y', linestyle='-', color=(0,0,0), alpha=0.4)


ax1.set_ylabel('Decode-Geschwindigkeit [s]', fontsize=18)
ax1.tick_params(axis='y', labelsize=16)
ax1.set_ylim(0, max(decode_speed) * 1.1)
ax1.get_yaxis().get_major_formatter().set_scientific(False)

ax1.set_xticks(bar_positions1)
ax1.set_xticklabels(codecs, fontsize=16)
plt.tight_layout()
plt.show()