from flask import Flask, request,jsonify,Response
from flask import render_template
from matplotlib.pyplot import fill_between
import pandas as pd
import talib
from binance import Client
import mplfinance as mpf
from matplotlib.figure import Figure
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)

def switch(interval,coin):
    key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    client = Client(api_key = key, api_secret = secret)
    return client.get_historical_klines(coin, Client.KLINE_INTERVAL_15MINUTE,start_str = "1 days ago UTC")
    



@app.route("/")
def hello_world():
    return ("Hello World")


@app.route("/mfi")
def mfi():
    key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    client = Client(api_key = key, api_secret = secret)
    args = request.args
    interval = args['interval']
    coin = args['coin']
    
    data = switch(interval,coin)

    df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore'])
    result = talib.MFI(df["high"], df["low"], df["close"], df["volume"], timeperiod=14)
    # return f'no {interval} no2 {coin}'

    return f'{result[-1:]}'

@app.route("/adx")
def adx():
    key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    client = Client(api_key = key, api_secret = secret)
    args = request.args
    interval = args['interval']
    coin = args['coin']
    
    data = switch(interval,coin)

    df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore'])
    result = talib.ADX(df["high"], df["low"], df["close"], timeperiod=14)
    # return f'no {interval} no2 {coin}'
    return f'{result[-1:]}'

@app.route("/ema")
def ema():
    key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    client = Client(api_key = key, api_secret = secret)
    args = request.args
    interval = args['interval']
    coin = args['coin']
    
    data = switch(interval,coin)

    df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore'])
    result = talib.EMA(df["close"], timeperiod=30)
    # return f'no {interval} no2 {coin}'
    return f'{result[-1:]}'

@app.route("/sma")
def sma():
    key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    client = Client(api_key = key, api_secret = secret)
    args = request.args
    interval = args['interval']
    coin = args['coin']
    
    data = switch(interval,coin)

    df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore'])
    result = talib.SMA(df["close"], timeperiod=30)
    # return f'no {interval} no2 {coin}'
    return f'{result[-1:]}'

@app.route("/rsi")
def rsi():
    key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    client = Client(api_key = key, api_secret = secret)
    args = request.args
    interval = args['interval']
    coin = args['coin']
    
    data = switch(interval,coin)

    df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore'])
    result = talib.RSI(df["close"], timeperiod=14)
    # return f'no {interval} no2 {coin}'
    return f'{result[-1:]}'

app.route("/mom")
def mom():
    key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    client = Client(api_key = key, api_secret = secret)
    args = request.args
    interval = args['interval']
    coin = args['coin']
    
    data = switch(interval,coin)

    df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore'])
    result = talib.MOM(df["close"], timeperiod=10)
    # return f'no {interval} no2 {coin}'
    return f'{result[-1:]}'

@app.route("/mfichart")
def mfichart():
    key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    client = Client(api_key = key, api_secret = secret)
    args = request.args
    interval = args['interval']
    coin = args['coin']
    
    data = switch(interval,coin)

    df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore'])
    df.date = pd.to_datetime(df.date)
    df =  df.set_index('date')

    df = df.astype(float)
    result = talib.MFI(df["high"], df["low"], df["close"], df["volume"], timeperiod=14)
    min = result.min()
    max = result.max()
    result = pd.DataFrame(result)
    if min <= 20 and max >= 20:
        result['weak'] = [20]*96
    if min <= 50 and max >= 50:
        result['strong'] = [50]*96
    if min <= 80 and max >= 80:
        result['very'] = [80]*96
    if min <= 100 and max >= 100:
        result['extreme'] = [100]*96
    # return f'no {interval} no2 {coin}'
    
    fig = mpf.figure(figsize=(12,9))
    ax1 = fig.add_subplot(1,1,1,style='yahoo')
    ax2 = ax1.twinx()

    addplot = mpf.make_addplot(result,ax=ax2)
    mpf.plot(df,addplot=addplot , type='candle',ax=ax1, axtitle='MFI Scanner Chart')

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route("/adxchart")
def adxchart():
    key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    client = Client(api_key = key, api_secret = secret)
    args = request.args
    interval = args['interval']
    coin = args['coin']
    
    data = switch(interval,coin)

    df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore'])
    df.date = pd.to_datetime(df.date)
    df =  df.set_index('date')

    df = df.astype(float)
    result = talib.ADX(df["high"], df["low"], df["close"], timeperiod=14)
    min = result.min()
    max = result.max()
    color = ''
    adxarea = ''
    final = result[95]
    if final < 25:
        color = 'red'
        adxarea = 'Weak ADX Area'
    if final >= 25 and final < 50:
        color = 'orange'
        adxarea = 'Strong ADX Area'
    if final >= 50 and final < 75:
        color = 'blue'
        adxarea = 'Very Strong ADX Area'
    if final >= 75 and final <= 100:
        color >= 'green'
        adxarea = 'Extremely Strong ADX Area'

    result = pd.DataFrame(result)
    result['final'] = [final]*96
    mav_titles = ['ADX','Current ADX']
    if min <= 25 and max >= 25:
        result['weak'] = [25]*96
        mav_titles.append('Weak Trend Line')
    if min <= 50 and max >= 50:
        result['strong'] = [50]*96
        mav_titles.append('Strong Trend Line')
    if min <= 75 and max >= 75:
        result['very'] = [75]*96
        mav_titles.append('Very Strong Trend Line')
    if min <= 100 and max >= 100:
        result['extreme'] = [100]*96
        mav_titles.append('Extremely Strong Trend Line')
    # return f'no {interval} no2 {coin}'
    mav_titles.append(adxarea)


    fig = mpf.figure(figsize=(12,9))
    ax1 = fig.add_subplot(1,1,1,style='yahoo')
    ax2 = ax1.twinx()
    addplot = [
        mpf.make_addplot(result,ax=ax2,fill_between=dict(y1=final-5,y2=final+5,color=color,alpha=0.127), y_on_right=False)
    ]
    fig.text(0.96, 1, 'some text', size=9, fontweight='bold',color='black', ha="right")
    mpf.plot(df,addplot=addplot ,  type='candle',ax=ax1, axtitle='ADX Scanner Chart')
    ax2.legend(mav_titles)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route("/adxchart2")
