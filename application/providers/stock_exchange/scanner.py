import yfinance as yf

from application.models.stock_price import StockPrice
from application.database import db

def downloadData():
    symbol = "CDR.WA" 

    data = yf.download(symbol, start="2014-01-17", end="2024-01-19")
    
    for index, row in data.iterrows():
        stock_price = StockPrice(
            symbol=symbol,
            date=index,
            open_price=row['Open'],
            high_price=row['High'],
            low_price=row['Low'],
            close_price=row['Close'],
            adj_close_price=row['Adj Close'],
            volume=row['Volume']
        )
        db.session.add(stock_price)

    db.session.commit()
    
if __name__ == '__main__':
    downloadData()