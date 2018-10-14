# Google PageSpeed Score Python Script
When completed thiss script will automatically monitor the Google PageSpeed score for a list of websites and notify you when a score falls below an acceptable threshold.  Currently the script will return the PageSpeed score from a text file containing a list of URLs.  The notification function and will be added it in the near future.  

## Setup
This script is designed to be ran from the command line on Linux and Mac systems. Copy the script and text files to the same directory on your sysstem.  If your text file is not in the same directory, update the script with the full path to the text file.  Replace the example URLs in webiste-list.txt with a list of URLs you would like to check.  The text file will be read line by line.  Do not add any other content to the text file.  Run the script from your terminal to retreive the PageSpeed score for the list of URLs in website-list.txt.

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


