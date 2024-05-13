# %%
import pandas as pd

# %%
dados = {
    "nome": ["Téo", "Nah", "Napoleão"],
    "idade": [31,32,14]
}
df = pd.DataFrame(dados)
df.describe()
# %%
df['idade'].mean()
# %%
df['nome'].iloc[-1]
# %%
