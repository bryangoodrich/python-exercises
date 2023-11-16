import geodatasets
import geopandas as gpd
import geoplot
import matplotlib.pyplot as plt

chicago_data = geodatasets.get_path("geoda.chicago_commpop")
grocery_store_data = geodatasets.get_path("geoda.groceries")
chicago = gpd.read_file(chicago_data)
groceries = gpd.read_file(grocery_store_data)
groceries.geometry = groceries.centroid
groceries = groceries.to_crs(chicago.crs)

fig, ax = plt.subplots(figsize=(10, 8))
base = chicago.plot(ax=ax, color='white', edgecolor='black')
groceries.plot(ax=base, marker='o', color='red', markersize=15)
geoplot.kdeplot(groceries, cmap="Reds", fill=True, n_levels=10, alpha=0.65, ax=base)

plt.savefig("map.png")
