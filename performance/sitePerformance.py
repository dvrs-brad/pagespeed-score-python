#!/usr/bin/env python3.6

import os
import csv

# open a csv file containing a list of managed websites.  Analyze each website
# with Google Lighthouse.  Generate a json file with the results.

# File containing a list of websites to audit
readPath = "/path/to/your/file/example-list.txt"
# loction to save the Lighthouse json results
savePath = "/path/to/save/audit/results"

# Open a CSV containing a list of websites to audit
with open(f'{readPath}') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Skip the first row of the CSV file
    next(csv_reader)
    print("Processiing Websites")
    for row in csv_reader:
        company = row[0]
        reportFilename = company.replace(" ", "")
        url = row[1]
        # Format the lighthouse string
        command = f"lighthouse --chrome-flags='--headless' {url} --quiet --disable-device-emulation --output=json --output-path={savePath}{reportFilename}.json"
        os.system(command)
        print(f"Generated {reportFilename}.json")
    print(f'Finished processing websites.')
