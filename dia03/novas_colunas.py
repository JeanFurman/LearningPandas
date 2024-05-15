# %%

import pandas as pd
import numpy as np

df = pd.read_csv("../data/customers.csv", sep=";")

# %%
df["Points_double"] = df["Points"] * 2
df
# %%
df["Points_ratio"] = df["Points_double"] / df["Points"]
df
# %%
df["Constante"] = 1
df
# %%
df["Points_log"] = np.log(df["Points"])
# %%
np.log(df[["Points", "Points_double", "Points_ratio"]])
df["Name"].str.upper()

# %%
df["Name"].apply(lambda x: x.split("_")[0])
# %%

def intervalo_pontos(pontos):
    if pontos < 2500:
        return "baixo"
    elif pontos < 3500:
        return "medio"
    else:
        return "alto"
    
df["Faixa_pontos"] = df["Points"].apply(intervalo_pontos)
df
# %%
data = {
    'nome': ['Teo', 'Nah', 'Maria', 'Lara'],
    'recencia': [1,30,10,45],
    'valor': [100,2000,15,500],
    'frequencia':[2,5,1,15]
}

df_crm = pd.DataFrame(data)
