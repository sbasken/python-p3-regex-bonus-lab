import re

my_pattern = r"[^\s\"!\?][\w\'\s\,]{23,}[\.\?]"
my_regex = re.compile(my_pattern)

