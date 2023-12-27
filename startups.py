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

db.nunique()

db['Empresa'].nunique()
db['Empresa'].value_counts()

db['Setor'].nunique()
db['Setor'].value_counts(normalize=True)

plt.figure(figsize=(15,6))
plt.title('Análise Setores')
plt.xticks(rotation=45, ha='right')
plt.bar( db['Setor'].value_counts().index, db['Setor'].value_counts())

db['Pais'].value_counts()
Analise = round( db['Pais'].value_counts(normalize=True)*100,1)
top_10_sectors = db['Pais'].value_counts(normalize=True).head(10)
plt.figure(figsize=(15,6))
plt.title('Análise Setores')
plt.pie(
        top_10_sectors,
        labels=top_10_sectors.index, # type: ignore
        shadow=True,
        startangle=90,
        autopct='%1.1f%%'
        );

