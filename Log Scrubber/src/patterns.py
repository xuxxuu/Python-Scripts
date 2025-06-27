import re

ANY_IP = re.compile(r"(\d{1,3}\.){3}\d{1,3}")

DOMAINS = [
    re.compile(r"example1\.com"),
    re.compile(r"example2\.com"),
    re.compile(r"example3\.com"),
    re.compile(r"example4\.com"),
    re.compile(r"example5\.com"),
    re.compile(r"example6\.com")
]

REPLACEMENTS = [
    "replacement1.com",
    "replacement2.com",
    "replacement3.com",
    "replacement4.com",
    "replacement5.com",
    "replacement6.com"
]

re_replacement_pairs = [
    (re_string, replacement)
    for re_string, replacement
    in zip(DOMAINS, REPLACEMENTS)
]