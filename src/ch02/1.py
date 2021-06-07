import numpy as np
import pandas as pd

pd.set_option('precision', 3)
df = pd.read_csv('../data/ch2_scores_em.csv', index_col='生徒番号')

scores = np.array(df['英語'])[:10]
scores_df = pd.DataFrame({'点数': scores}, index=pd.Index(
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], name='生徒'))

print(pd.Series(scores).describe())
