#Program created to help make routing of robot quicker and more efficient
#By clicking from node to node, this program compiles all the necessary functions for the robot based off of the hard coding done using RobotC
from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk
import sys,ctypes,os
from collections import namedtuple

Node = namedtuple("Node","name x1 y1 x2 y2")
nList = [Node("0",110,30,130,48),Node("1",47,8,67,28),Node("2",25,267,44,290),Node("3",153,295,169,314),Node("4",270,295,289,313),Node("5",212,254,233,265),Node("6",235,230,253,244),Node("7",234,170,253,185),Node("8",235,92,256,108),Node("9",257,7,275,26),Node("10",321,80,339,96),Node("11",258,48,277,60),Node("12",286,275,310,291),Node("13",385,203,404,217),Node("14",407,148,424,165),Node("15",474,58,490,75),Node("16",494,38,513,53),Node("17",493,128,511,143),Node("18",494,203,512,217),Node("19",472,222,489,239),Node("20",494,276,513,290),Node("21",516,7,535,27),Node("22",516,148,536,167),Node("23",576,57,595,76),Node("24",576,221,595,234),Node("25",576,295,595,313),Node("26",599,243,617,258),Node("27",600,170,618,184),Node("28",600,80,618,93),Node("29",599,31,618,44),Node("30",622,148,637,164),Node("31",728,8,746,26),Node("32",706,40,725,53),Node("33",681,58,703,76),Node("34",706,90,724,105),Node("35",669,130,688,145),Node("36",685,185,705,202),Node("37",708,203,726,216),Node("38",684,221,703,239),Node("39",706,276,725,290),Node("40",767,148,783,165),Node("41",761,58,778,75),Node("42",781,30,800,46),Node("43",781,242,799,257),Node("44",834,57,851,75),Node("45",833,221,850,239),Node("46",877,9,893,26),Node("47",852,39,874,55),Node("48",855,129,874,142),Node("49",855,203,874,217),Node("50",855,277,874,290),Node("51",761,294,777,312),Node("52",925,294,942,312),Node("53",945,243,964,257),Node("54",945,170,964,185),Node("55",877,148,895,166),Node("56",968,148,984,166),Node("57",924,221,942,239),Node("58",1037,9,1052,26),Node("59",1015,39,1034,53),Node("60",995,59,1012,76),Node("61",1017,131,1034,144),Node("62",1015,200,1036,215),Node("63",992,221,1012,240),Node("64",1014,276,1034,290),Node("65",1105,293,1124,311),Node("66",1128,243,1146,257),Node("67",1128,79,1146,97),Node("68",1128,30,1146,46),Node("69",1106,59,1126,77),Node("70",1109,220,1125,239),Node("71",1220,31,1239,47),Node("72",1194,221,1215,239),Node("73",1218,242,1239,258),Node("74",1197,295,1215,312),Node("75",1174,272,1194,290),Node("1A",69,271,89,291),Node("1B",92,271,112,291),Node("1C",114,271,134,291),Node("1D",137,271,157,291),Node("2A",400,78,421,100),Node("2B",423,78,443,100),Node("2C",447,78,467,100),Node("3A",415,198,437,218),Node("3B",439,198,459,218),Node("3C",462,198,482,218),Node("4A",515,78,536,100),Node("4B",515,102,536,122),Node("4C",515,125,536,145),Node("5A",832,78,852,98),Node("5B",832,102,852,122),Node("5C",832,125,852,145),Node("6A",877,198,897,217),Node("6B",901,198,921,217),Node("6C",922,198,942,217),Node("7A",992,78,1012,100),Node("7B",992,102,1012,122),Node("7C",992,128,1012,148),Node("8A",1037,78,1057,100),Node("8B",1060,78,1080,100),Node("8C",1083,78,1103,100),Node("8D",1106,78,1126,100),Node("9A",1196,60,1215,81),Node("9B",1196,83,1215,103),Node("9C",1196,106,1215,126),Node("9D",1196,128,1215,148),Node("9E",1196,150,1215,170),Node("10A",1242,60,1261,81),Node("10B",1242,83,1261,103),Node("10C",1242,106,1261,126),Node("10D",1242,128,1261,148),Node("10E",1242,150,1261,170)]

