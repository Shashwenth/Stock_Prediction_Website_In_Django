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

def link_to_project1(request):
    # Redirect to Project 2's URL
    return redirect('http://127.0.0.1:8000/myapp3/')



def stock_details(request):
    # Check if form is submitted
    if request.method == 'POST':
        ticker = request.POST['ticker']
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
            # Create and save Stock object
            stock_obj=Stock()
            stock_obj.ticker=ticker
            stock_obj.name=stock_name
            stock_obj.price=stock_price
            stock_obj.description=description
            #stock_obj = Stock(ticker=ticker, name=stock_name, price=stock_price)
            stock_obj.save()

            # Get stock history data
            now = datetime.now()
            start_date = now - timedelta(days=365*10)  # 10 years ago
            end_date = now
            stock_history = stock.history(start=start_date, end=end_date)

            # Generate stock growth graph
            stock_history['Close'].plot(figsize=(10, 6))
            plt.title(f"{stock_name} Stock Growth in the Last 10 Years")
            plt.xlabel("Date")
            plt.ylabel("Close Price")
            plt.grid()
            plt.tight_layout()
            plt.savefig('compare/static/stock_growth.png')  # Save graph as image
            plt.close()

            context = {
                'ticker': ticker,
                'stock_obj': stock_obj,
                'stock_history': stock_history,
            }
            return render(request, 'stock_details_show.html', context)
        except:
            # Handle error when retrieving stock details
            context = {
                'error': 'Failed to retrieve stock details. Please check the ticker symbol.',
            }
            return render(request, 'stock_details_show.html', context)
    else:
        return render(request, 'stock_details_show.html')
