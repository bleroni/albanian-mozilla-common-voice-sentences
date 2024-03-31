from datasets import load_dataset

dataset = load_dataset("bleroni/kosovo-government-contract-titles", split="train")
# ds = load_dataset("bleroni/kosovo_institution_names", split="train")

list_dataset = dataset.to_list()
for index, row in enumerate(list_dataset[:5]):
  print(index, row)



