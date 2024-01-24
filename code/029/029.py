import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

OSM = ctx.providers.OpenStreetMap.Mapnik

df = gpd.read_file("data/parksandrecs.geojson")
# 0    POINT (-121.38490 38.56548)
# 1    POINT (-121.38436 38.56526)
# 2    POINT (-121.38360 38.56522)
# 3    POINT (-121.38079 38.56640)
# 4    POINT (-121.37733 38.56684)

# EPSG Number for State Plane Zone II
points = df.to_crs(crs=2226)
# 0    POINT (6737538.412 1968351.119)
# 1    POINT (6737693.535 1968272.139)
# 2    POINT (6737910.656 1968259.393)
# 3    POINT (6738709.452 1968697.093)
# 4    POINT (6739698.089 1968863.292)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

df.plot(cmap="Blues", ax=ax1)
points.plot(cmap="Reds", ax=ax2)

ctx.add_basemap(ax1, crs=df.crs, source=OSM)
ctx.add_basemap(ax2, crs=points.crs, source=OSM)

ax1.set_title("World Coordinates (WGS 84)")
ax2.set_title("State Plane Zone II")

plt.tight_layout()
plt.savefig("map.png")