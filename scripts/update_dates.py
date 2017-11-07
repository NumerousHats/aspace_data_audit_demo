#python 3

import requests
import csv
import json

def login():
    api_url = input('Please enter the ArchivesSpace API URL: ')
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    auth = requests.post(api_url+'/users/'+username+'/login?password='+password).json()
    #if session object is returned then login was successful; if not it failed.
    if 'session' in auth:
        session = auth["session"]
        headers = {'X-ArchivesSpace-Session':session}
        print('Login successful!')
        return (api_url, headers)
    else:
        print('Login failed! Check credentials and try again')
        return

def opencsv():
    '''This function opens a csv file'''
    input_csv = input('Please enter path to CSV: ')
    file = open(input_csv, 'r', encoding='utf-8')
    csvin = csv.reader(file)
    next(csvin, None)
    return csvin

def parse_dates():
	values = login()
	reader = opencsv()
	for row in reader:
		URI = row[1]
		json_data = requests.get(values[0] + URI, headers=values[1]).json()
		json_post = requests.post(values[0]  + URI, headers=values[1], data=json.dumps(json_data)).json()
		print(json_post)
		
parse_dates()

