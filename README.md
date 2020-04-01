# BIgDoG

What is **BIgDoG** anyway?\
**BIgDoG** is an abbreviation of **B**asic **I**ma**g**e **Do**wnloader for BMK**G** site, while BMKG is a national
 agency for meteorology, climatology, and geophysics in Indonesia. Its function is to download radar images from the BMKG site. This project is in very early development.

## More Information
### Requirements
The script is written in Python 3.8 and there are f-strings inside. Therefore, you need minimum of Python 3.6 
interpreter to run this.

### Explanation
What happens if you run this script?
1) It downloads an image from [this site](https://dataweb.bmkg.go.id/MEWS/Radar/TANG_SingleLayerCRefQC.png) 
(All images are copyright to their respective owners). Brief description:

    > Site shows a radar image of rain on the Jabodetabek area. It refreshes at a random interval between 3-10 minutes.
2) The hash of the site will be checked using hashlib module. It helps to differentiate the image when the site 
is checked again.
3) Script sleeps for 2 minutes. After that, the script will run again to check whether the image is updated or not by 
hashing the site. If the image appears to be different from the previous one, the new one will be downloaded.
4) This script will repeat the cycle until it's forcibly closed.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
