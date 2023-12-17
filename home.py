import numpy as np
import pandas as pd
import seaborn as sns

sns.set_theme(style='darkgrid')

base_dados = sns.load_dataset('tips')
base_dados.head()