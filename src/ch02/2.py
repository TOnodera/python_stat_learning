import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('precision', 3)
df = pd.read_csv('../data/ch2_scores_em.csv', index_col='生徒番号')

english_scores = np.array(df['英語'])

freq, _ = np.histogram(english_scores, bins=10, range=(0, 100))

freq_class = [f'{i}~{i+10}'for i in range(0, 100, 10)]
freq_dist_df = pd.DataFrame(
    {'度数': freq}, index=pd.Index(freq_class, name='階級'))

class_value = [(i+(i+10))//2 for i in range(0, 100, 10)]
rel_freq = freq / freq.sum()

cum_rel_freq = np.cumsum(rel_freq)

freq_dist_df['階級値'] = class_value
freq_dist_df['相対度数'] = rel_freq
freq_dist_df['累積相対度数'] = cum_rel_freq
freq_dist_df = freq_dist_df[['階級値', '度数', '相対度数', '累積相対度数']]


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

freq, _, _ = ax.hist(english_scores, bins=10, range=(0, 100))
ax.set_xlabel('点数')
ax.set_ylabel('人数')

ax.set_xticks(np.linspace(0, 100, 10+1))
ax.set_yticks(np.arange(0, freq.max()+1))

plt.show()
