import numpy as np
import pandas as pd

pd.set_option('precision', 3)
df = pd.read_csv('../data/ch2_scores_em.csv', index_col='生徒番号')

english_scores = np.array(df['英語'])
print(pd.Series(english_scores).describe())

freq, _ = np.histogram(english_scores, bins=10, range=(0, 100))

freq_class = [f'{i}~{i+10}'for i in range(0, 100, 10)]
preq_dist_df = pd.DataFrame(
    {'度数': freq}, index=pd.Index(freq_class, name='階級'))
print(preq_dist_df)
