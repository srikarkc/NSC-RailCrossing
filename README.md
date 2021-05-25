# NSC-RailCrossing

The following is the original code to count the number of vehicles in an image based on the json output from the Google API.

# Importing the json module
import json

# Opening the json module and saving the data as Python dictionary
with open('googleOutput.json') as json_file:
    data = json.load(json_file)

# Find out how many labelAnnotations are there.
range_of_data = len(data['labelAnnotations'])

# List of all the things to keep count of.
countable_list = ['car', 'land vehicle', 'motor vehicle', 'kit car', 'mid-size car', 'city car', 'compact mpv', 'full-size car', 'personal luxury car']

# Initiate a counter
counter = 0

# Looping through the dictionary - labelAnnotations.
for i in range(0,range_of_data):
    description = data['labelAnnotations'][i]['description']
    if description.lower() in countable_list:
        counter += 1

print(f'Number of items: {counter}')


#for i in data['labelAnnotations']
