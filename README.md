# Google PageSpeed Score Python Script
Fetch the Google PageSpeed score for a list of URLs
## Setup
This script is designed to be ran from the command line on Linux and Mac systems. Copy the script and text files to the same directory on your sysstem.  Replace the example URLs in webiste-list.txt with a list of URLs you would like to check.  Run the script to retreive the PageSpeed score for the list of URLs in website-list.txt.

In order to call the script you must first make it executable.
```
# Make the script executable
$ chmod +x getScore
```

Add your Google API key to the script
```
def runPageSpeed(site):
    url = "https://www.googleapis.com/pagespeedonline/v4/runPagespeed?url="+site+"&strategy=desktop&key=[your-api-key]"
```


