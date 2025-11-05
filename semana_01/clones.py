# %%

import pandas as pd

df = pd.read_parquet("../data/dados_clones.parquet")

df['General Jedi encarregado'].unique()

# %%

features = ['Massa(em kilos)', 'Estatura(cm)']

df.groupby('Status ')[features].mean()

# %%

import pandas as pd

df = pd.read_parquet("../data/dados_clones.parquet")

df['General Jedi encarregado'].unique()

# %%

from sklearn import tree

tree.plot_tree(max_depth=3)


# %%

features = ['Massa(em kilos)', 'Estatura(cm)']

df.groupby('Status ')[features].mean()
