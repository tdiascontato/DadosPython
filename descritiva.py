import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

db = sns.load_dataset('iris')
db.head()
db.shape  #total de amostrs, colunas#
db['petal_length'].mean()  #média aritmética#
db['petal_length'].mode()  #moda#
db['petal_length'].median()  #mediana#
db['petal_length'].describe()  #Medidas separatrizes#
sns.boxplot(db['petal_length'])
sns.heatmap(db.corr(), annot=True)
sns.scatterplot(data=db, x='petal_length', y='petal_length')
