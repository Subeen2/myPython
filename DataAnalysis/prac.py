import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


df = pd.read_csv('https://raw.githubusercontent.com/cranberrygame/data_analysis/master/StudentsPerformance.csv')

# print(df.info())
# sns.pairplot(df)
# #두세가지 이상의 변수를 파악하려고.
# plt.show()

df['average'] = df['math score'] + df['reading score'] + df['writing score']
print(df.head())

sns.catplot(x='lunch', y='math score', data=df, hue='gender', kind='box')
plt.show()
