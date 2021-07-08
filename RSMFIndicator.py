import  json, numpy
import ccxt
from talib import RSI, MFI
from datetime import datetime
from time import sleep, time
from ccxt.base.errors import ExchangeError
import logging
from discord_webhook import DiscordWebhook, DiscordEmbed
import ccxt  # noqa: E402
# -----------------------------------------------------------------------------



with open ('settings.json') as config_file:
   config = json.load(config_file)
key = config['api-key']
secret = config['api-secret']
leverage  = config['leverage']
percentBal = config['BalancePercent_per_Order']
maxPosition = config['Max_Percent_in_Coin']
RSI_PERIOD = config['PERIOD']
RSMFI_OVERBOUGHT = config['RSMFI_OVERBOUGHT']
RSMFI_OVERSOLD = config['RSMFI_OVERSOLD']
TRADE_SYMBOL = config['coins']
CANDLE_TIME = config['CANDLE_TIME']
discord = config['discord']
discordwebhook = config['discord_webhook']
timeframe = CANDLE_TIME.lower()
sleeptime = config['CHECK_TIME_sec']
exchang = config['exchange']
market = config['market']# spot, future, margin

exchange = getattr(ccxt, exchang)({
    'apiKey': key,
    'secret': secret,
    'options': {
         'defaultType': market,}})  

log_format = '%(levelname)s - %(asctime)s - %(message)s'
logging.basicConfig(filename='errors.log', filemode='a',
  level=(logging.ERROR),
  format=log_format)


class RSI_TRADER:

    def __init__(self):
            self._TIMEOUT = 5

    def get_account(self):
        ticker = exchange.fetch_ticker(self.tickerSymbol)
        self.last = ticker['last']
        account = exchange.fapiPrivateGetAccount()
        balance = round(float(account['totalWalletBalance']), 2)
        qty1 = balance * leverage / 100  * percentBal
        qty = qty1 / self.last
        print(self.Symbol,': TIME:',datetime.now().strftime('%H:%M:%S %m-%d'))
        print(self.Symbol,': Price: {}'.format(self.last))
        print(self.Symbol,': Amount per Order:', round(qty, 4))
        print(self.Symbol,': Current RSMFI: {}'.format(round(self.average,4)))
        self.long_qty = round(qty, 4)
        self.short_qty = round(qty, 4)
        self.maxPosition = balance / self.last * (maxPosition / 100 * leverage)
        bot.check_postions()

    def clear_history(self):
        del self.closes
        del self.highs
        del self.lows
        del self.volumes
        del self.average
        del self.tickerSymbol
        #del self.Symbol
        del self.long_qty
        del self.short_qty
        del self.maxPosition
        self.closes = []
        self.highs = []
        self.lows = []
        self.volumes = []


    def start(self):
        print('Starting Relative Strength Money Flow Indicator with',len(TRADE_SYMBOL),'Coins!')
        self.closes = []
        self.highs = []
        self.lows = []
        self.volumes = []
        while True:
            try:
                for coin in TRADE_SYMBOL:
                    print('----------------------------------')
                    bot.on_message(coin)
                    sleep(sleeptime)
            except Exception as e:
                print(e)
                logging.error(e)
                sleep(15)


    def on_message(self,coin):
        self.Symbol = coin
        symbolRaw = self.Symbol[:-4]
        self.tickerSymbol = symbolRaw + '/USDT'
        # each ohlcv candle is a list of [ timestamp, open, high, low, close, volume ]
        ohlcv = exchange.fetch_ohlcv(self.tickerSymbol, timeframe)
        for candle in ohlcv:
            close = candle[4]
            high = candle[2]
            low = candle[3]
            volume = candle[5]
            self.closes.append(float(close))
            self.highs.append(float(high))
            self.lows.append(float(low))
            self.volumes.append(float(volume))
        if len(self.closes) > RSI_PERIOD:
            np_closes = numpy.array(self.closes)
            np_highs = numpy.array(self.highs)
            np_lows = numpy.array(self.lows)
            np_volumes = numpy.array(self.volumes)
            rsi = RSI(np_closes, RSI_PERIOD)
            mfi = MFI(np_highs, np_lows, np_closes, np_volumes, RSI_PERIOD)
            self.average = float(mfi[-1] + rsi[-1]) / 2
            bot.get_account()


    def place_Positions(self):
        if abs(self.size) <= self.maxPosition:
            if self.average < RSMFI_OVERSOLD:
                if self.side == None or self.side == 'long':
                    bot.set_leverage()
                    i = exchange.create_market_buy_order(self.tickerSymbol, self.long_qty)
                    print(i)
                    print('##############################################')
                    print(self.Symbol,': BUY LONG!')
                    print('##############################################')
                    self.orderside = "long"
                    self.qt =self.long_qty
                    if discord:
                        bot.send_hook()
            else:
                if self.average > RSMFI_OVERBOUGHT:
                    if self.side == None or self.side == 'short':
                        bot.set_leverage()
                        i = exchange.create_market_sell_order(self.tickerSymbol, self.short_qty )
                        print(i)
                        print('##############################################')
                        print(self.tickerSymbol,':  BUY SHORT!')
                        print('##############################################')
                        self.orderside = "short"
                        self.qt =self.short_qty
                        if discord:
                            bot.send_hook()
        else:
            if abs(self.size) >= self.maxPosition:
                print('##############################################')
                print(self.tickerSymbol,'MAX Invest reached !!!')
                print('##############################################')
        bot.clear_history()

    def check_postions(self):
        open_positions = exchange.fapiPrivateGetPositionRisk()
        for position in open_positions:
            if position['symbol'] == self.Symbol:
                if float(position['positionAmt']) > 0:
                    self.open_position = True
                    self.position = True
                    self.side = 'long'
                    self.size = float(position['positionAmt'])
                    bot.place_Positions()
                if float(position['positionAmt']) < 0:
                    self.open_position = True
                    self.position = True
                    self.side = 'short'
                    self.size = float(position['positionAmt'])
                    bot.place_Positions()
                if float(position['positionAmt']) == 0:
                    self.open_position = False
                    self.side = None
                    self.size = 0
                    bot.place_Positions()

    def send_hook(self):
        url = discordwebhook
        try:
            webhook = DiscordWebhook(url=url)
            embed = DiscordEmbed(title=('RSMFI Indicator'), description='Signal received, Buy Position:', color=242424)
            #embed.set_image(height=340,width=340 ,url='https://img.freepik.com/vektoren-kostenlos/tiger-head-angry-gesicht-mit-horn-und-drei-augen-detail-mit-grunge-effect-bearbeitbaren-schichten_67811-271.jpg?size=338&ext=jpg')
            embed.set_timestamp()
            embed.add_embed_field(name='Symbol:' , value=(str(self.Symbol)))
            embed.add_embed_field(name='LONG/SHORT:', value=(str(self.orderside)))
            embed.add_embed_field(name='Current RSMFI:', value=(str(round(self.average,4))))
            embed.add_embed_field(name='Amount', value=(str(self.qt)))
            embed.add_embed_field(name='COIN PRICE $: ', value=(str(self.last)))
            webhook.add_embed(embed)
            webhook.execute()
        except Exception as e:
            print(e)

    def set_leverage(self):
        params = {'symbol':self.Symbol,
         'leverage':leverage}
        exchange.fapiPrivatePostLeverage(params=params)

bot = RSI_TRADER()
bot.start()
