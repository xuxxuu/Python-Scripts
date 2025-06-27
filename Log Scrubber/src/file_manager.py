from abc import ABC, abstractmethod
from pathlib import Path
from patterns import re_replacement_pairs
from scrubber import scrub_line
import chardet


class ScrubberStrategy(ABC):
    
    def detect_encoding(self, filepath: Path):
        with open(filepath, "rb") as f:
            raw_data = f.read()
            encoding = chardet.detect(raw_data)["encoding"]
            return encoding

    def handle_file(self, path: Path):
        encoding = self.detect_encoding(path)
        with open(path, encoding=encoding) as f:
            text = f.read().strip().splitlines()
        for line in text:
            for pair in re_replacement_pairs:
                line = scrub_line(line, pair)
            print(line)

    @abstractmethod
    def scrub(self, path: Path):
        pass


class ScrubberStartsAtFile(ScrubberStrategy):
    """No extra methods needed. Just scrub the file"""
    def scrub(self, path: Path):
        """scrubs the file"""
        self.handle_file(path)


class ScrubberStartsAtDir(ScrubberStrategy):
    def walk(self, path: Path):
        for dirpath, _, filenames in path.walk():
            for filename in filenames:
                yield dirpath / filename

    def scrub(self, path: Path):
        """scrubs the file"""
        for filepath in self.walk(path):
            self.handle_file(filepath)


class LogScrubber:
    def __init__(self, path: Path) -> None:
        self.path = path.resolve()
        if self.path.is_dir():
            self.scrubber = ScrubberStartsAtDir()
        elif self.path.is_file():
            self.scrubber = ScrubberStartsAtFile()

    def scrub_logs(self):
        self.scrubber.scrub(self.path)