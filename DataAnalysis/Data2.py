import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df_train = pd.DataFrame([
    [100,200],
    [120,205],
    [130,210],
    [140,220],
    [150,230],
    [160,250],
    [170,270],
    [180,280],
    [190,285]
] , columns=['height', 'footnm'])


print(df_train.head(10))
print(df_train.describe())
print(df_train.corr())
corr = df_train.corr()
sns.heatmap(data=corr)
plt.show()

sns.barplot(x='height', y='footnm', data=df_train)
plt.show()
