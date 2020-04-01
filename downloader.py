# BIgDoG: Basic Image Downloader for BMKG site
# This script is intended to download radar images from BMKG website.
# All images are copyright to their respective owners.
# Requires Python 3.6 or later
from datetime import datetime
import hashlib
import os
import requests
import time

# Variable assignment
default_url = "https://dataweb.bmkg.go.id/MEWS/Radar/TANG_SingleLayerCRefQC.png"  # Site source
t_interval = 120  # Time interval between the checking session in second
count = 1  # For image numbering
dt_now = datetime.now().strftime("%b %d %Y %H %M")
img_dir = f"{os.getcwd()}\\{dt_now}"

# Output in command line
print("\n\n", "=" * 78, sep='')
print("This is an automated script named BIgDoG (Basic Image Downloader for BMKG site).")
print("Location: Tangerang.")
print("There is no way to change the location or site unless the script is modified.")
print("=" * 78, "\n")
# To make directory with current time as the name. Example: Mar 31, 2020 21 30
print(f"Creating directory {dt_now}.")

try:
    # Tries to make a directory
    os.mkdir(f"{img_dir}")
except OSError:
    # If it fails, this script terminates
    print("Failed to create directory!\nDoes the script have access to write a directory?")
    exit()
else:
    # Looking good!
    print("Directory created successfully!\n")


# Function to get the content of site
def img_content():
    try:
        return requests.get(default_url).content
    except requests.Timeout:
        print("\nConnection Error.")
        print("Does this script have access to internet and the URL?")
        exit()


# To download image with requests module
def dl_image():
    # The name of image file will be number sequence starting from 1
    # e.g. "1.png", "2.png", etc.
    global count, img_dir, default_url
    img_name = f"{img_dir}\\{count}.png"

    # Image writing operation
    img_file = open(img_name, 'wb')
    img_file.write(img_content())
    img_file.close()

    print(f"Downloaded image as {count}.png at {datetime.now().strftime('%H:%M')}")
    # Add the count so the filename doesn't collide
    count += 1


# Get the hash of the site a.k.a. checking whether the image is renewed or not
def get_hash():
    return hashlib.sha256(img_content()).hexdigest()


# Initiating first image download
dl_image()
hash_now = get_hash()

# You can stop this script with CTRL + C or just simply exiting the command line.
# Remember not to do that when a file is being written!
try:
    while 1:
        if get_hash() != hash_now:
            dl_image()
            hash_now = get_hash()
        time.sleep(t_interval)

except KeyboardInterrupt:
    print("\n\nKeyboard interrupt detected!\nNow closing...")
    exit()
