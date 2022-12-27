from bs4 import BeautifulSoup
import requests

date = input("which year do you want to travel to? Type Date in this format YYYY-MM-DD")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
songs = response.text
soup = BeautifulSoup(songs, "html.parser")
song_names = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
song_list = [song.getText() for song in song_names]
song_ls = [song.removeprefix("\n\n\t\n\t\n\t\t\n\t\t\t\t\t").removesuffix("\t\t\n\t\n") for song in song_list]
print(song_ls)

# "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"

# < h3
# id = "title-of-a-story"
#
#
# class ="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet" >
#
#
# Incomplete
#
# < / h3 >

spotify_client_id = "4cb98b2589434d94881ab6e9be76f298"
spotify_client_secret = "50473b0888ac4ed5a862b448fc7fa4fc"
