from pathlib import Path
path = Path("my_name.txt")

contents = path.read_text()
print(contents)

new_path = Path("new_file.txt")
new_path.write_text("Paris 123")

