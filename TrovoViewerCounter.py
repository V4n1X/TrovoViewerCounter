# Project: TrovoViewerCount
# Author: V4n1X (C)2020
# Version: 0.2
# Last update: 28.06.2020
# Extracting viewers from trovo.live
# using web request (#<span data-v-3dfc5312>X viewers</span>)
# Updates every 2 sec

#Import everything
from bs4 import BeautifulSoup
import urllib3
import time
import datetime
import os
import sys

#Print start time
starttime = datetime.datetime.now()
print ("Startzeit: " + str(starttime.hour) + ":" + str(starttime.minute))

#Setting vars
streamerURL = "V4n1X"
url = "https://trovo.live/" + streamerURL
fileLoc = os.path.dirname(os.path.realpath(__file__))

#Open text writer
file = open("TrovoViewerCount.txt", "w")

#Start loop
def loopit():
    try:
        #Get data pool
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        
        #Extract items
        soup = BeautifulSoup(r.data, "html.parser")
        items = soup.find("p",class_="viewer").span.text
        
        #Seperate and clean stuff
        sep = ' '
        output = items.split(sep, 1)[0]
        
        #Print stuff for logging
        print (output)
        #Open text writer
        file = open("TrovoViewerCount.txt", "w")
        file.write(output)
        file.close()
    except: #Catch *all* exceptions
        e = sys.exc_info()[0]
    
    #Wait 60 sec
    time.sleep(2)

#Restart loop
try:
    while True:
        loopit()
except: #Catch *all* exceptions
        e = sys.exc_info()[0]       
        loopit()
