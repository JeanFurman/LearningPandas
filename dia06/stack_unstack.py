# %%
import pandas as pd

df = pd.read_csv("../data/bia_consolidado.csv", sep=";")
df
# %%

df = df.set_index(["cod", "nome", "período"])
df
# %%
df_stack = df.stack().reset_index().rename(columns={"level_3": "Tipo Homicidio", 0: "Qtde"})

df_unstack = (df_stack.set_index(["cod", "nome", "período", "Tipo Homicidio"])
        .unstack()
        .reset_index())
homicidios = df_unstack["Qtde"].columns.tolist()
homicidios

df_unstack.columns = ["cod", "nome", "período"] + homicidios
df_unstack
# %%
