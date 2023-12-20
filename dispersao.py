import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

db = sns.load_dataset('iris')
db['sepal_length'].max() - db['sepal_length'].min() #Amplitude Total - desatualizado?#
db['sepal_length'].var() #Variância#
db['sepal_length'].std() #Desvio Padrão#