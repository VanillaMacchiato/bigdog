# BIgDoG

What is **BIgDoG** ?\
**BIgDoG** is an abbreviation of **B**asic **I**ma**g**e **Do**wnloader for BMK**G** site. The BMKG itself is a national agency for meteorology, climatology, and geophysics in Indonesia. The purpose of this script is to download radar images from the BMKG site periodically. This project is in early development and might be abandoned.

## More Information
### Libraries used
Libraries used: datetime, hashlib, json, os, requests, time.

These libraries are built-in. No need to download any suplementary libraries.

### Requirements
The downloader.py was written in Python 3 and f-strings are used. The f-strings are available since Python version 3.6. Therefore, you need Python 3.6 or later.

### Explanation
What will happen if you run this script?
1) Immediately downloads an image from the location you chosen. Base site: [Citra radar BMKG](https://www.bmkg.go.id/cuaca/citra-radar.bmkg) 
 Brief description:

    > Site shows radar images of rain at certain area. The site is updating its images at random interval between 3-10 minutes.
2) The hash of the image will be checked by hashlib. This step helps to recognize the image.
3) Downloader.py will sleep for 2 minutes. From there on, the script will run again to check whether the image is updated or not by hashing the image. If the image appears to be different from the previous image, the new one will be downloaded.
4) This script will repeat the cycle until it's forcibly closed.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
