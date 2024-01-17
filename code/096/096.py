import struct

shapefile = "data/census_tract/cb_2022_06_tract_500k.shp"
eight_bytes = 8
offset = 36

with open(shapefile, "rb") as fh:
    fh.seek(offset)
    minx = struct.unpack("<d", fh.read(eight_bytes))
    miny = struct.unpack("<d", fh.read(eight_bytes))
    maxx = struct.unpack("<d", fh.read(eight_bytes))
    maxy = struct.unpack("<d", fh.read(eight_bytes))

with open(shapefile, "rb") as fh:
    fh.seek(offset)
    bounding_box = struct.unpack("<dddd", fh.read(4*eight_bytes))
    # (-124.409591, 32.534435, -114.131211, 42.009485)

with open(shapefile, "rb") as fh:
    buffer = fh.read(4*eight_bytes + offset)
    bounding_box = struct.unpack_from("<dddd", buffer, offset)

with open(shapefile, "rb") as fh:
    fh.seek(offset)
    buffer = fh.read(4*eight_bytes)
    points = struct.iter_unpack("<d", buffer)
    bounding_box = tuple(item[0] for item in points)
