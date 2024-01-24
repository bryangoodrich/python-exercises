import pandas as pd
import pandera as pa

chk_length_3 = pa.Check(lambda v: len(v) >= 3 if isinstance(v, str) else False,
    name = "length 3", element_wise = True)
nonnegative = pa.Check(lambda v: v >= 0, name = "nonnegative", element_wise = True)
schema = pa.DataFrameSchema({
    'name': pa.Column(pa.String, nullable=False),
    'plate': pa.Column(pa.String, nullable = True, checks = chk_length_3),
    'distance': pa.Column(pa.Float, nullable = True, checks = nonnegative)
})

try:
    df = pd.read_csv("data/rides.csv")
    schema.validate(df)
except pa.errors.SchemaError as e:
    print(e)
# on-nullable series 'name' contains null values:
# 4    NaN
# Name: name, dtype: object

# <Schema Column(name=plate, type=DataType(str))> failed element-wise validator 0:
# <Check length 3>
# failure cases:
#    index failure_case
# 0      2             
# 1      5            A

# <Schema Column(name=distance, type=DataType(float64))> failed element-wise validator 0:
# <Check nonnegative>
# failure cases:
#    index  failure_case
# 0      3          -3.2