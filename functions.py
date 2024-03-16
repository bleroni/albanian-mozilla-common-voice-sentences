import shutil
import os

from dotenv import load_dotenv
load_dotenv()

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

def fix_split_word(input_text, output_text):
    pairs = [
        (" aditur", "paditur"),
        (" jyk at", "gjyk at"),
        (' randaj', 'prandaj'),
        (' DPZ', ''),
        (' SHPK',''),
        (' TVSH', ''),
    ]
    return "split word"


def fix_abbreviations(input_text, output_text):
    # AKP
    pairs = [
        ("AKP", "Agjencia Kosovare e Privatizimit"),
    ]
    pass


def fix_abbreviations_reges(input_text, output_text):
    # AKP
    pairs = [
        ("AKP", "Agjencia Kosovare e Privatizimit"),
    ]
    pass