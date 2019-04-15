import pandas as pd
import numpy as np

read = pd.read_csv("property data.csv")
# print read['ST_NUM']
# print read['ST_NUM'].isnull()


cnt = 0
for row in read['OWN_OCCUPIED']:
    try:
        int(row)
        read.lac[cnt, 'OWN_OCCUPIED'] = np.nan
    except ValueError:
        pass
    cnt+=1


    print(read.isnull().sum())

    print(read.isnull().values.any())

    print read.isnull.sum().sum()