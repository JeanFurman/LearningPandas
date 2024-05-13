# %%
import pandas as pd

# %%
idades = [30, 42, 90, 34]
idades


# %%
media = sum(idades) / len(idades)

total = 0

for i in idades:
    total += (media - i) ** 2

variancia = total / (len(idades) - 1)
variancia
# %%
series_idades = pd.Series(idades)
series_idades
# %%
series_idades.mean()
# %%
series_idades.var()
series_idades.std()
# %%
series_idades.median()
# %%
series_idades.quantile(0.75)
# %%
series_idades.describe()
# %%
series_idades.shape
# %%
idades[0]
series_idades[0]

# %%
series_idades.index = ['t', 'e', 'o', 'c']
series_idades['t']
# %%
series_idades.iloc[-1]
series_idades.iloc[2:4]
# %%
series_idades = pd.Series(idades, name="idades")
series_idades
# %%
