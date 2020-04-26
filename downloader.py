# BIgDoG: Basic Image Downloader for BMKG site.
# This script is intended to download radar images from BMKG website.
# All images are copyright to their respective owners.
# Requires Python 3.6 or later for f-strings.
from datetime import datetime
import hashlib
import os
import requests
import time

# Variable assignment
# Site source
default_url = "https://dataweb.bmkg.go.id/MEWS/Radar/TANG_SingleLayerCRefQC.png"
# Time interval between the checking session in second
t_interval = 120
# For image numbering
count = 1
# Get the time today
dt_now = datetime.now().strftime("%b %d %Y %H %M")
# To make directory with current time as the name e.g. Mar 31, 2020 21 30
img_dir = f"{os.getcwd()}\\{dt_now}"


# Output in command line
def print_intro():
    print("\n\n", "=" * 78, sep='')
    print("This is an automated script named BIgDoG (Basic Image Downloader"
          " for BMKG site).")
    print("Location: Tangerang.")
    print("There is no way to change the location or site unless the script"
          " is modified.")
    print("=" * 78, "\n")
    print(f"Creating directory {dt_now}.")


# Make the directory with a name as seen from above
def make_directory():
    try:
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
    global count
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


# You can stop this script with CTRL + C or just simply exiting the command line.
# Remember not to do that when a file is being written!
def download_loop():
    dl_image()
    hash_now = get_hash()

    try:
        while 1:
            if get_hash() != hash_now:
                dl_image()
                hash_now = get_hash()
            time.sleep(t_interval)

    except KeyboardInterrupt:
        print("\n\nKeyboard interrupt detected!\nNow closing...")
        exit()


# Run the function
print_intro()
make_directory()
download_loop()
