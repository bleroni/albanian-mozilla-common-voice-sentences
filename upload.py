import requests
import time
from functions import copy_file, get_headers, get_payload

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

def save_list_to_file(list_of_strings, file_path):
    """
    Saves a list of strings to a file, with each string on a new line.
    
    :param list_of_strings: List of strings to be saved.
    :param file_path: The path of the file where the list will be saved.
    """
    with open(file_path, 'w') as file:
        for item in list_of_strings:
            file.write(f"{item}\n")

# new_filename = copy_file('clean_files/copa_2_bleron.txt', 'temp_folder/copa_2_bleron.txt')
new_filename = 'temp_folder/copa_2_bleron.txt'
sentences = open(new_filename, 'r').readlines()

# sentences = ['Kjo fjale eshte me iniciale I.L. dhe R.A. nder te tjera', 'Kjo fjali është shumë e thjeshtë.', 
#              'Prape fjali me iniciale I.L. dhe R.A., e cila nuk do duhej funksionuar', 'Tirana dhe Prishtina janë qytete shumë të bukura']

failed_requests = []
successful_requests = []

count = 0
while sentences:
    count += 1
    sentence = sentences.pop(0)
    print(f"Processing sentence {count}: {sentence}")
    resp = post_request_to_mozilla(sentence)
    if resp == 'success':
      successful_requests.append(sentence)
      save_list_to_file(successful_requests, 'temp_folder/successful_requests.txt')
    else: 
      # failed_requests.append(sentence)
      # save_list_to_file(failed_requests, f'temp_folder/failed_requests/{resp}.txt')
      with open(f'temp_folder/failed_requests/{resp}.txt', 'a') as file1:
        file1.write(sentence)

    time.sleep(2)    
