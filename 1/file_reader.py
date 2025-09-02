from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
print(lines)

pi_string = ''

for line in lines:
    pi_string += line.lstrip()

print(pi_string)


