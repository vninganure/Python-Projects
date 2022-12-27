import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Manson-Subtle-Giving-Everything-combo/dp/B07Y57WH9H/ref=sr_1_2?crid=3Q34LLAU8RGL8&keywords=the+subtle+art+of+not+giving+a+fck&qid=1655051662&s=books&sprefix=the+subtle+art+of+not+giving+a+fck%2Cstripbooks-intl-ship%2C679&sr=1-2"
# "https://www.amazon.com/Ikigai-Japanese-Secret-Long-Happy/dp/0143130722/ref=sxin_10_mbs_w_global_sims?content-id=amzn1.sym.167d0880-9da0-400b-938e-4382731a4102%3Aamzn1.sym.167d0880-9da0-400b-938e-4382731a4102&crid=3EPFGE3ZPJ0EO&cv_ct_cx=the+subtle+art+of+not+giving+a+fck&keywords=the+subtle+art+of+not+giving+a+fck&pd_rd_i=0143130722&pd_rd_r=1a701ac5-890f-4a31-9b79-793822abc7b9&pd_rd_w=X1MnO&pd_rd_wg=JUgx0&pf_rd_p=167d0880-9da0-400b-938e-4382731a4102&pf_rd_r=FYP1XX5S93ZBN5331ET0&qid=1655049814&sprefix=the+sub%2Caps%2C445&sr=1-2-9e7645f9-2d19-4bff-863e-f6cdbe50f990"

header = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.text, "html.parser")

all = soup.find("span", class_="a-size-base a-color-price a-color-price").getText()
all_split = all.split("$")[1]
price = float(all_split)
print(price)