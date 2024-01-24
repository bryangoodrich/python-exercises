import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

indicators = ["balance_frequency", "purchases_frequency",
    "oneoff_purchases_frequency", "purchases_installments_frequency",
    "cash_advance_frequency"]

df = pd.read_csv("data/shopping.csv")
df.columns = df.columns.str.lower()
values = df.drop(columns=indicators + ["cust_id"])
corr = values.corr(method='kendall')


N = len(values.columns)
fig, axes = plt.subplots(nrows=N, ncols=N, figsize=(20, 20),
    gridspec_kw={'wspace': 0, 'hspace': 0})
for i in range(N):
    for j in range(N):
        ax = axes[i, j]
        if i > j:  # Lower Triangle Scatter Plot With Regression Line
            sns.regplot(x=values.iloc[:, j], y=values.iloc[:, i], ax=ax, 
                scatter_kws={'alpha': 0.5}, line_kws={"color": 'red'})
            ax.set_xticks([])
            ax.set_yticks([])
        
        elif i < j:  # Upper Triangle Correlation Heatmap
            corr_value = corr.iloc[i, j]
            sns.heatmap([[corr_value]], annot=True,
                cmap='coolwarm', center=0, cbar=False, ax=ax)
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_frame_on(False)
        
        else:  # Diagonal KDEs
            sns.kdeplot(values.iloc[:, i], ax=ax)
            ax.set_xticks([])
            ax.set_yticks([])
        
        if j == 0:
            ax.set_ylabel(values.columns[i])
        if i == len(values.columns) - 1:
            ax.set_xlabel(values.columns[j])

plt.tight_layout()
plt.savefig("corr.png")

