# %%
import pandas as pd


# %%
data = {
    "nome": ["teo", "nah", "lara", "maria"],
    "sobrenome": ["calvo", "ataide", "calvo", "calvo"],
    "idade": [31, 32, 31, 2]
}
data["idade"][0]
# %%
df = pd.DataFrame(data)
df
# %%
df["idade"]
df["idade"].iloc[0]
# %%
df.iloc[0]
# %%
df
# %%
df.index
df.columns
# %%
df.columns
# %%
df.info(memory_usage='deep')
# %%
df.dtypes

# %%
df['peso'] = [80, 53, 65, 14]
df.describe()
sumario = df.describe()
sumario['peso']['mean']
# %%
df.head()
# %%
df.tail(2)
# %%
