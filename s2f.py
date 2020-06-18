#!/usr/bin/env python3

# Don't change tabbing, spacing, formating as file is automatically linted.
# Ignore long lines
# pylama:format=pep8:linters=pep8:ignore=E501

import os
import sys
import logging
import traceback
import argparse
import datetime
import json
import urllib.request


def infoFromMessari():
    url = "https://data.messari.io/api/v1/assets/bitcoin/metrics"
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))
    logger.debug("cont {}".format(cont))
    fwd_stock_to_flow = cont['data']['supply']['stock_to_flow']
    # conservative formula: 0.18 * s2f^3.3
    # aggressive formula:  exp(-1.84) * s2f^3.36
    # conservative gives slightly lower price
    # conservative formula: 0.18*s2f^3.3
    fwd_stock_to_flow_usd = 0.18 * fwd_stock_to_flow ** 3.3
    annual_inflation_percent = cont['data']['supply']['annual_inflation_percent']
    circulating = cont['data']['supply']['circulating']
    logger.debug("Data {} {} {} {}".format(fwd_stock_to_flow, fwd_stock_to_flow_usd,
                                           annual_inflation_percent, circulating))
    # example output: Data 54.73928728956236 98097.8891323435
    # 1.826841468925517 18410936.0981691
    return float(circulating), float(annual_inflation_percent), float(
        fwd_stock_to_flow), float(fwd_stock_to_flow_usd)


def btcSupplyOnDate(date):
    """Provides BTC supply on a given date"""
    url = 'https://community-api.coinmetrics.io/v2/assets/btc/metricdata?metrics=SplyCur&start=' + \
        str(date) + '&end=' + str(date)
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))
    supply = cont['metricData']['series'][0]['values'][0]
    return float(supply)


def infoFromCoinMetrics(period):
    dateYesterday = datetime.date.today() - datetime.timedelta(days=1)
    datePeriodInit = dateYesterday - datetime.timedelta(days=period)
    supplyYesterday = btcSupplyOnDate(dateYesterday)
    supplyPeriodAgo = btcSupplyOnDate(datePeriodInit)
    stock_to_flow_ratio = supplyPeriodAgo / \
        ((supplyYesterday - supplyPeriodAgo) / period * 365)
    # conservative formula: 0.18*s2f^3.3, see comments above
    stock_to_flow_usd = 0.18 * stock_to_flow_ratio ** 3.3
    return stock_to_flow_ratio, stock_to_flow_usd


def s2f(args):
    """Computes and prints the Stock-to-Flow ratio and price.
    For ratio the 463-day Stock-to-Flow is used. Why 463?
    See: https://twitter.com/digitaliknet/status/1270892084929626112?s=21
    It was 365 days in a past formula, then in June 2020 adjusted to 463 as
    463 is the value fitting the curve best
    """
    period = 463
    stock_to_flow_ratio, stock_to_flow_usd = infoFromCoinMetrics(period)
    circulating, annual_inflation_percent, fwd_stock_to_flow, fwd_stock_to_flow_usd = infoFromMessari()

    if args.verbose:
        print("Read about Stock-to-Flow here:    {}".format(
            "https://medium.com/@100trillionUSD/efficient-market-hypothesis-and-bitcoin-stock-to-flow-model-db17f40e6107"))
        print("Compare with Stock-to-Flow data:  {}".format(
            "https://bitcoin.clarkmoody.com/dashboard/"))
        print(
            "Compare with Stock-to-Flow graph: {}".format("https://digitalik.net/btc/"))

    if not args.terse:
        print("Data sources:                     {}".format(
            "messari.io and coinmetrics.io"))
        print(
            "Calculated for date:              {}".format(
                datetime.date.today()))
        print(
            "Circulating BTC:                  {:,.0f} BTC".format(circulating))
        print("Annual inflation:                 {:.2f} %".format(
            annual_inflation_percent))
    print("Forward stock-to-flow ratio:      {:.2f}".format(fwd_stock_to_flow))
    print(
        "Forward stock-to-flow price:      {:,.0f} USD".format(fwd_stock_to_flow_usd))
    print("{}-day Stock-to-flow ratio:      {:.2f}".format(period, stock_to_flow_ratio))
    print("{}-day Stock-to-flow price:      {:,.0f} USD".format(period, stock_to_flow_usd))


if __name__ == "__main__":
    if "DEBUG" in os.environ:
        logging.basicConfig()  # initialize root logger, a must
        logging.getLogger().setLevel(logging.DEBUG)  # set log level on root logger
    else:
        logging.getLogger().setLevel(logging.INFO)  # set log level on root logger

    # Construct the argument parser
    ap = argparse.ArgumentParser(
        description="This program prints the Bitcoin Stock-to-Flow ratio and price")
    # Add the arguments to the parser
    ap.add_argument("-d", "--debug", required=False,
                    action="store_true", help="Print debug information")
    ap.add_argument("-v", "--verbose", required=False,
                    action="store_true", help="Print verbose output")
    ap.add_argument("-t", "--terse", required=False,
                    action="store_true", help="Print only terse condensed output")
    args = ap.parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)  # set log level on root logger
        logging.getLogger().info("Debug is turned on.")
    logger = logging.getLogger("s2f")

    try:
        s2f(args)
    except Exception:
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
