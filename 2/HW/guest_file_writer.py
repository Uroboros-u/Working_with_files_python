from pathlib import Path

path = Path('guest.txt')

#10-4
guest = input('Write down your name: ')
path.write_text(guest)

#10-5
guest = ''
while True:
    guest += input('Write down your name: ') + '\n'
    path.write_text(guest)

    add_user = input('If you want to add one more guest write "Add" and press enter: ')
    if add_user != 'Add':
        break
