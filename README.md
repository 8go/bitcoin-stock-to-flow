# :star:   bitcoin-stock-to-flow  :star:
Stock-to-Flow ratio and price for Bitcoin

`s2f.py` is a small 1-file-only Python program to pull data from internet sources (https://messari.io and https://coinmetrics.io) to display the Bitcoin stock-to-flow ratio and price. 

### What is Bitcoin Stock-to-Flow?
Stock-to-Flow (S2F, STF) is an economic model. Read more about it here:
- https://en.wikipedia.org/wiki/Stock_and_flow
- https://medium.com/@100trillionUSD/efficient-market-hypothesis-and-bitcoin-stock-to-flow-model-db17f40e6107
- https://bitcoin.clarkmoody.com/dashboard/
- https://digitalik.net/btc/

### How to run?

If desired rename `s2f.py` to `s2f`. Just type `s2f.py` into your terminal. Try `s2f.py --help` to get help.

Example output of `s2f.py`:

```
Data sources:                 messari.io and coinmetrics.io
Calculated for date:          2020-06-15
Circulating BTC:              18,411,899 BTC
Annual inflation:             1.83 %
Forward stock-to-flow ratio:  54.75
Forward stock-to-flow price:  98,163 USD
463-day Stock-to-flow ratio:  27.03
463-day Stock-to-flow price:  9,556 USD
```

Example output of `s2f.py --verbose`:

```
This program prints the Bitcoin Stock-to-Flow ratio and price.
Read about Stock-to-Flow here:    https://medium.com/@100trillionUSD/efficient-market-hypothesis-and-bitcoin-stock-to-flow-model-db17f40e6107
Compare with Stock-to-Flow data:  https://bitcoin.clarkmoody.com/dashboard/
Compare with Stock-to-Flow graph: https://digitalik.net/btc/
Data sources:                 messari.io and coinmetrics.io
Calculated for date:          2020-06-15
Circulating BTC:              18,411,899 BTC
Annual inflation:             1.83 %
Forward stock-to-flow ratio:  54.75
Forward stock-to-flow price:  98,163 USD
463-day Stock-to-flow ratio:  27.03
463-day Stock-to-flow price:  9,556 USD
```

</> with :heart:   and available on :octocat:. PRs welcome.
