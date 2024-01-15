import pandas as pd
import pyarrow.parquet as pq
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter

src = pq.read_table("data.parquet").to_pandas()
src['read_date'] = pd.to_datetime(src.read_date)
site = 'DEOK'
year = 2016

filters = (src.site == site) & (src.read_date.dt.year == year)
df = src[filters].sort_values(by='read_date')
values = df.iloc[:, 1:].set_index("read_date")
percentages = values.div(values.sum(axis=1), axis=0) * 100

# Nominal Value Heatmap
fig, ax = plt.subplots(figsize=(10, 19))
sns.heatmap(values, cmap='coolwarm',
    cbar_kws={'shrink': 0.5, 'orientation': 'horizontal'},
    xticklabels=1, yticklabels=1, ax=ax)
plt.title(f'Heatmap for {site} - Year {year}')
plt.xlabel('Hour of the day')
plt.ylabel('Day of the year')
month_locator = MonthLocator(bymonthday=1, interval=1)
ax.yaxis.set_major_locator(month_locator)
date_format = DateFormatter('%B')
ax.yaxis.set_major_formatter(date_format)
plt.subplots_adjust(top=0.95, bottom=0.01)
plt.savefig("heatmap.png")

# Percentage Heatmap
fig, ax = plt.subplots(figsize=(10, 19))
sns.heatmap(percentages, cmap='coolwarm',
    cbar_kws={'shrink': 0.5, 'orientation': 'horizontal'},
    xticklabels=1, yticklabels=1, ax=ax)
plt.title(f'Heatmap for {site} - Year {year}')
plt.xlabel('Hour of the day')
plt.ylabel('Day of the year')
month_locator = MonthLocator(bymonthday=1, interval=1)
ax.yaxis.set_major_locator(month_locator)
date_format = DateFormatter('%B')
ax.yaxis.set_major_formatter(date_format)
plt.subplots_adjust(top=0.95, bottom=0.01)
plt.savefig("heatmap2.png")

# Load Profiles
plt.figure(figsize=(8, 8))
for date, row in percentages.iterrows():
    plt.plot(range(24), row.values, alpha=0.3)
plt.title(f'Load Profiles for {site} - Year {year}')
plt.xlabel('Hour of the day')
plt.ylabel('Percentage')
plt.xticks(range(24), labels=[str(i) for i in range(24)])
plt.savefig("plot.png")