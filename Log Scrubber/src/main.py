from pathlib import Path
from file_manager import LogScrubber

def main():
    cwd = Path.cwd()
    target = Path(cwd / input("File/Dir you would like to scrub: ".strip()))
    scrubber = LogScrubber(target)
    scrubber.scrub_logs()


if __name__ == '__main__':
    main()