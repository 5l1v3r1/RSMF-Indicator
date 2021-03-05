# :rocket: RSMFI Indicator Modul :rocket:
![alt text](https://trading-tigers.com/img/ms-icon-310x310.png)
##### Here comes the Relative Strength Money Flow Indicator, it checks your selected trading pairs in binance futures for specified conditions and opens a LONG or SHORT position.  
RSMF Indicator is able to detect and execute an opportunity on different trading pairs at high speed.  
This is not comparable to the human trader who has to enter an order manually, at the same time, this has no emotions and executes stop loss directly.  
It eliminates the physical aspect of being glued to your screen tracking your currencies.  
You have the power to effortlessly monitor more currencies at once.
### [CHECK MORE MODULES AND INDICATORS](https://Trading-Tigers.com)
### [TradingTigers Token @BSC](https://bscscan.com/token/0x017a6d12ca6e591d684e63791fd2de1e8a550169)
## Your benefits of our software.
#### READY FOR ALL!
Suitable for experienced, advanced and novice traders, perfect for learning.  
#### EARN WHILE YOU SLEEP!
The automated TradingTiger bots work 24/7 so you don't have to.  
#### QUICK AND EASY TO SET UP!
Little to no trading experience or programming knowledge required.  
You can run multiple trading pairs on the same exchange and check for Take Profit and Stop Loss.
### Contributing
#### !!!!PLEASE MAKE SURE TRADING LEVERAGE IS HIGH RISK!!!!!!  
![alt text](https://raw.githubusercontent.com/Trading-Tiger/RSMFI-Indicator/main/preview.png)  
[![Foo](https://trading-tigers.com/img/joindiscord.png)](https://discord.gg/xAGZHAr)  
[![TELEGRAM](https://trading-tigers.com/img/telegram-ken.png)](https://t.me/TradingTigers_Orginal)

## Authentication  
Create a Binance-Smart-Chain address from which you have the private key.  
[Then buy Trading Tiger Tokens (TIGS) at Bakeryswap](https://www.bakeryswap.org/#/swap?outputCurrency=0x017a6d12ca6e591d684e63791fd2de1e8a550169).  
You need Max 150 TIGS to start our tools, this will vary!  
If the tokens have a price, the amount will be adjusted (less).  
[![bakeryswap](https://trading-tigers.com/img/bakeryswap.png)](https://www.bakeryswap.org/#/swap?outputCurrency=0x017a6d12ca6e591d684e63791fd2de1e8a550169)
## Download  
[Find a version for your system at Releases](https://github.com/Trading-Tiger/RSMF-Indicator/releases)  
[Use the TakeProfitStopLoss module to manage your positions!](https://github.com/Trading-Tiger/StopLossTakeProfit-Modul/#rocket-stoplosstakeprofits-modul-rocket)  

## Settings

#### Api Keys  
Never give your API Key authorization to withdrawal, make sure that you enable trading and futures. 
#### coins
"coins" : ["BTCUSDT", "XRPUSDT" , "ADAUSDT" ], -> Pairs to Trade on Binance Future.  
You can find a complete COIN list [HERE](https://github.com/Trading-Tiger/Supported_Trading_Pairs/blob/main/Binance_Future_Pairs.json).
#### bsc_Secret-Key  
Binance-Smart-Chain Private-Key with Trading Tiger Tokens (TIGS).[BUY TIGS Bakeryswap](https://www.bakeryswap.org/#/swap?outputCurrency=0x017a6d12ca6e591d684e63791fd2de1e8a550169) 
#### Candles  
"CANDLE_TIME" : "5m", -> The time frame of the candles with which the indicator calculates.  
"PERIOD" : 25, -> The number of last CANDLES that are used to calculate. 14-499  
#### Position calculation  
"BalancePercent_per_Order" : 0.5, -> Wallet percentage size of a position.  
"Max_Percent_in_Coin" : 1.5, -> The maximum Wallet percentage size of a position on a trading pair.  
"leverage" : 3,-> Set Your Leverage!  
#### Position conditions 
"RSMFI_OVERBOUGHT" : 83, -> The trigger for a SHORT position.  
"RSMFI_OVERSOLD" : 21,  -> The trigger for a LONG position.  
#### Discord  
You want to receive notifications about achieved stop loss, no problem, activate it and add your Discord webhook URL.  
"discord" : true,  
"discord_webhook": "https://discord.com/api/webhooks/7952906218/qOc_NnbAywZecawB0",  
#### Interval  
  
## Optional
Install [Nodejs](https://nodejs.org/en/)  
Open CMD or SHELL with Admin
```javascript
npm install pm2 -g
```
Then you can start your Tiger Tool with:
```javascript
pm2 start <appname> --name "<set_name>"
```
And Monitoring it with:
```javascript
pm2 monit
```
Some more PM2 commands:
```javascript
pm2 status
pm2 restart <APP_Name>
pm2 stop <APP_Name>
pm2 delete <APP_Name>
```


### !!!!PLEASE MAKE SURE TRADING LEVERAGE IS HIGH RISK!!!!!!
