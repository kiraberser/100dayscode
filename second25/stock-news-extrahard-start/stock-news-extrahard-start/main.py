import requests
from datetime import datetime
from twilio.rest import Client

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

today = datetime.now().date()
day1 = today.day 
yesterday = datetime.now().date().replace(day=day1 - 1)
day_before = datetime.now().date().replace(day=day1 - 2)

URL = "https://www.alphavantage.co/query?"
API_KEY_STOCK = "3"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_STOCK,
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
data = response.json()

price_yesterday = 209.99
price_before_yesterday = 209.72

percentage_change = ((price_yesterday - price_before_yesterday)/price_before_yesterday) * 100

API_KEY_NEWS = "4"
URL_NEWS = "https://newsapi.org/v2/everything?"

def increase_or_decrease():
    if price_yesterday < price_before_yesterday:
        lower_percentage = "🔻" + str(round(percentage_change, 2)) + "%"
        return lower_percentage
    else:
        high_percentage = "🔺" + str(round(percentage_change, 2)) + "%"
        return high_percentage
    
parameters_news = {
    "apiKey": API_KEY_NEWS,
    "qInTitle": COMPANY_NAME,
    
}
response_news = requests.get(url=URL_NEWS, params=parameters_news)
response_news.raise_for_status()
data_news = response_news.json()["articles"]

three_articles = data_news[:3]

formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

account_sid = "1"
auth_token = "2"

increseOrDecrease = increase_or_decrease()

client = Client(account_sid, auth_token)
for article in formatted_article:
    message = client.messages.create(
        body=f"{STOCK}: {increseOrDecrease}\n{article}",
        from_="+18178359131",
        to="+522321479161"
    )


