import csv
#import collections

csv_in = input('Please enter path to CSV: ')

with open(csv_in, 'r', encoding='utf-8') as c:
    notes = c.readlines()

with open('dupes.csv', 'w', encoding='utf-8') as outfile:
    seen = set()
    for n in notes:
        if n in seen:
#            print("duplicate: " + n)
            outfile.write(n)
        else:
            seen.add(n)

print('All Done! Check outfile for results.')