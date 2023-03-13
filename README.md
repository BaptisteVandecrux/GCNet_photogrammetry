[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7729252.svg)](https://doi.org/10.5281/zenodo.7729252)

# GC-Net weather station geometry from field picture photogrammetry

Box, J., Revheim, M., Vandecrux, B.

These scripts load one by one pictures from [GCNET_photos_availability](https://github.com/GEUS-Glaciology-and-Climate/GCNET_photos_availability) and use the https://opencv.org/ Python package to track the clicks of a user on the image and counts the pixels that separate the clicks. The user is asked to click on the junction of the two levels, on the two sonic rangers, the two T/RH sensors, the two anemometers and on the estimated point where the vertical line passing by each sensor hits the surface. Eventually, the user is asked to click on the bottom and top of the anemometer which is taken as a reference for the vertical scal of the picture.

Perspective is not taken into consideration. This technique is therefore considered as a transparent and reproducible "best guess" of the instrument heights in the absence of field measurements.
