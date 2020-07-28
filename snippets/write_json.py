## this file collects the data and saves them into a JSON format file

## NEW DATA FORMAT
## "worm": [ [frame_name, x,y,w,h,] , [] , ......... ]
## "non_worm" : [ [ frame_name, x,y,w,h, ] , [] , ......... ]


## Import Libraries
import json

def create_json(file_name,list1, list2):
        worms_data = list1
        non_worms_data = list2

        ##Append to Json Data
        json_data = {}
        json_data["worms"] = worms_data
        json_data["non_worms"] = non_worms_data

        ####For Debugging Purpose
        # print(json_data)
        dump_json(file_name,json_data)

def create_json(file_name,list1):
        data = list1

        ##Append to Json Data
        json_data = {}
        json_data["all data"] = data
        
        ####For Debugging Purpose
        # print(json_data)

        dump_json(file_name,json_data)


def dump_json(file_name,json_data):
        ##Write the JSON to a file
        with open(file_name, 'w') as outfile:  
                json.dump(json_data, outfile)