def adxchart2():
    key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    client = Client(api_key = key, api_secret = secret)
    args = request.args
    interval = args['interval']
    coin = args['coin']
    
    data = switch(interval,coin)

    df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore'])
    df.date = pd.to_datetime(df.date)
    df =  df.set_index('date')

    df = df.astype(float)
    result = talib.ADX(df["high"], df["low"], df["close"], timeperiod=14)
    min = result.min()
    max = result.max()
    color = ''
    adxarea = ''
    final = result[95]
    if final < 25:
        color = 'red'
        adxarea = 'Weak ADX Area'
    if final >= 25 and final < 50:
        color = 'orange'
        adxarea = 'Strong ADX Area'
    if final >= 50 and final < 75:
        color = 'blue'
        adxarea = 'Very Strong ADX Area'
    if final >= 75 and final <= 100:
        color >= 'green'
        adxarea = 'Extremely Strong ADX Area'

    result = pd.DataFrame(result)
    result['final'] = [final]*96
    mav_titles = ['ADX','Current ADX']
    if min <= 25 and max >= 25:
        result['weak'] = [25]*96
        mav_titles.append('Weak Trend Line')
    if min <= 50 and max >= 50:
        result['strong'] = [50]*96
        mav_titles.append('Strong Trend Line')
    if min <= 75 and max >= 75:
        result['very'] = [75]*96
        mav_titles.append('Very Strong Trend Line')
    if min <= 100 and max >= 100:
        result['extreme'] = [100]*96
        mav_titles.append('Extremely Strong Trend Line')
    # return f'no {interval} no2 {coin}'
    mav_titles.append(adxarea)


    fig = mpf.figure(figsize=(12,9))
    ax1 = fig.add_subplot(2,1,1,style='yahoo')
    ax2 = ax1.twinx()
    ax3 = fig.add_subplot(2,1,2,style='yahoo')
    addplot = [
        mpf.make_addplot(result,ax=ax2,fill_between=dict(y1=final-5,y2=final+5,color=color,alpha=0.127),secondary_y=False)
    ]
    fig.text(0.96, 1, 'some text', size=9, fontweight='bold',color='black', ha="right")
    mpf.plot(df,addplot=addplot,  type='candle',ax=ax1, axtitle='ADX Scanner Chart',tight_layout=True,)
    mpf.plot(df, type='candle',ax=ax3, axtitle='ADX Scanner Chart')
    ax2.legend(mav_titles)
    ax1.set_yticklabels([])
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route("/adxchart3")
def adxchart3():
    key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    client = Client(api_key = key, api_secret = secret)
    args = request.args
    interval = args['interval']
    coin = args['coin']
    
    data = switch(interval,coin)

    df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore'])
    df.date = pd.to_datetime(df.date)
    df =  df.set_index('date')

    df = df.astype(float)
    result = talib.ADX(df["high"], df["low"], df["close"], timeperiod=14)
    min = result.min()
    max = result.max()
    color = ''
    adxarea = ''
    final = result[95]
    if final < 25:
        color = 'red'
        adxarea = 'Weak ADX Area'
    if final >= 25 and final < 50:
        color = 'orange'
        adxarea = 'Strong ADX Area'
    if final >= 50 and final < 75:
        color = 'blue'
        adxarea = 'Very Strong ADX Area'
    if final >= 75 and final <= 100:
        color >= 'green'
        adxarea = 'Extremely Strong ADX Area'

    result = pd.DataFrame(result)
    result['final'] = [final]*96
    mav_titles = ['ADX','Current ADX']
    if min <= 25 and max >= 25:
        result['weak'] = [25]*96
        mav_titles.append('Weak Trend Line')
    if min <= 50 and max >= 50:
        result['strong'] = [50]*96
        mav_titles.append('Strong Trend Line')
    if min <= 75 and max >= 75:
        result['very'] = [75]*96
        mav_titles.append('Very Strong Trend Line')
    if min <= 100 and max >= 100:
        result['extreme'] = [100]*96
        mav_titles.append('Extremely Strong Trend Line')
    # return f'no {interval} no2 {coin}'
    mav_titles.append(adxarea)


    fig = mpf.figure(figsize=(12,9))
    ax1 = fig.add_subplot(2,1,1,style='yahoo')
    ax2 = fig.add_subplot(1,1,1,style='yahoo')
    # ax3 = fig.add_subplot(3,1,3,style='yahoo')
    addplot = [
        mpf.make_addplot(result,ax=ax2,fill_between=dict(y1=final-5,y2=final+5,color=color,alpha=0.127),secondary_y=False)
    ]

    mpf.plot(df,addplot=addplot,  type='candle',ax=ax1, axtitle='ADX Scanner Chart',tight_layout=True,)
    # mpf.plot(df, type='candle',ax=ax3, axtitle='ADX Scanner Chart')
    ax2.legend(mav_titles)
    ax1.set_xticklabels([])
    ax1.axis('off')
    # ax1.set_yticklabels([])
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

app.run(host='0.0.0.0')