import sys
import json
from PyQt4 import QtCore, QtGui
import cv2
from final import Ui_MainWindow
i=1
file_name = r"data.json"
worm=[]
nonworm=[]
json_data={}
l=[[410, 239, 3, 2], [388, 239, 3, 2], [372, 239, 3, 2], [398, 238, 3, 3], [361, 238, 3, 3], [353, 238, 3, 3], [326, 238, 3, 3], [316, 238, 3, 3], [253, 238, 3, 3], [230, 238, 3, 3], [103, 238, 3, 3], [70, 238, 3, 3], [64, 238, 3, 3], [13, 238, 3, 3], [196, 237, 5, 4], [162, 237, 3, 4], [3, 237, 5, 4], [271, 236, 6, 5], [260, 236, 5, 5], [240, 236, 3, 3], [122, 236, 8, 5], [111, 236, 3, 3], [417, 235, 5, 6], [291, 234, 11, 7], [24, 234, 3, 3], [221, 233, 3, 3], [411, 231, 3, 3], [372, 231, 3, 3], [366, 231, 3, 3], [281, 231, 3, 3], [275, 231, 3, 3], [0, 231, 1, 3], [287, 230, 2, 3], [128, 230, 3, 3], [407, 228, 3, 3], [307, 228, 3, 3], [342, 226, 3, 3], [390, 225, 3, 3], [375, 225, 3, 3], [399, 224, 3, 3], [196, 224, 3, 3], [11, 222, 3, 3], [3, 222, 4, 7], [355, 221, 3, 3], [230, 220, 4, 3], [21, 220, 6, 8], [25, 219, 1, 1], [180, 218, 3, 8], [289, 216, 10, 9], [177, 216, 1, 1], [369, 215, 3, 3], [179, 214, 1, 1], [45, 212, 3, 3], [65, 211, 3, 3], [22, 209, 3, 3], [50, 207, 3, 3], [381, 206, 8, 3], [177, 201, 2, 2], [2, 200, 8, 10], [70, 199, 3, 3], [334, 198, 3, 3], [11, 198, 3, 3], [110, 197, 5, 7], [389, 196, 3, 3], [279, 193, 3, 3], [263, 193, 3, 3], [398, 189, 3, 3], [135, 189, 9, 13], [365, 186, 3, 3], [412, 183, 10, 7], [297, 183, 3, 3], [230, 183, 3, 3], [369, 182, 5, 3], [191, 182, 3, 3], [119, 182, 3, 5], [412, 176, 1, 1], [236, 175, 3, 3], [2, 175, 4, 4], [414, 174, 1, 1], [285, 174, 7, 18], [2, 174, 15, 19], [6, 172, 1, 1], [383, 170, 4, 7], [8, 170, 1, 1], [28, 169, 6, 5], [335, 168, 3, 3], [417, 166, 3, 3], [214, 164, 3, 3], [155, 164, 12, 8], [417, 160, 3, 3], [12, 160, 16, 16], [410, 159, 3, 3], [29, 159, 3, 3], [27, 153, 3, 3], [2, 153, 8, 11], [15, 151, 5, 7], [83, 147, 3, 3], [6, 147, 7, 5], [256, 146, 3, 3], [191, 143, 3, 3], [19, 142, 3, 3], [374, 141, 4, 5], [415, 139, 3, 2], [372, 136, 3, 3], [280, 135, 3, 3], [265, 135, 6, 4], [253, 133, 3, 3], [262, 132, 3, 3], [227, 131, 5, 10], [27, 131, 3, 3], [414, 127, 3, 3], [249, 127, 3, 3], [130, 127, 3, 3], [14, 127, 3, 3], [354, 126, 7, 11], [42, 126, 3, 3], [279, 125, 3, 3], [52, 125, 4, 3], [32, 124, 3, 3], [0, 123, 13, 20], [6, 134, 5, 5], [179, 119, 3, 3], [154, 119, 3, 3], [126, 115, 3, 3], [284, 113, 10, 12], [102, 112, 3, 3], [71, 112, 3, 3], [349, 111, 3, 3], [246, 111, 3, 3], [164, 110, 3, 3], [143, 110, 3, 3], [27, 110, 3, 3], [410, 108, 3, 3], [340, 108, 3, 3], [251, 108, 1, 1], [373, 107, 6, 13], [253, 106, 1, 1], [120, 104, 3, 3], [419, 103, 3, 3], [150, 103, 3, 3], [212, 101, 5, 4], [224, 98, 6, 4], [176, 98, 10, 10], [40, 97, 3, 4], [129, 94, 3, 3], [30, 94, 3, 3], [406, 90, 5, 8], [135, 88, 3, 3], [228, 86, 6, 7], [181, 86, 3, 3], [59, 86, 3, 3], [110, 84, 3, 3], [37, 83, 6, 6], [246, 82, 9, 7], [332, 81, 3, 3], [28, 79, 3, 3], [36, 77, 3, 3], [0, 77, 3, 3], [127, 73, 3, 3], [221, 71, 3, 3], [45, 71, 3, 3], [170, 70, 3, 3], [76, 70, 3, 3], [87, 68, 11, 16], [152, 66, 3, 3], [296, 65, 3, 3], [225, 65, 3, 3], [412, 64, 3, 3], [143, 64, 3, 3], [158, 63, 3, 3], [416, 58, 6, 4], [188, 58, 3, 3], [378, 57, 3, 3], [409, 55, 3, 3], [158, 54, 3, 3], [144, 54, 3, 3], [100, 54, 2, 2], [93, 54, 3, 3], [126, 52, 3, 3], [326, 51, 3, 3], [351, 49, 3, 3], [64, 49, 3, 3], [270, 48, 3, 3], [142, 48, 3, 3], [213, 46, 3, 3], [30, 46, 3, 3], [410, 44, 4, 8], [378, 44, 3, 3], [105, 44, 3, 3], [6, 94, 7, 8], [3, 88, 5, 6], [12, 75, 6, 5], [6, 59, 9, 7], [15, 57, 6, 6], [24, 56, 11, 8], [417, 43, 3, 3], [217, 42, 3, 3], [63, 42, 3, 3], [269, 40, 3, 3], [30, 40, 3, 3], [20, 40, 3, 3], [343, 39, 3, 3], [276, 39, 3, 3], [169, 39, 8, 9], [334, 38, 3, 3], [154, 38, 3, 3], [145, 38, 3, 3], [356, 37, 6, 8], [212, 37, 4, 5], [2, 37, 12, 8], [343, 33, 3, 3], [140, 33, 3, 3], [3, 33, 2, 3], [380, 32, 7, 10], [353, 32, 3, 3], [54, 31, 1, 1], [30, 31, 3, 3], [15, 31, 3, 3], [8, 31, 3, 3], [407, 30, 4, 7], [393, 30, 8, 3], [171, 30, 3, 3], [41, 30, 3, 3], [241, 29, 8, 3], [114, 29, 25, 21], [56, 29, 1, 1], [76, 28, 5, 5], [50, 28, 3, 3], [279, 27, 3, 3], [71, 26, 3, 3], [35, 26, 3, 3], [110, 25, 3, 3], [86, 25, 3, 6], [395, 23, 3, 3], [175, 23, 13, 11], [116, 23, 3, 3], [413, 22, 3, 3], [388, 22, 3, 3], [337, 22, 3, 3], [63, 22, 3, 3], [403, 21, 5, 4], [155, 21, 3, 3], [143, 21, 3, 7], [79, 21, 3, 3], [0, 21, 9, 11], [309, 20, 3, 3], [295, 20, 11, 6], [14, 20, 3, 3], [347, 19, 3, 3], [333, 19, 3, 3], [95, 19, 3, 3], [7, 19, 3, 3], [84, 18, 6, 3], [55, 18, 6, 3], [304, 17, 3, 3], [122, 17, 15, 9], [209, 16, 31, 20], [200, 16, 3, 8], [108, 16, 3, 7], [2, 16, 3, 2], [319, 15, 3, 3], [151, 15, 6, 4], [98, 15, 3, 3], [77, 15, 3, 3], [205, 14, 6, 8], [188, 14, 3, 3], [139, 14, 3, 2], [62, 14, 3, 3], [28, 14, 8, 7], [343, 13, 3, 3], [238, 13, 3, 3], [42, 13, 9, 4], [114, 12, 5, 5], [93, 12, 3, 3], [54, 12, 3, 3], [390, 11, 6, 5], [366, 11, 3, 3], [373, 9, 14, 10], [99, 9, 3, 3], [263, 8, 4, 3], [200, 8, 4, 3], [139, 7, 3, 3], [124, 6, 3, 3], [413, 5, 9, 17], [110, 5, 3, 3], [7, 4, 1, 1], [395, 3, 19, 15], [342, 3, 3, 3], [326, 2, 3, 3], [184, 2, 3, 3], [153, 2, 3, 3], [103, 2, 5, 3], [382, 0, 10, 10], [370, 0, 3, 4], [356, 0, 5, 4], [339, 0, 3, 1], [294, 0, 19, 11], [301, 0, 3, 1], [284, 0, 2, 1], [277, 0, 3, 1], [252, 0, 3, 3], [239, 0, 10, 9], [220, 0, 10, 10], [189, 0, 11, 5], [179, 0, 3, 1], [172, 0, 4, 3], [160, 0, 7, 5], [141, 0, 6, 2], [132, 0, 3, 2], [125, 0, 3, 1], [118, 0, 5, 5], [81, 0, 14, 14], [34, 0, 9, 11], [28, 0, 8, 6], [19, 0, 3, 1], [0, 0, 26, 14]]
# class Main(QtGui.QMainWindow, Ui_MainWindow):
class Main(QtWidgets.QMainWindow, Ui_MainWindow):    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        global i
        global file_name
        global json_data
        self.setupUi(self)


    def slot1(self):
        pic = QtGui.QLabel(self)
        pic.setPixmap(QtGui.QPixmap(r"pic2.png"))
        pic.move(200,120)
        pic.resize(70,70)
        pic.show()

    def slot2(self):
        pic = QtGui.QLabel(self)
        pic.setPixmap(QtGui.QPixmap(r"pic1.png"))
        pic.move(490,120)
        pic.resize(70,70)
        pic.show()

    '''def slot3(self):
        global i
        global worm
        count=0
        pic = QtGui.QLabel(self)
        pic.setPixmap(QtGui.QPixmap(r"pic"+str(i-1)+".png"))
        pic.move(300,300)
        pic.resize(70,70)
        pic.show()
        i=i-1'''

    def slot3(self):
        global i
        global l
        MPx = l[i-1][0]
        MPy = l[i-1][1]
        trows = l[i-1][2]
        tcols = l[i-1][3]
        img = cv2.imread('pic1.png')
        cv2.rectangle(img, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
        cv2.imshow('output',img)
        cv2.waitKey(0)
        img = cv2.imread('pic1.png',cv2.IMREAD_UNCHANGED)
        crop_img = img[MPy:MPy+tcols, MPx:MPx+trows]
        scale_percent = 1500
        width = int(crop_img.shape[1] * scale_percent / 100)
        height = int(crop_img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(crop_img, dim, interpolation = cv2.INTER_AREA)
        cv2.imshow("Worm", resized)
        cv2.waitKey(0)
        
        i=i-1


    def slot4(self):
        global i
        global l
        MPx = l[i+1][0]
        MPy = l[i+1][1]
        trows = l[i+1][2]
        tcols = l[i+1][3]
        img = cv2.imread('pic1.png')
        cv2.rectangle(img, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
        cv2.imshow('output',img)
        cv2.waitKey(0)
        img = cv2.imread('pic1.png',cv2.IMREAD_UNCHANGED)
        crop_img = img[MPy:MPy+tcols, MPx:MPx+trows]
        scale_percent = 1500
        width = int(crop_img.shape[1] * scale_percent / 100)
        height = int(crop_img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(crop_img, dim, interpolation = cv2.INTER_AREA)
        cv2.imshow("Worm", resized)
        cv2.waitKey(0)
        i=i+1
        

    '''def slot4(self):
        global i
        pic = QtGui.QLabel(self)
        pic.setPixmap(QtGui.QPixmap(r"pic"+str(i+1)+".png"))
        pic.move(300,300)
        pic.resize(70,70)
        pic.show()
        i=i+1'''

    def slot5(self):
        #print("hello")
        global i
        global worm
        global nonworm
        #print(i)
        count=0
        for j in worm:
            if j==i:
                count = count+1
        if count==0:
            worm.append(i)
        count=0
        for j in nonworm:
            if j==i:
                count = count+1
        if count>0:
            del nonworm[nonworm.index(i)]
        self.slot7


    def slot6(self):
        #print("bye")
        global i
        global worm
        global nonworm
        #xprint(i)
        count=0
        for j in nonworm:
            if j==i:
                count = count+1
        if count==0:
            nonworm.append(i)
        count=0
        for j in worm:
            if j==i:
                count = count+1
        if count>0:
            del worm[worm.index(i)]
        self.slot7

    def slot7(self):
        global worm
        global nonworm
        print(worm)
        print(nonworm)


    def create_json():
        global worm
        global nonworm
        global file_name
        global json_data 
        json_data = {}
        json_data["worms"] = worm
        json_data["non_worms"] = nonworm
        dump_json()

    def create_json():
        global file_name
        global worm
        global json_data
        data = worm
        json_data = {}
        json_data["all data"] = data
        dump_json(file_name,json_data)


    def dump_json():
        global file_name
        global json_data
        with open(file_name, 'w') as outfile:  
                json.dump(json_data, outfile)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())