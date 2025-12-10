from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser()
parser.add_argument("path", type=str, help="path to the txt file")
parser.add_argument("-t", "--text", action="store_true", help="print the most repeated words.")


args = parser.parse_args()

# Checking if path exist
file_path = Path(args.path)
if file_path.exists():
    with open(args.path, 'r') as f:
        content = f.read()
else:
    print(f"this path '{file_path}' does not exist!!!")
    raise SystemExit(1)

# convert text in lower case
content = content.lower()

#remove ponctuation only keep a-z and spaces
content = ''.join(char if char.isalpha() or char.isspace() else ' ' for char in content)

# count frequency of each words
words = content.replace("\n", "").split(" ")

word_count = {}
for word in words:
    if word: # Skip empty strings
        word_count[word] = word_count.get(word, 0) + 1


# print the top 10 most frequent word in descending order
items = list(word_count.items())

for i in range(1, len(items)):
    key_item = items[i]
    key = key_item[1]
    j = i - 1

    while j >= 0 and key > items[j][1]:
        items[j+1] = items[j]
        j-=1
    items[j+1] = key_item


if args.text:
    for item, i in zip(items, range(1, 11)):
        print(f"{i}. {item[0]}: {item[1]}")
else:
    print(content)