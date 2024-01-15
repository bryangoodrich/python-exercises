# 🐍 Daily Pandas 🐼
#
# Categorical plotting can be hard. Have you tried mosaic plots?
#
# I make a mock dataset of 3 hair colors and 2 genders. I use a dictionary comprehension (ugh!) to map colors to hair and alpha values (transparency) to gender for use in the mosaic plot.
#
# Then I generate counts and compare a grouped barchart to the mosaic plot in statsmodels. What do you think? Which shows the comparisons better?
#
# ------
# 🗣 If you like this post, follow Bryan for daily #python tips, and hit that like button so the algorithms help others see it, too. 
#
# For full code and data on this and other exercises, see https://www.github.com/bryangoodrich/python-exercises
# ------

import pandas as pd
import random
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

hair = ("Blonde", "Black", "Red")
gender = ("Male", "Female")
data = {
    "hair": random.choices(hair, k=100, weights=(.2, .5, .3)),
    "gender": random.choices(gender, k=100, weights=(.3, .7))
}
colors = {'Blonde':'#F2EF4C', 'Black':'#5F5C5D', 'Red':'#F70B69'}
props = {
    (h, g): {
        "facecolor": colors[h], 
        "alpha": 0.7 if g=='Male' else 1
    } 
    for h in hair for g in gender
}
df = pd.DataFrame(data)
counts = df.value_counts().reset_index()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))
counts \
    .pivot_table("count", "gender", "hair") \
    .plot.bar(ax=ax1, color=colors)
_ = mosaic(df, ["hair", "gender"], ax=ax2, properties=props)

fig.tight_layout()
plt.savefig("pandas/mosaic-plot.png")
