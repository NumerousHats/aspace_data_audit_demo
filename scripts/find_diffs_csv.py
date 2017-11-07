import csv
#reads a CSV and finds any rows that are in one CSV but not the other

#csv with fewer lines - the "old" file
csv_one = input('Please enter path to CSV1: ')
#csv with more lines - the "new" file
csv_two = input('Please enter path to CSV2: ')

with open(csv_one, 'r', encoding='utf-8') as c1, open(csv_two, 'r', encoding='utf-8') as c2:
    file_one = c1.readlines()
    file_two = c2.readlines()

with open('matches.csv', 'w', encoding='utf-8') as outfile1, open('diffs.csv', 'w', encoding='utf-8') as outfile2:
    for line in file_two:
#        print(line)
        if line in file_one:
            outfile1.write(line)
        elif line not in file_one:
            outfile2.write(line)

print('All Done! Check outfiles for results.')
            
            