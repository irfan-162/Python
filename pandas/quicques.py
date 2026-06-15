import numpy as np
import pandas as pd

ser = pd.Series(['a',1, 2.5, np.nan, None])
print(ser.notnull().sum()) #output should be 3
