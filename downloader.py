# BIgDoG: Basic Image Downloader for BMKG site
# This script is intended to download radar images from BMKG website
# For personal use only
# Use Python version 3.6 or later
from datetime import datetime
import hashlib
import json
import os
import requests
import time

# Variable assignment
count = 1
DT_NOW = datetime.now().strftime("%b %d %Y %H %M")  
IMG_DIR = f"{os.getcwd()}\\{DT_NOW}"

def get_data():
    with open("region.json", "r") as region:
        data = json.loads(region.read())
    return data


def prompt_location():
    while True:
        change_location = input("Change current location? (Y/N)\n")
        if change_location.upper() == "Y":
            return True
        elif change_location.upper() == "N":
            return False
        print("Invalid input!")

    
def make_directory(location):
    print(f"Creating directory '{DT_NOW} {location}'.")
    try:
        os.mkdir(f"{IMG_DIR} {location}")
    except OSError:
        print("Failed to create directory!\nDoes the script have access to write a directory?")
        exit()
    else:
        print("Directory created successfully!\n")


def image_content(location_url):
    try:
        return requests.get(location_url).content
    except Exception as e:
        print(e)
        exit()


def write_image(location, content):
    # The name of the image will be a sequence of numbers starting from 1
    # e.g. "1.png", "2.png", etc.
    global count
    img_name = f"{IMG_DIR} {location}\\{count}.png"

    # Image writing operation
    with open(img_name, 'wb') as img_file:
        img_file.write(content)

    print(f"Image downloaded as {count}.png at {datetime.now().strftime('%H:%M')}")
    # Add the count so the filename doesn't collide
    count += 1


def get_hash(content):
    return hashlib.sha256(content).hexdigest()


def run_downloader():
    print("This is an automated script named BIgDoG (Basic Image Downloader for BMKG site).")
    print("Default location: Tangerang.")
    location = "Tangerang"
    INTERVAL = 120 #in seconds
    data = get_data()

    if prompt_location():
        print("Please choose one of the available locations: ")
        print(", ".join(data.keys()))
        while True:
            location = input("Location: ").title()
            if location in data: break
            print("No valid location found! Please try again")
    
    location_url = data[location]
    make_directory(location)

    try:
        content = image_content(location_url)
        write_image(location, content)
        current_hash = get_hash(content)

        while True:
            content = image_content(location_url)
            temp_hash = get_hash(content)
            if temp_hash != current_hash:
                write_image(location, content)
                current_hash = temp_hash
                
            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected!\nNow closing...")
        exit()


run_downloader()