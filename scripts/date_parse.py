from dateutil.parser import parse
import csv

csvin = input('Please enter path to input csv: ')
file = open(csvin, 'r', encoding='utf-8')
reader = csv.reader(file)
next(reader, None)
for row in reader:
    date_expression = row[0]
    try:
        parse_it = parse(date_expression)
        print(parse_it)
    except ValueError:
        print('String does not contain a parse-able date: ' + row[0])
        continue

