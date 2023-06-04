# Stock_Prediction_Website_In_Django

In this Django project for my Software Engineering and Web Applications course I have created a Stock market Info application. In this project, my aim is to present a ‘blog’ like website about Cryptocurrency and how to start investing in them.

What are the Services provided ?
1. View Individual Stocks: 
When users input the Stock Tickers, the following details are presented to them in real time:
    Name of the company
    Today’s stock prove
    Brief description of the company
    Chart created using matplotlib to show the companies previous performances.
    
This feature is achieved by using yfinance package that allows us to download data in realtime.

2. Compare Stocks:
This feature allows users to compare the stocks of two different companies. Provides information about both these companies and provides information about their stocks.

3. Predict Future Performance Of Stocks:
  I have included an ARIMA based prediction model to predict the future stock values.
  This services provides the trend chart and the future trend as well.
  Also, it provides the predicted Market close values for the next 10 days.

Requirements:
Using python3 and Django I have created this website. For importing real-time data from Yahoo Finance I have used ‘yfinance’ package and for presenting charts I have used ‘matplotlib’ package.
For the prediction model I have used the ARIMA model from ‘statsmodel’ package. I have optimized the model by plotting autocorrelation plots on the model and determining the parameters for the model.This autocorrelation chart provides insights about the data and allows to calculate the ‘order’ parameter for the model.


