import re
from patterns import re_replacement_pairs


def scrub_line(line: str, pair: tuple[re.Pattern, str]):
    pattern, replacement = pair
    line = re.sub(pattern, replacement, line)
    return line


if __name__ == '__main__':
    text = "I want to visit the example1.com and that would be awesome!"
    for pair in re_replacement_pairs:
        text = scrub_line(text, pair)
        print(text)
        exit()