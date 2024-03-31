from datasets import load_dataset
from functions import copy_file, post_request_to_mozilla, fix_words, get_word_length

dataset = load_dataset("bleroni/kosovo-government-contract-titles", split="train")
list_dataset = dataset.to_list()

for count, row in enumerate(list_dataset[205:1205]):
  sentence = fix_words(row['Title'])  
  
  word_length = get_word_length(sentence)
  if word_length < 3 or word_length > 15:
    continue

  resp = post_request_to_mozilla(sentence, count)
  # print(count, sentence)
  if resp != 'success':
      with open(f'temp_folder/datasets/failed_requests/{resp}.txt', 'a') as file1:
        file1.write(sentence)
  else:
      with open(f'temp_folder/datasets/kosovo_tenders_successful_requests.txt', 'a') as file2:
        file2.write(f"{sentence}\n")  