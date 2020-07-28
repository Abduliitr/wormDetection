### Get list of all the coordinates along with the frame label (ABDUL's part)
## this file collects the data and saves them into a JSON format file


## ## OLD DATA FORMAT
## "worm": [ [ label_number, (coordinate 1 of rectangle),(coordinate 2 of rectangle),(coordinate 3 of rectangle),(coordinate 4 of rectangle), area ] , [] , ......... ]
## "non_worm" : [ [ label_number, (coordinate 1 of rectangle),(coordinate 2 of rectangle),(coordinate 3 of rectangle),(coordinate 4 of rectangle), area ] , [] , ......... ]


## NEW DATA FORMAT
## "worm": [ [frame_name, x,y,w,h,] , [] , ......... ]
## "non_worm" : [ [ frame_name, x,y,w,h, ] , [] , ......... ]


## Import Libraries
import json


## Testing DATA FOR WORMS AND NON_WORMS
worms_coordinates = [ ["frame1", 1, 2, 3, 4] , ["frame2", 2, 3, 4, 5] , ["frame3", 3, 4, 5, 6] ]

non_worms_coordinates = [ ["framea", 1, 2, 3, 0] , ["frameb", 2, 3, 4, 0] , ["framec", 3, 4, 5, 0] ]


worms_data = []
non_worms_data = []

##Read the lists

for i in range(len(worms_coordinates)):
    # print(i)
    worms_data.append(worms_coordinates[i])

for i in range(len(non_worms_coordinates)):
    # print(i)
    non_worms_data.append(non_worms_coordinates[i])


####For Debugging Purpose
# print(worms_data)
# worms_data.append(["frame_new, 00, 00, 00, 00"])
# print(worms_data)
# print(worms_coordinates)
# print(worms_coordinates)
#print(non_worms_coordinates)

##Append to Json Data
json_data = {}

json_data["worms"] = worms_data
json_data["non_worms"] = non_worms_data


####For Debugging Purpose
print(json_data)


##Write the JSON to a file
with open('worms_data_file.json', 'w') as outfile:  
        json.dump(json_data, outfile)