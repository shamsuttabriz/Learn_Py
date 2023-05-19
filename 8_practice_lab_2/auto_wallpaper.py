""" Download image and change wallpapers automatically """

import requests
import json
import PyWallpaper

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"


# get the json
response = requests.get(api_url)
content = response.content.decode('utf-8')

# convert string to json
dict_content = json.loads(content)

# get the image url
img_url = dict_content['url']

# download the image
res = requests.get(img_url)

# save the image
with open('wallpaper.png', 'wb') as image:
    image.write(res.content)

# set as wallpaper
PyWallpaper.change_wallpaper('D:\PH_Python\#anis_vai\Learn_Py\8_practice_lab_2\wallpaper.png')