import time
from functions import copy_file, post_request_to_mozilla

target_file = 'copa_10_bleron_clean'
new_filename = copy_file(f'temp_folder/{target_file}.txt', f'temp_folder/{target_file}_uploading.txt')
# new_filename = 'temp_folder/tmp_kushtrim.txt'
sentences = open(new_filename, 'r').readlines()

failed_requests = []
successful_requests = []

count = 0
while sentences:
    count += 1
    sentence = sentences.pop(0)
    print(f"Processing sentence {count}: {sentence}")
    resp = post_request_to_mozilla(sentence, count)
    
    if resp != 'success':
        with open(f'temp_folder/failed_requests/{resp}.txt', 'a') as file1:
          file1.write(sentence)

    time.sleep(2)    
