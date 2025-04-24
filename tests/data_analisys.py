import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import margins
from pandas import pivot
import seaborn as sns


# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # print(a)
#
# df = pd.DataFrame(a)
# print(df)

# print(df[1])  # prima colonna


# data = {
#     'Nome': ['Luca', 'Anna', 'Marta', 'Marco', 'Giulia', 'Francesco', 'Elena'],
#     'Età': [25, 30, 22, 28, 35, 40, 29],
#     'Città': ['Roma', 'Milano', 'Torino', 'Napoli', 'Firenze', 'Bologna', 'Venezia'],
# }
#
# df = pd.DataFrame(data)
# print(df)
# print(type(df))
# print(df.head())
# print(df.describe())
# print(df.tail())

# x = [1, 2, 3, 4, 5]
# y = [6, 7, 8, 9, 10]
# plt.plot(x, y)
# plt.title("Titolo")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()
#
#
# plt.hist(df['Età'])
# plt.title("Distribuzione età")
#
#
# plt.scatter(df['Età'], df['Nome'])


data = {
    'Nome': ['Luca', 'Anna', 'Marta', 'Giulio', 'Sara', 'Elena'],
    'Età': [25, 30, 22, 28, 24, 26],
    'Città': ['Roma', 'Milano', 'Roma', 'Bologna', 'Napoli', 'Firenze'],
    'Lingua': ['Python', 'Java', 'Python', 'C++', 'Python', 'JavaScript'],
    'Voto finale': [88, 92, 79, 85, 90, 87]
}

df = pd.DataFrame(data)

print(df)
# print(df.describe())

# plt.plot(df["Età"], df["Voto finale"])
# plt.xlabel("eta")
# plt.ylabel("voto finale")
# plt.title("relazione tra eta e voto finale")
# plt.grid(True)
# plt.show()

# plt.scatter(df["Età"], df["Voto finale"], color="red", edgecolors="blue", marker="o")
# plt.xlabel("eta")
# plt.ylabel("voto finale")
# plt.title("relazione tra eta e voto finale")
# plt.grid(True)
# plt.show()




# Scatter plot
# plt.figure(figsize=(8,6))
# plt.scatter(df["Età"], df["Voto finale"], color='red', edgecolor='black', s=200, alpha=0.7)

# Etichette con i nomi
# for i in range(len(df)):
#     plt.text(df["Età"][i]+0.2, df["Voto finale"][i], df["Nome"][i], fontsize=12)
#
# plt.xlabel("Età")
# plt.ylabel("Voto finale")
# plt.title("Relazione tra Età e Voto finale")
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# test = df[["Lingua", "Città"]].describe()
# print(test)
#
# plt.figure(figsize=(8,6))
# plt.bar(df["Nome"], df["Voto finale"], color='skyblue', edgecolor='black')
# plt.show()

# df[["Età", "Voto finale"]].plot(kind='bar', figsize=(6, 4), grid=True)
# plt.title("Boxplot di Età e Voto finale")
# plt.show()

# test_stats = test.loc[["count", "unique", "freq"]].astype(int)
# test_stats.plot(kind='bar', figsize=(6, 4), grid=True)
# plt.title("Statistiche descrittive per Lingua e Città")
# plt.xlabel("Statistiche")
# plt.ylabel("Valori", rotation=0)
# plt.xticks(rotation=0)
# plt.show()

# arr = np.array([1, 2, 3, 4, 5], "a")
# arr_1 = np.array(["a", "b", "c", "d", "e"])
# print(arr)

# print(type(arr))

# print(pd.DataFrame(arr, arr_1))
# print(pd.Series(arr, arr_1))

# print(df["Nome"].unique())

# plt.figure(figsize=(8, 5))
# sns.lineplot(x='Nome', y='Voto finale', data=df, hue = "Voto finale",  palette='viridis')
# plt.title("Voti finali degli studenti")
# # plt.show()
#
# plt.figure(figsize=(8, 5), facecolor='lightblue')
# sns.boxplot(x='Lingua', y='Voto finale', data=df, color='green')
# plt.title("Distribuzione dei voti finali per linguaggio preferito")
# plt.show()
#
# plt.figure(figsize=(8, 5))
# sns.lineplot(x='Nome', y='Voto finale', data=df, hue="Lingua", palette='viridis')
# plt.title("Voti finali degli studenti (colorati per lingua)")
# plt.show()

# plt.figure(figsize=(10, 6))
# # sns.lineplot(x='Nome', y='Voto finale', data=df, color='green')
# # sns.scatterplot(x='Nome', y='Voto finale', data=df, hue='Voto finale', marker='o', palette='viridis', s=100, edgecolor='black')
# sns.lineplot(x='Nome', y='Voto finale', data=df, hue='Voto finale', marker='o', palette='viridis')
# plt.ylabel('Voto finale', rotation=0, labelpad=30)
# plt.title("Voti finali degli studenti")
# plt.show()

# print(df["Città"])
# print(df["Città"].unique())
# print(df["Città"].describe())
# plt.figure(figsize=(8,6))
# sns.countplot(x='Città', data=df)
# plt.title("numero studenti per citta")
# plt.ylabel("Città", rotation=0, labelpad=20)
# plt.show()

# print("eta media", df["Età"].mean)
# print("lingua piu usata", df["Lingua"].mode)
# print("lingua media", df["Lingua"].median)
# print("Voto finale media", df["Voto finale"].mean)
# print("voto piu alto:")
# print(df[df["Voto finale"]==df["Voto finale"].max()])

pivot_df = df.pivot(index='Nome', columns='Lingua', values='Voto finale')
print(pivot_df)