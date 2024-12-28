

import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        fields = line.split(',')
        if len(fields) == 15:
            age = fields[0]
            income = fields[-1]
            if age.isdigit() and int(age) > 25 and income.strip() == '>50K':
                print('%s\t%s' % (income, 1))
