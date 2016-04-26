# APOD Downloader.py
# Author: Jason Duffey
# Date: 01/2016
# Downloads the current picture from NASA's Astronomy Picture of the Day website
# Saves it to a specified location and sets the picture as the desktop background

import urllib.request
import json
import ctypes
import datetime



# Get the current date as a string to save the iamge
current_date = datetime.date
today = str(current_date.today()).replace("-","")
save_location = 'C:\\Path\\To\\Save\\Location\\' + today + ".jpg"

# Get results from the NASA API website
results = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?concept_tags=True&api_key=<KEY>").read()

# Turn the results to a JSON object and get image URL
imagejson = json.loads(results.decode())
photo_url = imagejson['url']
# Retrieve the image and save it under today's date
if imagejson['media_type'] == "image":
	urllib.request.urlretrieve(photo_url,save_location)

	# Set image as background
	SPI_SETDESKWALLPAPER = 20
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0,save_location,0)
