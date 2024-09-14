import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

df = pd.read_csv('./model/test-logs/manual-evaluation-no-base-model.csv')

hue_order = ['0', '1b', '2a', '2b', '3']

ax = sns.countplot(data=df, x='model', hue='code', hue_order=hue_order, palette='Set2')

plt.legend(loc="upper left", ncol = 5)
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))

plt.show()
