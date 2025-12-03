from argparse import ArgumentParser
from string import punctuation
from pprint import pprint
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
for punctuation in punctuation:
    for i, element in enumerate(content):
        if punctuation == element:
            content = content[:i] + " " + content[i+1:]

# count frequency of each words
words = content.replace("\n", "").split(" ")

word_count = {}
for orig in words:
    count = 0
    for fake in words:
        if orig == fake:
            count+=1
    word_count[f"{orig}"] = count


# print the top 10 most frequent word in descending order
counts =list(word_count.values())
for i in range(len(counts) - 1):
    min_idx = i

    for j in range(i+1, (len(counts) - 1)):
        if counts[min_idx] < counts[j]:
            min_idx = j
    
    counts[min_idx], counts[i] = counts[i], counts[min_idx]
    words[min_idx], words[i] = words[i], words[min_idx]


most_10 = {}
index = 1
for key, value in zip(words, counts):
    if index <= 10:
        most_10[key] =  value
        index+=1
        print(key)
        print(len(most_10))


if args.text:
    print(f"\n{content}")
else:
    print(len(most_10))
    for i, element in enumerate(most_10):
        print( f"{i+1} {element}: {most_10[element]}" )