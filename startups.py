import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import os
warnings.filterwarnings('ignore')

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'startups.csv')
db = pd.read_csv(file_path)
print(db.shape)
db.head()
db.columns
db.rename(
    columns={
        'Unnamed: 0':'Id',
        'Company':'Empresa',
        'Valuation ($B)':'Valor($)',
        'Date Joined':'Data de Adesão',
        'Country':'Pais',
        'City':'Cidade',
        'Industry':'Setor',
        'Select Investors':'Investimentos',
    }, inplace=True
)
db.info()
db.isnull().sum()
plt.figure(figsize=(15,6))
plt.title('Dados Nulos')
sns.heatmap(db.isnull(), cbar=False)