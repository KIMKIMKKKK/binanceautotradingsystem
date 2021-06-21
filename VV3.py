import time
import pyupbit
import datetime

access = "HjC5Ygpg9Oebg9xmkbus05iNhNEtk44WEWUtlfNi"
secret = "w6Z7Nd6cBQmq4BwiWwuxPe2WdrgGb1e4xxxxOUAk"

def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * 0.5
    return target_price

def get_start_time(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

def target_price_bit(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price_bit = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * 0.3
    return target_price_bit

def buy(coin):
            target_price = get_target_price(coin)
            current_price = get_current_price(coin)
            bt = get_current_price("KRW-BTC") - target_price_bit("KRW-BTC")
            print(bt, coin, "target=", target_price, "current=", current_price, "limit=", target_price - current_price)
            if target_price == current_price and 0 < bt:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order(coin, krw*0.3)

def sell(coin, KRW):
    btc = get_balance(coin)
    if btc > 0.00008:
        upbit.sell_market_order(KRW, btc)
        time.sleep(1)

upbit = pyupbit.Upbit(access, secret)

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=90):
            buy("KRW-BTC")
            buy("KRW-ETH")
            buy("KRW-ADA")
            buy("KRW-DOGE")
            buy("KRW-XRP")
            buy("KRW-DOT")
            buy("KRW-BCH")
            buy("KRW-LINK")
            buy("KRW-LTC")
            buy("KRW-XLM")
            buy("KRW-EOS")
            buy("KRW-TRX")
            buy("KRW-TFUEL")
            buy("KRW-ETC")
            buy("KRW-VET")
            buy("KRW-NEO")
            buy("KRW-THETA")
            buy("KRW-IOTA")
            buy("KRW-CRO")
            buy("KRW-BTT")
        else:
            print("Last_price Selling")
            sell("BTC", "KRW-BTC")
            sell("ETH", "KRW-ETH")
            sell("ADA", "KRW-ADA")
            sell("DOGE", "KRW-DOGE")
            sell("XRP", "KRW-XRP")
            sell("DOT", "KRW-DOT")
            sell("BCH", "KRW-BCH")
            sell("LINK", "KRW-LINK")
            sell("LTC", "KRW-LTC")
            sell("XLM", "KRW-XLM")
            sell("EOS", "KRW-EOS")
            sell("TRX", "KRW-TRX")
            sell("TFUEL", "KRW-TFUEL")
            sell("ETC", "KRW-ETC")
            sell("VET", "KRW-VET")
            sell("NEO", "KRW-NEO")
            sell("THETA", "KRW-THETA")
            sell("IOTA", "KRW-IOTA")
            sell("CRO", "KRW-CRO")
            sell("BTT", "KRW-BTT")
    except Exception as e:
        print(e)
        time.sleep(1)
