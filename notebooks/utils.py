import numpy as np
import pandas as pd

def quantile_normalize(df):
    sorted_df = np.sort(df.values, axis=0)
    mean_sorted = np.mean(sorted_df, axis=1)
    ranks = np.argsort(np.argsort(df.values, axis=0), axis=0)
    normalized = mean_sorted[ranks]
    return pd.DataFrame(normalized, columns=df.columns, index=df.index)