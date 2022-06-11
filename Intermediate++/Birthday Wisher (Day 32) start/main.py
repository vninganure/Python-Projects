import random
import smtplib
import datetime as dt


def read_data():

    with open("quotes.txt", "r") as quotes:
        data_list = quotes.readlines()
        # print(data_list)
        quotes = random.choice(data_list)
        return quotes

quote = read_data()
print(quote)

now = dt.datetime.now()
weekday = now.weekday()

username = "vjsmvit@gmail.com"
password = "vijay1998"
if weekday == 0:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=username, password=password)
    connection.sendmail(from_addr=username, to_addrs="preranaalka123@gmail.com",
                        msg=f"Subject: Monday Motivation\n\n {quote}")

#
#
# year = now.year
# month = now.month
# weekday = now.weekday()


