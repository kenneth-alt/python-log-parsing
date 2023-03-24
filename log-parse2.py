#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <logfile>")
    sys.exit(1)

logfile = sys.argv[1]

# Define a dictionary to count the number of occurrences of each URL
url_counts = {}

# Open the log file for reading
with open(logfile, 'r') as f:
    # Iterate over each line in the file
    for line in f:
        # Split the line into fields using whitespace as the delimiter
        fields = line.split()
        # Extract the URL and status code from the appropriate columns
        url = fields[6]
        status = fields[8]
        # If the status code is 404, increment the count for the URL in the dictionary
        if status == '404':
            if url in url_counts:
                url_counts[url] += 1
            else:
                url_counts[url] = 1

# Write the results to an output file
with open('output.txt', 'w') as f:
    # Write the heading row
    f.write("Count\tURL\n")
    # Iterate over the URLs and their counts, sorted alphabetically
    for url, count in sorted(url_counts.items()):
        # Write the count and URL to the file, separated by a tab
        f.write(f"{count}\t{url}\n")
    # Write the total number of URLs with a 404 error code to the file
    f.write(f"Total: {len(url_counts)}\n")
