# SciFiMap

Web-scraping for data on science fiction conventions, then using the BaseMap package to map locations of Texas conventions and normalize by county populations.  Also included is a map of US convention locations.

Directories include shapefiles used for map boundaries.

2013_txpopest_county.csv is the Texas State Demographer data.

Conlist.txt contains the html scraped from Wikipedia.

ScifiCons.ipynb is the data munging notebook, while MakeAMap.ipynb has the code for creating the maps themselves.

TexasCons.jpg or TexasCons.pdf = Texas map with location markers sized by number of conventions in that location.

TexasCoCons.jpg or pdf = Texas map with county boundaries and county color scaled by conventions per person in the county.

USAcons.jpg or pdf = USA map with state boundaries and location markers sized by number of conventions in that location.
