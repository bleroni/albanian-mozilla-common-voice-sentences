from functions import copy_file, fix_words
target_file = 'copa_10_bleron'
new_filename = copy_file(f'temp_folder/{target_file}.txt', f'temp_folder/{target_file}_copy.txt')

sentences = open(f'{new_filename}', 'r').readlines()
modified_sentences = []

for sentence in sentences: # [-5:]
  sentence = fix_words(sentence)
  # Fix broken and other words
  words = sentence.split()
  print(words)

  # Fix uppercase words
  transformed_words = []
  for word in words:
    if word.isupper():
      transformed_words.append(word.capitalize())
    else:
      transformed_words.append(word)
  print(transformed_words)    
  print('-------')  

  modified_sentence = ' '.join(transformed_words)
  modified_sentences.append(modified_sentence)


transformed_filename = f"{new_filename.replace('.txt','')}_transformed.txt"
with open(transformed_filename, 'a') as file1:
  file1.write('\n'.join(modified_sentences))