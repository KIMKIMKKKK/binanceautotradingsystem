import time
import pyupbit
import datetime

access = ""
secret = ""

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

now = datetime.datetime.now()
start_time = get_start_time("KRW-ETH")
end_time = start_time + datetime.timedelta(days=1)

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def autotrading(coin, k):
    if start_time < now < end_time - datetime.timedelta(seconds=10):
        target_price = get_target_price(coin, k)
        ma15 = get_ma15(coin)
        current_price = get_current_price(coin)
        if target_price < current_price and ma15 < current_price:
            krw = get_balance("KRW")
            if krw > 5000:
                upbit.buy_market_order(coin, krw*0.5)

# 목표가 < 현재가 and 이동 평균 < 현재가

def autoselling(sellcoin, krwsellco):
    btc = get_balance(sellcoin)
    if btc > 0.00008:
        upbit.sell_market_order(krwsellco, btc*0.9995)
        time.sleep(1)

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
print(get_target_price("KRW-BTC", 0.5))
print(get_target_price("KRW-ETH", 0.5))
print(get_target_price("KRW-ADA", 0.5))
print(get_target_price("KRW-XRP", 0.5))
print(get_target_price("KRW-DOT", 0.5))
print(get_target_price("KRW-LINK", 0.5))
print(get_target_price("KRW-BCH", 0.5))
print(get_target_price("KRW-LTC", 0.5))
print(get_target_price("KRW-DOGE", 0.5))

# 자동매매 시작
while True:
    try:
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            autotrading("KRW-BTC", 0.5)
            autotrading("KRW-ETH", 0.5)
            autotrading("KRW-ADA", 0.5)
            autotrading("KRW-XRP", 0.5)
            autotrading("KRW-DOT", 0.5)
            autotrading("KRW-LINK", 0.5)
            autotrading("KRW-BCH", 0.5)
            autotrading("KRW-LTC", 0.5)
        else:
            autoselling("BTC", "KRW-BTC")
            autoselling("ETH", "KRW-ETH")
            autoselling("ADA", "KRW-ADA")
            autoselling("XRP", "KRW-XRP")
            autotrading("DOT", "KRW-DOT")
            autotrading("LINK", "KRW-LINK")
            autotrading("BCH", "KRW-BCH")
            autotrading("LTC", "KRW-LTC")
    except Exception as e:
        print(e)
        time.sleep(1)          
