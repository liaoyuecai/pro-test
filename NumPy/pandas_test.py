# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# object = pd.Series([2, 5, 8, 9], index=['a', 'b', 'c', 'd'])
#
# print(object['a'])

data = pd.DataFrame(np.arange(10).reshape((2, 5)), index=['c', 'a'],
                    columns=['one', 'four', 'two', 'three', 'five'], dtype=int)

print(data)
print(data.describe())