Connection = namedtuple("Connect","nodes coord func")
cList = [Connection("01","120,42,120,17,35,17","turnLeft();Drive_white();"),Connection("12","35,17,35,304","turnLeft();Drive_white();"),Connection("23","35,304,183,304","turnLeft();Drive_white();"),Connection("21A","35,304,80,304,80,280","turnLeft();Park_left(1);"),Connection("21B","35,304,103,304,103,280","turnLeft();Park_left(2);"),Connection("21C","35,304,125,304,125,280","turnLeft();Park_left(3);"),Connection("21D","35,304,147,304,147,280","turnLeft();Park_left(4);"),Connection("34","183,304,303,304","Drive_white();"),Connection("35","183,304,186,283,210,263,245,257","turnLeft();Drive_yellow();"),Connection("425","303,304,608,304","Drive_white();"),Connection("512","245,257,271,259,297,282,303,304","Drive_yellow();"),Connection("612","245,257,271,259,297,282,303,304","turnLeft();Drive_yellow();"),Connection("76","245,199,245,257","Drive_white();"),Connection("719","245,199,392,230,501,230","turnLeft();Drive_white();"),Connection("73A","245,199,426,230,426,208","turnLeft();Park_left(1);"),Connection("73B","245,199,448,230,448,208","turnLeft();Park_left(2);"),Connection("73C","245,199,471,230,471,208","turnLeft();Park_left(3);"),Connection("87","245,114,245,199","Drive_white();"),Connection("810","245,114,279,135,317,120,330,116,328,68","turnLeft();Circle();"),Connection("90","245,17,120,17,120,42","FinishLine();"),Connection("91","245,17,35,17","Drive_white();"),Connection("98","245,17,245,114","turnLeft();Drive_white();"),Connection("1011","328,68,286,48,245,65","Drive_yellow();"),Connection("1015","328,68,501,68","turnRight();Drive_white();"),Connection("102A","328,68,409,68,409,90","turnRight();Parking_right(1);"),Connection("102B","328,68,432,68,432,90","turnRight();Parking_right(2);"),Connection("102C","328,68,455,68,455,90","turnRight();Parking_right(3);"),Connection("118","245,65,245,114","Drive_white();"),Connection("1225","303,304,608,304","turnLeft();Drive_white();"),Connection("1319","392,230,501,230","turnLeft();Drive_white();"),Connection("133A","392,230,426,230,426,208","turnLeft();Park_left(1);"),Connection("133B","392,230,448,230,448,208","turnLeft();Park_left(2);"),Connection("133C","392,230,471,230,471,208","turnLeft();Park_left(3);"),Connection("1413","392,158,392,230","turnLeft();Drive_yellow();"),Connection("1517","503,68,503,158","turnRight();Drive_white();"),Connection("1523","503,68,607,68","Drive_white();"),Connection("154A","503,68,503,94,525,94","turnRight();Park_left(1);"),Connection("154B","503,68,503,113,525,113","turnRight();Park_left(2);"),Connection("154C","503,68,503,136,525,136","turnRight();Park_left(3);"),Connection("1617","503,68,503,158","Drive_white();"),Connection("1623","503,68,607,68","turnLeft();Drive_white();"),Connection("164A","503,68,503,94,525,94","Park_left(1);"),Connection("164B","503,68,503,113,525,113","Park_left(2);"),Connection("164C","503,68,503,136,525,136","Park_left(3);"),Connection("1714","503,158,392,158","turnRight();Drive_yellow();"),Connection("1718","503,158,503,230","Drive_white();"),Connection("1820","503,230,503,304","Drive_white();"),Connection("1824","503,230,608,230","turnLeft();Drive_white();"),Connection("1920","503,230,503,304","turnRight();Drive_white();"),Connection("1924","503,230,608,230","Drive_white();"),Connection("2025","503,304,608,304","turnLeft();Drive_white();"),Connection("219","503,17,245,17","Drive_white();"),Connection("2116","503,17,503,68","turnLeft();Drive_white();"),Connection("2214","503,158,392,158","Drive_yellow();"),Connection("2218","503,158,503,230","turnLeft();Drive_white();"),Connection("2329","608,68,608,17","turnLeft();Drive_white();"),Connection("2333","608,68,714,68","Drive_white();"),Connection("2427","608,230,608,158","turnLeft();Drive_white();"),Connection("2438","608,230,714,230","Drive_white();"),Connection("2526","608,304,608,230","turnLeft();Drive_white();"),Connection("2551","608,304,790,304","Drive_white();"),Connection("2627","608,230,608,158","Drive_white();"),Connection("2638","608,230,714,230","turnRight();Drive_white();"),Connection("2722","608,158,503,158","turnLeft();Drive_white();"),Connection("2728","608,158,608,68","Drive_white();"),Connection("2829","608,68,608,17","Drive_white();"),Connection("2833","608,68,714,68","turnRight();Drive_white();"),Connection("2921","608,17,503,17","turnLeft();Drive_white();"),Connection("3022","608,158,503,158","Drive_white();"),Connection("3028","608,158,608,68","turnRight();Drive_white();"),Connection("3121","714,17,503,17","Drive_white();"),Connection("3132","714,17,714,68","turnLeft();Drive_yellow();"),Connection("3234","714,68,714,118","Drive_yellow();"),Connection("3241","714,68,791,68","turnLeft();Drive_white();"),Connection("3334","714,68,714,118","turnRight();Drive_yellow();"),Connection("3341","714,68,791,68","Drive_white();"),Connection("3435","714,118,684,126,674,158","turnRight();Drive_yellow();"),Connection("3530","674,158,608,158","turnRight();Drive_yellow();"),Connection("3536","674,158,679,181,697,196,714,201","Drive_yellow();"),Connection("3635","714,201,735,199,754,180,758,144,736,120,714,118,684,126,674,158","Drive_yellow();"),Connection("3637","714,201,714,230","turnRight();"),Connection("3739","714,230,714,304","Drive_yellow();"),Connection("3745","714,230,866,230","turnLeft();Drive_white();"),Connection("3839","714,230,714,304","turnRight();Drive_yellow();"),Connection("3845","714,230,866,230","Drive_white();"),Connection("3951","714,304,790,304","turnLeft();Drive_white();"),Connection("4035","758,158,736,120,714,118,684,126,674,158","turnRight();Drive_yellow();"),Connection("4142","791,68,791,17","turnLeft();Drive_white();"),Connection("4144","791,68,866,68","Drive_white();"),Connection("4231","791,17,714,17","turnLeft();Drive_white();"),Connection("4345","790,230,866,230","turnRight();Drive_white();"),Connection("4448","866,68,866,158","turnRight();Drive_white();"),Connection("4460","866,68,1024,68","Drive_white();"),Connection("445A","866,68,866,92,841,92","turnRight();Parking_right(1);"),Connection("445B","866,68,866,109,841,109","turnRight();Parking_right(2);"),Connection("445C","866,68,866,135,841,135","turnRight();Parking_right(3);"),Connection("4550","866,230,866,304","turnRight();Drive_white();"),Connection("4557","866,230,954,230","Drive_white();"),Connection("456A","866,230,889,230,889,206","Park_left(1);"),Connection("456B","866,230,911,230,911,206","Park_left(2);"),Connection("456C","866,230,933,230,933,206","Park_left(3);"),Connection("4631","866,17,714,17","Drive_white();"),Connection("4647","866,17,866,68","turnLeft();Drive_white();"),Connection("4748","866,68,866,158","Drive_white();"),Connection("4760","866,68,1024,68","turnLeft();Drive_white();"),Connection("475A","866,68,866,92,841,92","Parking_right(1);"),Connection("475B","866,68,866,109,841,109","Parking_right(2);"),Connection("475C","866,68,866,135,841,135","Parking_right(3);"),Connection("4840","866,158,758,158","turnRight();Drive_yellow();"),Connection("4849","866,158,866,230","Drive_white();"),Connection("4950","866,230,866,304","Drive_white();"),Connection("4957","866,230,954,230","turnLeft();Drive_white();"),Connection("496A","866,230,889,230,889,206","turnLeft();Park_left(1);"),Connection("496B","866,230,911,230,911,206","turnLeft();Park_left(2);"),Connection("496C","866,230,933,230,933,206","turnLeft();Park_left(3);"),Connection("5052","866,304,954,304","turnLeft();Drive_white();"),Connection("5143","790,304,790,230","turnLeft();Drive_white();"),Connection("5152","790,304,954,304","Drive_white();"),Connection("5253","954,304,954,230","turnLeft();Drive_yellow();"),Connection("5265","954,304,1136,304","Drive_white();"),Connection("5354","954,230,954,158","Drive_yellow();"),Connection("5363","954,230,1024,230","turnRight();Drive_white();"),Connection("5455","954,158,866,158","turnLeft();Drive_white();"),Connection("5540","866,158,758,158","Drive_yellow();"),Connection("5549","866,158,866,230","turnLeft();Drive_white();"),Connection("5655","954,158,866,158","Drive_white();"),Connection("5754","954,230,954,158","turnLeft();Drive_yellow();"),Connection("5763","954,230,1024,230","Drive_white();"),Connection("5846","1024,17,866,17","Drive_white();"),Connection("5859","1024,17,1024,68","turnLeft();Drive_white();"),Connection("5961","1024,68,1024,158","Drive_white();"),Connection("5969","1024,68,1138,68","turnLeft();Drive_white();"),Connection("597A","1024,68,1024,90,1000,90","Parking_right(1);"),Connection("597B","1024,68,1024,110,1000,110","Parking_right(2);"),Connection("597C","1024,68,1024,134,1000,134","Parking_right(3);"),Connection("598A","1024,68,1045,68,1045,90","turnLeft();Parking_right(1);"),Connection("598B","1024,68,1069,68,1069,90","turnLeft();Parking_right(2);"),Connection("598C","1024,68,1091,68,1091,90","turnLeft();Parking_right(3);"),Connection("598D","1024,68,1113,68,1113,90","turnLeft();Parking_right(4);"),Connection("6061","1024,68,1024,158","turnRight();Drive_white();"),Connection("6069","1024,68,1138,68","Drive_white();"),Connection("607A","1024,68,1024,90,1000,90","turnRight();Parking_right(1);"),Connection("607B","1024,68,1024,110,1000,110","turnRight();Parking_right(2);"),Connection("607C","1024,68,1024,134,1000,134","turnRight();Parking_right(3);"),Connection("608A","1024,68,1045,68,1045,90","Parking_right(1);"),Connection("608B","1024,68,1069,68,1069,90","Parking_right(2);"),Connection("608C","1024,68,1091,68,1091,90","Parking_right(3);"),Connection("608D","1024,68,1113,68,1113,90","Parking_right(4);"),Connection("6156","1024,158,954,158","turnRight();Drive_white();"),Connection("6162","1024,158,1024,230","Drive_white();"),Connection("6264","1024,230,1024,304","Drive_white();"),Connection("6270","1024,230,1138,230","turnLeft();Drive_white();"),Connection("6364","1024,230,1024,304","turnRight();Drive_white();"),Connection("6370","1024,230,1138,230","Drive_white();"),Connection("6465","1024,304,1136,304","turnLeft();Drive_white();"),Connection("6566","1136,304,1138,230","turnLeft();Drive_white();"),Connection("6574","1136,304,1226,304","Drive_white();"),Connection("6575","1136,304,1184,304,1184,282","FinishLine();"),Connection("6667","1138,230,1138,68","Drive_white();"),Connection("6672","1138,230,1226,230","turnRight();Drive_white();"),Connection("6768","1138,68,1138,17","Drive_white();"),Connection("6858","1138,17,1024,17","turnLeft();Drive_white();"),Connection("6968","1138,68,1138,17","turnLeft();Drive_white();"),Connection("7067","1138,230,1138,68","turnLeft();Drive_white();"),Connection("7072","1138,230,1226,230","Drive_white();"),Connection("7158","1226,17,1024,17","turnLeft();Drive_white();"),Connection("7271","1226,230,1226,17","turnLeft();Drive_yellow();"),Connection("7210A","1226,230,1226,70,1251,70","turnLeft();Parking_right(1);"),Connection("7210B","1226,230,1226,91,1251,91","turnLeft();Parking_right(2);"),Connection("7210C","1226,230,1226,118,1251,118","turnLeft();Parking_right(3);"),Connection("7210D","1226,230,1226,139,1251,139","turnLeft();Parking_right(4);"),Connection("7210E","1226,230,1226,162,1251,162","turnLeft();Parking_right(5);"),Connection("729A","1226,230,1226,70,1203,70","turnLeft();Park_left(1);"),Connection("729B","1226,230,1226,91,1203,91","turnLeft();Park_left(2);"),Connection("729C","1226,230,1226,118,1203,118","turnLeft();Park_left(3);"),Connection("729D","1226,230,1226,139,1203,139","turnLeft();Park_left(4);"),Connection("729E","1226,230,1226,162,1203,162","turnLeft();Park_left(5);"),Connection("7371","1226,230,1226,17","Drive_yellow();"),Connection("7310A","1226,230,1226,70,1251,70","Parking_right(5);"),Connection("7310B","1226,230,1226,91,1251,91","Parking_right(4);"),Connection("7310C","1226,230,1226,118,1251,118","Parking_right(3);"),Connection("7310D","1226,230,1226,139,1251,139","Parking_right(2);"),Connection("7310E","1226,230,1226,162,1251,162","Parking_right(1);"),Connection("739A","1226,230,1226,70,1203,70","Park_left(1);"),Connection("739B","1226,230,1226,91,1203,91","Park_left(2);"),Connection("739C","1226,230,1226,118,1203,118","Park_left(3);"),Connection("739D","1226,230,1226,139,1203,139","Park_left(4);"),Connection("739E","1226,230,1226,162,1203,162","Park_left(5);"),Connection("7473","1226,304,1226,230","turnLeft();Drive_yellow();"),Connection("7574","1184,282,1184,304,1226,304","turnLeft();Drive_white();"),Connection("10A71","1251,70,1226,70,1226,17",""),Connection("10B71","1251,91,1226,91,1226,17",""),Connection("10C71","1251,118,1226,118,1226,17",""),Connection("10D71","1251,139,1226,139,1226,17",""),Connection("10E71","1251,162,1226,162,1226,17",""),Connection("1A3","80,280,80,304,183,304",""),Connection("1B3","103,280,103,304,183,304",""),Connection("1C3","125,280,125,304,183,304",""),Connection("1D3","147,280,147,304,183,304",""),Connection("2A15","409,90,409,68,501,68",""),Connection("2B15","432,90,432,68,501,68",""),Connection("2C15","455,90,455,68,501,68",""),Connection("3A19","426,208,426,230,501,230",""),Connection("3B19","448,208,448,230,501,230",""),Connection("3C19","471,208,471,230,501,230",""),Connection("4A17","525,94,503,94,503,158",""),Connection("4B17","525,113,503,113,503,158",""),Connection("4C17","525,136,503,136,503,158",""),Connection("5A48","841,92,866,92,866,158",""),Connection("5B48","841,109,866,109,866,158",""),Connection("5C48","841,135,866,109,866,158",""),Connection("6A57","889,206,889,230,954,230",""),Connection("6B57","911,206,911,230,954,230",""),Connection("6C57","933,206,933,230,954,230",""),Connection("7A61","1000,90,1024,90,1024,158",""),Connection("7B61","1000,110,1024,110,1024,158",""),Connection("7C61","1000,134,1024,134,1024,158",""),Connection("8A69","1045,90,1045,68,1138,68",""),Connection("8B69","1069,90,1069,68,1138,68",""),Connection("8C69","1091,90,1091,68,1138,68",""),Connection("8D69","1113,90,1113,68,1138,68",""),Connection("9A71","1203,70,1226,70,1226,17",""),Connection("9B71","1203,91,1226,91,1226,17",""),Connection("9C71","1203,118,1226,118,1226,17",""),Connection("9D71","1203,139,1226,139,1226,17",""),Connection("9E71","1203,162,1226,162,1226,17","")]

