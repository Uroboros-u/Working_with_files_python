#Exercises 10-12
from pathlib import Path
import json

def get_number(path):
    return json.loads(path.read_text())

def write_number(path, number):
    number = json.dumps(number)
    path.write_text(number)

def main():
    path = Path('favourite_number.json')
    if path.exists():
        number = get_number(path)
        print(f"I know your favorite number! It’s {number}.")
    else:
        number = input("Write your favourite number and I remember it: ")
        write_number(path, number)

main()



