import shutil
import os

from dotenv import load_dotenv
load_dotenv()


def save_list_to_file(list_of_strings, file_path):
    """
    Saves a list of strings to a file, with each string on a new line.
    
    :param list_of_strings: List of strings to be saved.
    :param file_path: The path of the file where the list will be saved.
    """
    with open(file_path, 'w') as file:
        for item in list_of_strings:
            file.write(f"{item}\n")

def post_request_to_mozilla(sentence):
    # Define the URL and API endpoint
    url = 'https://commonvoice.mozilla.org/api/v1/sentences'
    headers = get_headers()
    payload = get_payload(sentence)
    response = requests.post(url, headers=headers, json=payload)
    if response.ok:
        print('Response successful:', response.text)
        return 'success'
    else:
        print(str(count) + ': XXXXXXXX Request failed in text: ' + sentence)
        print('Status code:', response.status_code)
        json_resp = response.json()
        print(json_resp)
        
        if json_resp.get('errorType') is not None:
            return json_resp['errorType']
        else:
            return 'APPLICATION_500_ERROR'    


def get_payload(sentence):
  payload = {
        "domain": "general",
        "localeId": 71,
        "localeName": "sq",
        "sentence": sentence,
        "source": 'KC'  
    }
  return payload

def get_headers():
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

    return headers

def copy_file(source_path, destination_path):
    """
    Copies a file from source_path to destination_path.
    
    :param source_path: The path to the file to be copied.
    :param destination_path: The path where the file should be copied to.
    """
    # Ensure the destination directory exists, if not, create it.
    if not os.path.exists(os.path.dirname(destination_path)):
        os.makedirs(os.path.dirname(destination_path))
    
    # Copy the file to the new location
    shutil.copy(source_path, destination_path)
    print(f"File {source_path} has been copied to {destination_path}")
    return destination_path

def fix_words(input_text):
    pairs = [
        (' aditur', ' paditur'),
        (' jyk at', ' gjykat'),
        ('katë s', 'katës'),
        (' randaj', ' prandaj'),
        ('k undër', 'kundër'),              
        (' ëmtuar', ' dëmtuar'),
        (' kuzuar', ' akuzuar'),
        (' ropoz', ' propoz'),
        (' andehur', ' pandehur'),
        (' utorizuar', ' autorizuar'),
        (' ёrk', ' kërk'),
        ('nk esë', 'nkësë'),
        ('pë r', 'për'),
        ('mj et', 'mjet'),
        ('II',''),
        ('III',''),
        ('[',''),
        (']',''),
        ('(',''),
        (')',''),
        ('“',''),
        ('‘',''),
        ('”',''),
        ('’',''),
        ('AKP', 'Akp'),
        ('OAK', 'Oak'),
        (' DPZ', ''),
        (' SHPK',''),
        (' TVSH', ''),
        (' NTP', ''),                  
    ]

    for pair in pairs:
        input_text = input_text.replace(pair[0], pair[1])

    return input_text

