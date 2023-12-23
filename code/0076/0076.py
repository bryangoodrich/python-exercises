import yfinance as yf 

opt = yf.Ticker("GOOGL")
df = opt.option_chain('2024-01-26')
calls = df.calls
puts = df.puts
calls = calls.sort_values(by=['impliedVolatility'], ascending=False) 
puts = puts.sort_values(by=['impliedVolatility'], ascending=False)

print(puts.head())
#             lastTradeDate  strike    bid    ask  ... impliedVolatility  inTheMoney
# 2023-12-14 15:44:26+00:00    75.0   0.00   0.06  ...          0.773440       False
# 2023-12-08 20:05:41+00:00   215.0  72.85  74.15  ...          0.765627        True
# 2023-12-11 19:33:07+00:00   225.0  82.90  84.35  ...          0.642582        True
# 2023-12-20 15:35:26+00:00    85.0   0.00   0.07  ...          0.640629       False
# 2023-12-11 16:35:26+00:00    95.0   0.01   0.05  ...          0.503911       False
