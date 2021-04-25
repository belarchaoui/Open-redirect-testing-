import sys
import requests

baseUrl = sys.argv[1]
url = sys.argv[2]
lines = open('file_urls.txt', 'r').readlines()

validUrls = []

for line in lines:
    try:
        r = requests.get(url + line)
        print('.', end='', flush=True)
        if baseUrl not in r.url:
            validUrls.append(line)
    except:
        pass

print()

if len(validUrls) == 0:
    print('Site is Secured')
else:
    for url in validUrls:
        print(url)
    print()
    print('\033[91m -- Testing  -- \033[0m')
    print()
    print('Site is venerable to open Redirect using any of the above links:')
