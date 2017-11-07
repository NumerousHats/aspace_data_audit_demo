#Python3

import requests
import json
import csv

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

def update_pub_status():
    values = login()
    csvfile = opencsv()
    for row in csvfile:
        ao_uri = row[0]
        #1 for publish, 0 for unpublish
        updated_status = row[1]
        ao_json = requests.get(values[0] + ao_uri, headers=values[1]).json()
        if updated_status == '1':
            ao_json['publish'] = True
        elif updated_status == '0':
            ao_json['publish'] = False
        ao_data = json.dumps(ao_json)
        ao_update = requests.post(values[0] + ao_uri, headers=values[1], data=ao_data).json()
        print(ao_update)

#uses persistent ID as key; can also do this for resource_level notes...or abstract and use for both.
def update_note_pub_status():
    values = login()
    csvfile = opencsv()
    for row in csvfile:
        uri = row[0]
        persistent_id = row[1]
        updated_status = row[2]
        json = requests.get(values[0] + uri, headers=values[1]).json()
        for note in json['notes']:
            if note['persistent_id'] == persistent_id:
                if updated_status == '1':
                    note['publish'] = True
                elif updated_status == '0':
                    note['publish'] = False
        data = json.dumps(json)
        ao_update = requests.post(values[0] + uri, headers=values[1], data=data).json()
        print(ao_update)