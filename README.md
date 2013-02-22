feelingPingy
============

A collection of Python and R scripts to troubleshoot latency issues. 

License
=======
GPL

To Use
======
Open `pingTest.py` and change the ip addresses in the list near the top to include the IPs you wish to target. Change the `monitor()` parameters (last line of the script) to meet your needs. Depending on how common or uncommon your issue is, setting the duration and number of pings per sample to be higher might be worthwhile. Right now everything is set to a very low number (60 seconds, 4 pings per IP per "go"). 

Because `pingTool.py` needs root permissions to send packets, you have to run as root/admin. I have tested this on Windows and Crunchbang Linux and it works in both places. Not sure about OSX or other distros. 

Once the results are written to the CSV file, you can load them to R with the simple function `importPingData()` in `importPingData.R`. 
