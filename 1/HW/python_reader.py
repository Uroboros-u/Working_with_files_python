from pathlib import Path

#10-1
path = Path('learning_python.txt')
content = path.read_text().strip()
print(content, '\n')

for line in content.splitlines():
    print('- ', line)


#10-2
print('\n Ex. 10-2')
for line in content. splitlines():
    print('- ', line.replace('Python', 'C'))



