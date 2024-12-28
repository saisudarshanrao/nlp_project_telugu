

import sys

total_count = 0

for line in sys.stdin:
    line = line.strip()
    income, count = line.split('\t', 1)
    try:
        count = int(count)
        total_count += count
    except ValueError:
        pass

print(total_count)
