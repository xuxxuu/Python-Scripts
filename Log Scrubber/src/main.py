from pathlib import Path

cwd = Path.cwd()
target = Path(cwd / input("File you would like to scrub: "))
if target.is_file():
    # scrub
    ...
elif target.is_dir():
    # walk file tree
    ...