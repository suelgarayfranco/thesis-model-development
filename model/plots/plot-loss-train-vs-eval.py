import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
fig, ax = plt.subplots(2,2)
fig.tight_layout(h_pad=2)

df1 = pd.read_csv('./model/plots/latex-loss.csv')
ax1 = ax[0,0]
ax1.set_title('(1) PseudoLaTeX', fontweight='bold')
ax1.set_ylim([0, 1.4])

df2 = pd.read_csv('./model/plots/latex-ner-loss.csv')
ax2 = ax[0,1]
ax2.set_title('(2) PseudoLaTeX + NER', fontweight='bold')
ax2.set_ylim([0, 1.4])

df3 = pd.read_csv('./model/plots/latex-trees-loss.csv')
ax3 = ax[1,0]
ax3.set_title('(3) PseudoLaTeX + Trees', fontweight='bold')

df4 = pd.read_csv('./model/plots/complete-loss.csv')
ax4 = ax[1,1]
ax4.set_title('(4) PseudoLaTeX + NER + Trees', fontweight='bold')

sns.lineplot(data=df1, x='epoch', y='loss', hue='type', palette='Set2', ax=ax1, linewidth=2.5)
sns.lineplot(data=df2, x='epoch', y='loss', hue='type', palette='Set2', ax=ax2, linewidth=2.5)
sns.lineplot(data=df3, x='epoch', y='loss', hue='type', palette='Set2', ax=ax3, linewidth=2.5)
sns.lineplot(data=df4, x='epoch', y='loss', hue='type', palette='Set2', ax=ax4, linewidth=2.5)
plt.show()