import requests
from bs4 import BeautifulSoup

def fetch_price(ticker):
    url = f"https://kase.kz/ru/issuers/{ticker.lower()}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price_tag = soup.find("td", class_="last")
    if not price_tag:
        return None
    price = float(price_tag.text.strip().replace(" ", "").replace(",", "."))
    return price

def get_portfolio_profit(portfolio):
    prices = {}
    total_profit = 0
    for ticker, data in portfolio.items():
        current_price = fetch_price(ticker)
        if current_price:
            profit = (current_price - data["buy_price"]) * data["quantity"]
            prices[ticker] = {"current": current_price, "profit": profit}
            total_profit += profit
        else:
            prices[ticker] = {"current": 0, "profit": 0}
    return prices, total_profit
