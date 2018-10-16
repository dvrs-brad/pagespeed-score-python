
# Performance Audit

Performance audits are conducted using [Lighthoust](https://developers.google.com/web/tools/lighthouse/) via a python script. Lighthouse is an open-source, automated tool for improving the quality of web pages.  The resutls of the audit are saved as json and can be consumed by a dashboard program to display the health of your websites.

## Requirements

* Python 3.6
* [Lighthouse CLI](https://developers.google.com/web/tools/lighthouse/#cli)

## Running a Performance Audit
Before running the script, you need to create a a text file containing a list of websites to audit.  The format of the file is important.  It needs to be in CSV format and give the companies name and domain.  Make sure to include the first line with the columns headers (name,domain).  Save the file with extension .txt and make not of the file path.
```
name,domain
Example Company Name,https://example.com
Example Company Names,https://example.com
Example Company Name,https://example.com
Example Company Name,https://example.com
```
### Edit sitePerformance.py
Include the path to your list of websites.
```
# File containing a list of websites to audit
readPath = "/path/to/your/file/example-list.txt"
```
Enter a path to save the json results
```
# loction to save the Lighthouse json results
savePath = "/path/to/save/your/files"
```
