import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fontTools.ttLib.tables.otTraverse import dfs_base_table

square = lambda x: x**2
# print(square(3))
# print(list(map(square, [1, 2, 3])))
# print(list(filter(lambda x: x > 3, [1, 4, 2, 5])))

# for i, v in enumerate(['a', 'b', 'c']):
#     print(i, v)

# print(list(zip(['a', 'b'], [1, 2])))  # [('a',1), ('b',2)]

# a = np.arange(12).reshape(3, 4)
# print(a)
# print(a[1, 0])
# print(a[1, 1:3])

data = {
    "Nome": ["Mario", "Luca", "Giulia", "Marco", "Sara"],
    "Età": [25, 30, 22, 28, 26],
    "Voto": [90, 85, 95, 80, None],
    "Lingua": ["Italiano", None, "Italiano", "Francese", "Italiano"],
    "Città": ["Roma", "Milano", "Torino", "Napoli", None]
}

df = pd.DataFrame(data)
# print(df)
# print(df.describe())
# print(df.head(2))
# print(df.tail(2))
# print(df.shape) # (righe, colonne)
# print(df.isnull().sum())
# print(df.notnull().sum())
# print(df["Nome"].unique())
# print(df["Nome"].nunique())

# df["Paese"] = ["Italia", "Italia", "Italia", "Italia", "Italia"]
#
# print(df)
# print(df["Lingua"].unique())
#
# df.drop()


