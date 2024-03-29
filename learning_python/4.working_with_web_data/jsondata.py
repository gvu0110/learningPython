# 
# Example file for parsing and processing JSON
#

import urllib 
import json

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    
    # Now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
    
    # Output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print("There are {0} events recorded".format(count))
 
    # For each event, print the place where it occurred
    for i in theJSON["features"]:
        print(i["properties"]["place"])
        print("-----------------------")
    
    # Print the events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] > 4:
            print(str(i["properties"]["mag"]) + " at " + str(i["properties"]["place"]))
   
    # Print only the events where at least 1 person reported feeling something
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports >= 1:
            print("Report {0} times at {1}".format(feltReports, i["properties"]["place"]))
              
def main():
    # Define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    
    # Open the URL and read the data
    webUrl = urllib.urlopen(urlData)
    print ("Result code: " + str(webUrl.getcode()))

    if webUrl.getcode() == 200:
        data = webUrl.read()
        printResults(data)
    else:
        print("Error")

if __name__ == "__main__":
    main()
