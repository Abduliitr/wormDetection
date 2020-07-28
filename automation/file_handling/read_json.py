###This file is used to read the data from a json file and then it could be used to further process the data.

###Import Libraries
import json

###Open the desired Json file
with open("worms_data_file.json", 'r') as fp:
        json_data = json.load(fp)


###Print the required Data
print(json_data)
print("The following are the coordinates of the worms found in the auto-detection: ")
print(json_data['worms'])
print("The following are the coordinates of the non_worms found in the auto-detection: ")
print(json_data['non_worms'])
# print("Thanks You")