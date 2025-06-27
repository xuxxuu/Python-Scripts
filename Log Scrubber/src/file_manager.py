from abc import ABC, abstractmethod
from pathlib import Path
from patterns import re_replacement_pairs
from scrubber import scrub_line


class ScrubberStrategy(ABC):
    
    @abstractmethod
    def scrub(self, path: Path):
        pass


class ScrubberStartsAtFile(ScrubberStrategy):

    def scrub(self, path: Path):
        """scrubs the file"""
        with open(path) as f:
            text = f.read().strip().splitlines()
        for line in text:
            for pair in re_replacement_pairs:
                text = scrub_line(line, pair)
                print(text)


class ScrubberStartsAtDir(ScrubberStrategy):

    def scrub(self, path: Path):
        """scrubs the directory"""


def build_scrubber(path: Path) -> ScrubberStrategy | None:
    if path.is_dir():
        return ScrubberStartsAtDir()
    elif path.is_file():
        return ScrubberStartsAtFile()
    else:
        return None