from pathlib import Path

#10-10
path = Path('The_picture_of_Dorian_Gray.txt')
try:
    content = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print('Wrong path!')
else:
    times = content.lower().count('the ')
    print(times)