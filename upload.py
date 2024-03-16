import requests
import time
import os
from dotenv import load_dotenv
load_dotenv()


file1 = open('clean_files/copa_2_bleron.txt', 'r')
lines = file1.readlines()



# Define the URL and API endpoint
url = 'https://commonvoice.mozilla.org/api/v1/sentences'


# Define the headers as shown in the screenshot
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Length': '165',  # This is usually calculated automatically
    'Content-Type': 'application/json; charset=utf-8',
    'Cookie': os.environ.get('MOZILLA_COOKIE'),
    'Origin': 'https://commonvoice.mozilla.org',
    'Referer': 'https://commonvoice.mozilla.org/sq/write',
    'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0 Safari/537.36',
}

# The payload would be included if you had data to send with the POST request


# Perform the POST request

count = 0
# Strips the newline character
for line in lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    payload = {
        "domain": "general",
        "localeId": 71,
        "localeName": "sq",
        "sentence": line,
        "source": 'KC'  
    }
    print(payload)
    response = requests.post(url, headers=headers, json=payload)



    # Check the response
    if response.ok:
        print('Response successful:', response.text)
    else:
        print(str(count) + ': XXXXXXXX Request failed in text: ' + line)
        print('Status code:', response.status_code)

    time.sleep(3)    
