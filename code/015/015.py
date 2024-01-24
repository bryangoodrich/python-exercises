import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

base = "https://code.datasciencedojo.com/datasciencedojo/datasets/raw/master"
dataset = "Wholesale%20Customers/Wholesale%20customers%20data.csv"

df = pd.read_csv(f"{base}/{dataset}")
df.Channel = df.Channel.replace({1: "Hotel/Restaurant/Cafe", 2: "Retail"})
melt = pd.melt(df, 
    id_vars=['Channel', 'Region'], 
    value_vars=['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen'], 
    var_name='Category', 
    value_name='Annual Spending')

g = sns.displot(melt, x="Annual Spending", hue="Channel", col="Category", kind="kde",
    facet_kws={'sharey': False, 'sharex': False}, col_wrap=3, common_norm=True, 
    palette="pastel", linewidth=4)
g.ax.tick_params(axis='x', labelsize=12)
plt.savefig("plot.png")
