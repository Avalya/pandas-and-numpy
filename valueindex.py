import pandas as pd
 
import numpy as np
 
# giving a scalar value with index
ser = pd.Series(10, index=['2019-01-01 00:00:00', '2019-01-31 10:29:06',
               '2019-03-02 20:58:12', '2019-04-02 07:27:18',
               '2019-05-02 17:56:24'])
 
print(ser) 