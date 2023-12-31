Happy Holidays! 🎉🎉

Let's use Python to give us an advantage in options trading in the most secure way possible!

This analysis is self-explantory, but the short of it is this

➡️ Filter for a given stock (GOOGL) in this case
➡️ Filter for a given expiration, I'm going with last Friday of Jan 2024
➡️ Filter for strike price within 5% of it's 50 day moving average (DMA)
➡️ Filter that this strike price is not "in the money" (less than stock price)

After these subsets, we can look at the premium we would receive, which is the lastPrice * 100, because an option is always for 100 shares of the stock. So an option price 0.80 will get me $80 (minus fees and commission) per contract. I guess I could have also included the leverage (money) required for this trade, which say the option price is 130 then I need to cover this put by having $13,000 in my account! 

Anyway, I look at this data table as well as visualize the trading volume at different strike prices. Quickly I can see $135 looks promising because it's a nice size premium for 1 contract, it's got much more volume than 134, and it's still got a good bid-ask spread so if I try to sell this on Tuesday, it might go through quickly before the premium drops anymore! 

Why is this safe? 

1️⃣ Selling puts only requires you be willing to buy the stock.
2️⃣ We're only looking for a bargain strike price, so worth buying!
3️⃣ If stock price goes ⬆️ the put loses value and we keep premium.
4️⃣ If stock prices goes ⬇️ we may get assigned (have to buy), but we still keep premium! Not assigned, no different. Assigned, we bargain shop!
5️⃣ If assigned, we now sell covered calls on the stocks we own until we have to sell our stock at more than we bought, making more 💰💰💰

This is the basics of the Wheel Strategy. Easy, safe, and made me over $500 in December just trying out (need to compute my APY of invested capital). 

I'll be taking a break from doing stock stuff on my daily posts, unless people are interested. Let me know!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0078.png" />

