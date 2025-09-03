#10-8
from pathlib import Path

lists_of_path = ['dogs.txt', 'cats.txt']

for one_path in lists_of_path:
    path = Path(one_path)
    try:
            content = path.read_text()
    except FileNotFoundError:
        print(f"""I couldn't find "{path}" file.""")
    else:
        print(f"The {path} file has this content inside:\n{content}")