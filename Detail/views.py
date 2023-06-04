# views.py

import yfinance as yf
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from datetime import datetime, timedelta
from django.shortcuts import render
from .models import Stock
from django.shortcuts import redirect
#@login_required
from django.shortcuts import redirect

def link_to_project2(request):
    # Redirect to Project 2's URL
    return redirect('http://127.0.0.1:8000/myapp2/')



def stock_details(request):
    # Check if form is submitted
    if request.method == 'POST':
        ticker = request.POST['ticker']
        ticker1 = request.POST['ticker1']
        try:
            # Retrieve stock details and price using yfinance
            print(ticker)
            stock = yf.Ticker(ticker)
            stock_name = stock.info.get("longName")
            print(stock_name)
            stock_price = stock.info.get("regularMarketPreviousClose")
            print(stock_price)
            description = stock.info.get('longBusinessSummary', 'No description available')
            print(description)

            print(ticker1)
            stock1 = yf.Ticker(ticker1)
            stock_name1 = stock1.info.get("longName")
            print(stock_name1)
            stock_price1 = stock1.info.get("regularMarketPreviousClose")
            print(stock_price1)
            description1 = stock1.info.get('longBusinessSummary', 'No description available')
            print(description1)
            # Create and save Stock object
            stock_high=stock.info.get("dayHigh")
            stock_low=stock.info.get("dayLow")
            stock_market_cap=stock.info.get("marketCap")
            stock_div_yield=stock.info.get("dividendYield")
            stock_pe_ratio=stock.info.get("trailingPE")
            stock1_high=stock1.info.get("dayHigh")
            stock1_low=stock1.info.get("dayLow")
            stock1_market_cap=stock1.info.get("marketCap")
            stock1_div_yield=stock1.info.get("dividendYield")
            stock1_pe_ratio=stock1.info.get("trailingPE")

            stock_obj=Stock()
            stock_obj.ticker=ticker
            stock_obj.name=stock_name
            stock_obj.price=stock_price
            stock_obj.description=description
            stock_obj.high=stock_high
            stock_obj.low=stock_low
            stock_obj.div=stock_div_yield
            stock_obj.pe=stock_pe_ratio
            stock_obj.cap=stock_market_cap
            #stock_obj = Stock(ticker=ticker, name=stock_name, price=stock_price)
            stock_obj.save()

            stock_obj1=Stock()
            stock_obj1.ticker=ticker1
            stock_obj1.name=stock_name1
            stock_obj1.price=stock_price1
            stock_obj1.description=description1
            stock_obj1.high=stock1_high
            stock_obj1.low=stock1_low
            stock_obj1.div=stock1_div_yield
            stock_obj1.pe=stock1_pe_ratio
            stock_obj1.cap=stock1_market_cap
            #stock_obj = Stock(ticker=ticker, name=stock_name, price=stock_price)
            stock_obj1.save()

            # Get stock history data
            now = datetime.now()
            start_date = now - timedelta(days=365*10)  # 10 years ago
            end_date = now
            stock_history = stock.history(start=start_date, end=end_date)
            stock_history1 = stock1.history(start=start_date, end=end_date)
            # Generate stock growth grap

            plt.plot(stock_history1['Close'],label=stock_name1)
            plt.plot(stock_history['Close'],label=stock_name)
            plt.title(f"{stock_name1} Stock Growth in the Last 10 Years")
            plt.xlabel("Date")
            plt.ylabel("Close Price")
            plt.grid()
            plt.legend()
            plt.tight_layout()
            plt.savefig('Detail/static/stock_comp.png')  # Save graph as image
            plt.close()

            context = {
                'ticker': ticker,
                'stock_obj': stock_obj,
                'stock_history': stock_history,
                'ticker1': ticker1,
                'stock_obj1': stock_obj1,
                'stock_history1': stock_history1,
            }
            return render(request, 'stock_details.html', context)
        except:
            # Handle error when retrieving stock details
            context = {
                'error': 'Failed to retrieve stock details. Please check the ticker symbol.',
            }
            return render(request, 'stock_details.html', context)
    else:
        return render(request, 'stock_details.html')