Connections = []
lineDraw = []
functions = []

ContinueConMigo = True

line = ""
createdDog = ""

lastX = 0
lastY = 0
    
def determineNode(coord):
    x,y=coord
    for ctr in range(0,len(nList)):
        if x>= nList[ctr].x1 and x<= nList[ctr].x2 and y>=nList[ctr].y1 and y<=nList[ctr].y2:
            return nList[ctr].name
            break
        
if __name__ == "__main__":
    root = Tk()

    #setting up a tkinter canvas with scrollbars
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    canvas = Canvas(frame, bd=0, width=1280, height=320)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    frame.pack(fill=BOTH,expand=1)

    #adding the image
    img = ImageTk.PhotoImage(Image.open("shivaMap.png"))
    canvas.create_image(0,0,image=img,anchor="nw")
       
    #function to be called when mouse is clicked
    def printcoords(event):
        global line
        global lineDraw
        global functions
        global createdDog
        global lastX
        global lastY
        
        dogImg = ImageTk.PhotoImage(Image.open("dog.png"))
        myDog = Label(image=dogImg)
        myDog.image = dogImg
        
        canvas.delete(line)
        canvas.delete(createdDog)
        #outputting x and y coords to console
        frame.master.title(str(determineNode((event.x,event.y)))+" "+str(int(event.x))+" "+str(int(event.y)))

        appension = determineNode((event.x,event.y))
        if(appension):
            lineDraw.append(appension)
            Connections = []
            if len(lineDraw)>1:
                ctr2Use = 0
                while ctr2Use<len(lineDraw)-1:
                    Connections.append(str(lineDraw[ctr2Use])+str(lineDraw[ctr2Use+1]))
                    ctr2Use += 1

            line2Draw = ""
            found = False
            functions = []
            for ctr in Connections:
                found = False
                for ctr2 in cList:
                    if ctr2.nodes == ctr:
                        found = True
                        line2Draw += ctr2.coord +","
                        functions.append(str(ctr2.func)+"  //node connection "+str(ctr2.nodes))
                if not found:
                    lineDraw = lineDraw[:-1]
                    ctypes.windll.user32.MessageBoxA(0, "Connection not found!", "Error 404:", 0)
            if found:
                print functions[-1]
            if len(line2Draw)>1:
                canvas.delete(canvas.create_image((lastX,lastY),image=dogImg))
                line = canvas.create_line(eval(line2Draw[:-1]), width=2,fill="magenta", capstyle="round", arrow="last")
                splitIt = line2Draw[:-1].split(',')
                lastX = splitIt[-2]
                lastY = splitIt[-1]
                createdDog = canvas.create_image((splitIt[-2],splitIt[-1]),image=dogImg)

        else: #if not wasn't found
            ctypes.windll.user32.MessageBoxA(0, "Node not found!", "Error 404:", 0)
            Connections = []
            if len(lineDraw)>1:
                ctr2Use = 0
                while ctr2Use<len(lineDraw)-1:
                    Connections.append(str(lineDraw[ctr2Use])+str(lineDraw[ctr2Use+1]))
                    ctr2Use += 1

            line2Draw = ""
            for ctr in Connections:
                found = False
                for ctr2 in cList:
                    if ctr2.nodes == ctr:
                        line2Draw += ctr2.coord +","
                        found = True
                if not found:
                    lineDraw = lineDraw[:-1]
                    ctypes.windll.user32.MessageBoxA(0, "Connection not found!", "Error 404:", 0)
            if len(line2Draw)>1:
                canvas.delete(canvas.create_image((lastX,lastY),image=dogImg))
                line = canvas.create_line(eval(line2Draw[:-1]), width=2,fill="magenta", capstyle="round", arrow="last")
                splitIt = line2Draw[:-1].split(',')
                lastX = splitIt[-2]
                lastY = splitIt[-1]
                createdDog = canvas.create_image((splitIt[-2],splitIt[-1]),image=dogImg)
                
    def onKeyPress(event):
        global lineDraw
        global line
        global functions
        global createdDog

        dogImg = ImageTk.PhotoImage(Image.open("dog.png"))
        myDog = Label(image=dogImg)
        myDog.image = dogImg

        if event.char == chr(27):
            root.quit()
        elif event.char == chr(26):
            lineDraw = lineDraw[:-1]
            canvas.delete(line)
            canvas.delete(createdDog)

            functions = functions[:-1]
            print 'Delete last'
            #draws the line
            canvas.delete(line)
            Connections = []
            if len(lineDraw)>1:
                ctr2Use = 0
                while ctr2Use<len(lineDraw)-1:
                    Connections.append(str(lineDraw[ctr2Use])+str(lineDraw[ctr2Use+1]))
                    ctr2Use += 1

            line2Draw = ""
            for ctr in Connections:
                for ctr2 in cList:
                    if ctr2.nodes == ctr:
                        line2Draw += ctr2.coord +","
            if len(line2Draw)>1:
                line = canvas.create_line(eval(line2Draw[:-1]), width=2,fill="magenta", capstyle="round", arrow="last")
                splitIt = line2Draw[:-1].split(',')
                createdDog = canvas.create_image((splitIt[-2],splitIt[-1]),image=dogImg)
                
    #mouseclick event
    canvas.bind("<Button 1>",printcoords)
    root.bind("<KeyPress>",onKeyPress)    

    root.mainloop()

print 'Escape detected'
stockFile = open("newCode.c","r")
newLines = []

#get stock code
for line in stockFile:
    newLines.append(line)
    if line == "task main(){\n":
        break

#print newLines
#raw_input()

#get chosen functions
for line in functions:
    newLines.append(str(line)+"\n\t")
newLines.append("}\n")

print newLines

stockFile.close()
newFile = open("newCode2.c","w")
for line in newLines:
    #print line
    newFile.write(line)

newFile.close()
os.remove("newCode.c")
os.rename("newCode2.c","newCode.c")
