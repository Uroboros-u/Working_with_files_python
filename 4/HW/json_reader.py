#Exercises 10-11 (part2) Json reader

from pathlib import(Path)
import json

path = Path('favourite_number.json')
number = json.loads(path.read_text())
print(f"I know your favorite number! It’s {number}.")
