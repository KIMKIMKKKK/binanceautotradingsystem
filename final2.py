import time
import pyupbit
import datetime

access = ""
secret = ""

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

def buy(coin):
            target_price = get_target_price(coin)
            current_price = get_current_price(coin)
            print(coin, "target=", target_price, "current=", current_price, "limit=", target_price - current_price)
            if target_price == current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order(coin, krw*0.5)

def sell(coin):
    selling = get_balance(coin)        
    if selling > 0.00008:
        upbit.sell_market_order(coin, selling*0.9995)
        time.sleep(1)

upbit = pyupbit.Upbit(access, secret)

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=120):
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
            print("selling")
            sell("KRW-BTC")
            sell("KRW-ETH")
            sell("KRW-ADA")
            sell("KRW-DOGE")
            sell("KRW-XRP")
            sell("KRW-DOT")
            sell("KRW-BCH")
            sell("KRW-LINK")
            sell("KRW-LTC")
            sell("KRW-XLM")
            sell("KRW-EOS")
            sell("KRW-TRX")
            sell("KRW-TFUEL")
            sell("KRW-ETC")
            sell("KRW-VET")
            sell("KRW-NEO")
            sell("KRW-THETA")
            sell("KRW-IOTA")
            sell("KRW-CRO")
            sell("KRW-BTT")
    except Exception as e:
        print(e)
        time.sleep(1)
