import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

df1 = pd.read_csv('./model/plots/latex-loss.csv')
df2 = pd.read_csv('./model/plots/latex-ner-loss.csv')
df3 = pd.read_csv('./model/plots/latex-trees-loss.csv')
df4 = pd.read_csv('./model/plots/complete-loss.csv')

df1 = df1.loc[df1['type'] == 'evaluation']
df2 = df2.loc[df2['type'] == 'evaluation']
df3 = df3.loc[df3['type'] == 'evaluation']
df4 = df4.loc[df4['type'] == 'evaluation']

df1['model'] = 'pseudolatex'
df2['model'] = 'pseudo + ner'
df3['model'] = 'pseudo + trees'
df4['model'] = 'pseudo + ner + trees'

df3.drop(index=df3.index[-1], inplace=True, axis=0)

df = pd.concat([df1,df2,df3,df4])
sns.lineplot(data=df, x='epoch', y='loss', hue='model', palette='Set2',linewidth=2.5)

plt.show()
