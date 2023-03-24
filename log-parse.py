import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <logfile>")
    sys.exit(1)

logfile = sys.argv[1]

data = {}

with open(logfile) as f:
    for line in f:
        if 'HTTP/1.1" 404' in line:
            url, status = line.split()[6], line.split()[8]
            if url not in data:
                data[url] = 1
            else:
                data[url] += 1

total = sum(data.values())

with open('output.txt', 'w') as f:
    f.write("Count   URL             Status\n")
    for url, count in sorted(data.items()):
        f.write(f"{count:<7} {url:<16} 404\n")
    f.write(f"Total: {total}\n")
