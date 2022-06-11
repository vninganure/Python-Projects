import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "c8a366357c8c415ba3bae76963317852"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "VXELHSHC33H9UGUJ"
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
responce = requests.get(STOCK_ENDPOINT, params=stock_parameters)
responce.raise_for_status()
stock_data = responce.json()
actual_data = stock_data["Time Series (Daily)"]
stock_data_list = [n for n in actual_data.items()]


#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

last_closing_price = float(stock_data_list[0][1]['4. close'])

#TODO 2. - Get the day before yesterday's closing stock price

prv_closing_price = float(stock_data_list[1][1]['4. close'])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

stock_movement = round(abs(last_closing_price-prv_closing_price), 2)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percent_change = (stock_movement/prv_closing_price)*100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if percent_change > 5:
    news_parameter ={
        "apiKey": NEWS_API,
        "qInTitle": STOCK_NAME
    }
    responce = requests.get(NEWS_ENDPOINT, params=news_parameter)
    responce.raise_for_status()
    article = responce.json()["articles"]
    three_article = article[:3]
    print(three_article)

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

