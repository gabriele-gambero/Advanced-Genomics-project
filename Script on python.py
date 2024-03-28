
# pip install pandas

import pandas as pd

to_sub = pd.read_csv("./SBRG/data/log_tpm_norm.csv")
print(to_sub.iloc[0:8,0:5])


