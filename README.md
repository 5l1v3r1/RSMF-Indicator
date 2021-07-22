# :rocket: RSMFI Indicator Modul :rocket:
![alt text](https://trading-tigers.com/assets/img/TradingTigers.png)
##### Here comes the Relative Strength Money Flow Indicator, it checks your selected trading pairs in binance futures for specified conditions and opens a LONG or SHORT position.  
RSMF Indicator is able to detect and execute an opportunity on different trading pairs at high speed.  
This is not comparable to the human trader who has to enter an order manually, at the same time, this has no emotions and executes stop loss directly.  
It eliminates the physical aspect of being glued to your screen tracking your currencies.  
You have the power to effortlessly monitor more currencies at once.
### [CHECK MORE MODULES AND INDICATORS](https://Trading-Tigers.com)
### [TradingTigers Token @BSC](https://bscscan.com/token/0x34faa80fec0233e045ed4737cc152a71e490e2e3)  
## Your benefits of our software.
#### READY FOR ALL!
Suitable for experienced, advanced and novice traders, perfect for learning.  
#### EARN WHILE YOU SLEEP!
The automated TradingTiger bots work 24/7 so you don't have to.  
#### QUICK AND EASY TO SET UP!
Little to no trading experience or programming knowledge required.  
You can run multiple trading pairs on the same exchange and check for Take Profit and Stop Loss.
#### !!!!PLEASE MAKE SURE TRADING LEVERAGE IS HIGH RISK!!!!!! 

# Setup
Install [Python3](https://www.python.org/) with pip  
install python3 moduls:
```python
python3 -m pip install -r requirements.txt
```
Install Ta-Lib:  
linux:
```bash
sudo chmod +x setup_Talib.sh
sudo ./setup_Talib.sh
```



## Preview
![alt text](https://raw.githubusercontent.com/Trading-Tiger/RSMFI-Indicator/main/preview.png) 
## Join our Community
[![TELEGRAM](https://trading-tigers.com/old_website/img/telegram-ken.png)](https://t.me/TradingTigers_Orginal)


## Settings
#### Api Keys  
Never give your API Key authorization to withdrawal, make sure that you enable trading and futures. 
#### coins
"coins" : ["BTCUSDT", "XRPUSDT" , "ADAUSDT" ], -> Pairs to Trade on Binance Future.  
You can find a complete COIN list [HERE](https://github.com/Trading-Tiger/Supported_Trading_Pairs/blob/main/Binance_Future_Pairs.json).  
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
"discord_webhook": "https://discord.com/api/webhooks/795296218/qOc_NnwZecawB0",  
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
