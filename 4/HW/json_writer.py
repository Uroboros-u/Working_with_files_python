1

from pathlib import(Path)
import json

path = Path('favourite_number.json')
number = json.dumps(input("write your favourite number: "))
path.write_text(number)

