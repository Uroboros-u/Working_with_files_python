from pathlib import Path

path = Path('Alice_in_Wonderland.txt')

try:
    content = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print("Sorry I can't find your file!")
else:
    words = content.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")