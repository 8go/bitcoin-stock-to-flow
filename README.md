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
Data sources:                     messari.io and coinmetrics.io
Calculated for date:              2021-05-26
Circulating BTC:                  18,725,305 BTC
Annual inflation:                 1.80 %
Estimated next halving date:      06 May 2024
Forward stock-to-flow ratio:      55.70
Forward stock-to-flow price:      103,867 USD
463-day Stock-to-flow ratio:      46.68
463-day Stock-to-flow price:      57,979 USD
Current price:                    39,322 USD
Deviation of 463-day S2F price:   32.18 %
```

Example output of `s2f.py --verbose`:

```
Read about Stock-to-Flow here:    https://medium.com/@100trillionUSD/fficient-market-hypothesis-and-bitcoin-stock-to-flow-model-db17f40e6107
Compare with Stock-to-Flow data:  https://bitcoin.clarkmoody.com/dashboard/
Compare with Stock-to-Flow graph: https://digitalik.net/btc/
Data sources:                     messari.io and coinmetrics.io
Calculated for date:              2021-05-26
Circulating BTC:                  18,725,305 BTC
Annual inflation:                 1.80 %
Estimated next halving date:      06 May 2024
Forward stock-to-flow ratio:      55.70
Forward stock-to-flow price:      103,867 USD
463-day Stock-to-flow ratio:      46.68
463-day Stock-to-flow price:      57,979 USD
Current price:                    39,155 USD
Deviation of 463-day S2F price:   32.47 %
```

</> with :heart:   and available on :octocat:. PRs welcome.
