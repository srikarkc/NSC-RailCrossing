# Importing the json module
import json

# Opening the json module and saving the data as Python dictionary
with open('new-folder\googleOutput.json') as json_file:
    data = json.load(json_file)

# Find out how many labelAnnotations are there.
range_of_data = len(data['localizedObjectAnnotations'])

# List of all the things to keep count of.
countable_list = ['person']

# Initiate a counter
counter = 0

# boundingPoly in localizedObjectAnnotations

# Looping through the dictionary - labelAnnotations.
for i in range(0,range_of_data):
    description = data['localizedObjectAnnotations'][i]['name']
    #print(description)
    if description.lower() in countable_list:
        counter += 1

print(f'Number of person: {counter}')


#for i in data['labelAnnotations']