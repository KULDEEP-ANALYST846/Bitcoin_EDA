import pandas as pd # data pre-processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np # import it for numerical computation on data 
import matplotlib.pyplot as plt ## data viz libraries 
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
import plotly
import streamlit as st

st.set_page_config(page_title='Bitcoin Dashboard',layout='wide')
st.title('Comprehensize Bitcoin Price Analysis Dshboard' )


init_notebook_mode(connected=True)
df=pd.read_csv('bitcoin_price_Training - Training.csv')
df['Date']=pd.to_datetime(df['Date'])
df.sort_values(by='Date')
df.sort_index(ascending=False).reset_index()
#df.drop('index',axis=1,inplace=True)
df.set_index('Date',inplace=True)
df['Close_pct_change']=df['Close'].pct_change()
 

 #1st header
st.subheader('Bitcoin Candlestick Chart')
candlestick = go.Candlestick(x=df.index,open=df['Open'],close=df['Close'],high=df['High'],low=df['Low'],)
fig_candle=go.Figure(candlestick)
fig_candle.update_layout(width=1100,height=500,margin=dict(l=0,r=30,t=40,b=40),title='Bitcoin historical data')
st.plotly_chart(fig_candle,use_container_width=True)

#2nd plot
st.subheader('Daily percentage change in Closing price')

fig_change= px.line(df, y="Close_pct_change", title="Close % Change",height=500)
fig_change.update_traces(line=dict(color="rgb(255,153,51)"))

st.plotly_chart(fig_change,use_container_width=True)

#3rd plot
st.subheader('Bitcoin price trends over time')
fig_trend,ax=plt.subplots(figsize=(8,2))
sort_index=df.sort_index(ascending=False)
ax.plot(sort_index.index,df['Close'],color='green',lw=2)
ax.fill_between(sort_index.index, df['Close'], color='seagreen', alpha=0.25)

st.pyplot(fig_trend)
#4th plot
st.subheader('Average close price by Year,Month,Quarter')
interval={'YE':'Year','ME':'Month','QE':'Quarter'}
plt.figure(figsize=(8,4))
for index,key in enumerate(interval,start=1):
    plt.subplot(3,1,index)
    df['Close'].resample(key).mean().plot()
    plt.xlabel('') 
plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
st.pyplot(plt.gcf())

#5th plot
st.subheader('Close price comparison with Logrithmic Scale')
fig_log,(ax1,ax2)=plt.subplots(1,2,figsize=(14,5))
ax1.plot(df['Close'])
ax1.set_title('Close price')
ax2.plot(np.log1p(df['Close']))
ax2.set_title('Close price on Logrithmic Scale')
plt.tight_layout()
plt.subplots_adjust(left=0,wspace=0.1)
st.pyplot(fig_log,use_container_width=True)
